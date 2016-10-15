#!/usr/bin/env python
# coding: utf8

from TwitterSearch import *
from datetime import datetime
import os, sys, time, json, configparser

def chachetime(datei):
    systime = time.time()
    filetime = os.path.getmtime(datei)
    global daysDiff
    daysDiff = (systime-filetime)
    if(daysDiff < 3600): # Wenn Cache älter als 1 Stunde
        return True # Chache aktuell
    else:
        return False # Neuen Cache erstellen


def gettweets(hashtag):
    datei = '{}.json'.format(hashtag)
    if (os.path.isfile(datei) and chachetime(datei)):  # Wenn Cache existiert
        with open(datei) as cachefile:  # Lese Cache aus
            print("Ausgabe aus Cache " + datei)
            print("Cache wurde zuletzt vor " + str(round(daysDiff / 3600, 2)) + " Stunde/n aktualisiert")
            return json.loads(cachefile.read())  # Gebe Cache aus

    try:
        print("Chache wird neu erstellt")
        tso = TwitterSearchOrder()  # Twitter Objekt erstellen
        tso.set_keywords(['#' + hashtag])  # Wir suchen nach einem hashtag
        tso.set_language('de')  # Nur Deutsche Tweets
        tso.set_include_entities(False)  # Kein Entity Zeug ausgeben

        Config = configparser.ConfigParser()
        if os.path.isfile("config.ini"):
            Config.read("config.ini")
        else:
            print("The config file does not exist, please create a new config with the example file")
            sys.exit()

        consumer_key = Config.get("Twitter API", "consumer_key")
        consumer_secret = Config.get("Twitter API", "consumer_secret")
        access_token = Config.get("Twitter API", "access_token")
        access_token_secret = Config.get("Twitter API", "access_token_secret")

        # Objekt mit Zugangsdaten erstellen
        ts = TwitterSearch(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
            )

        tweets = set()
        for tweet in ts.search_tweets_iterable(tso):
            tweets.add(tweet['text'])

        tweets = list(tweets)

        with open(datei, 'w') as cachefile:
            tweetsasjson = json.dumps(tweets)
            cachefile.write(tweetsasjson)

        return tweets

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)
