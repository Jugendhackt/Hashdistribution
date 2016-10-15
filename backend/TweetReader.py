import TweetParser
import crawler
import json


#with open("jugendhackt.json") as cachefile:
#     json_data = json.loads(cachefile.read())

json_data = crawler.gettweets("jugendhackt")

for tweet in json_data:
    tweettext = TweetParser.TweetText(tweet)
    print(tweettext.getHashtags(), tweet)
