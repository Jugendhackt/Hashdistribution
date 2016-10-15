#!/usr/bin/env python
# coding: utf8

from TwitterSearch import *
from datetime import datetime
import os, sys, time, json, configparser


def gettweets(hashtag):
    datei = '{}.json'.format(hashtag)
    if (os.path.isfile(datei)):  # Wenn Cache existiert
        fmt = '%a %b %m %H:%M:%S %Y' #Sat Oct 15 11:24:47 2016
        systime = time.asctime(time.localtime(time.time()))
        filetime = time.ctime(os.path.getmtime(datei))
        d1 = datetime.strptime(systime, fmt)
        d2 = datetime.strptime(filetime, fmt)
        daysDiff = (d2-d1).days
        print(daysDiff)
        with open(datei) as cachefile:  # Lese Cache aus
            return json.loads(cachefile.read())  # Gebe Cache aus

    else: # Wenn kein Cache da ist.
        try:
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
