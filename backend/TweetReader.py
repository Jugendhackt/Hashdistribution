import TweetParser
import crawler
import json


#with open("jugendhackt.json") as cachefile:
#     json_data = json.loads(cachefile.read())
main_hashtag = "jugendhackt"
max_int = 5

hashtagdict = {}


def crawlHashtags(hashtagToCrawl, hashtagdict, depth=1):
    depth += 1
    json_data = crawler.gettweets(hashtagToCrawl)
    with open(".cache/RecursiveJugendhackt.json", 'w') as cachefile:
        #json.dump(hashtagdict, cachefile)
        cachefile.write(json.dumps(hashtagdict))
    hashtags = []
    if depth >= max_int:
        return
    for tweet in json_data:
        tweettext = TweetParser.TweetText(tweet)
        #print(tweettext.getHashtags(), tweet)
        for hashtag in tweettext.getHashtags():
            if (hashtag.lower() != main_hashtag.lower()) and (len(hashtag) > 1):
                hashtags.append(hashtag.lower())

    for hashtag in hashtags:
        hashtagdict[hashtagToCrawl] = {}
        crawlHashtags(hashtag, hashtagdict[hashtagToCrawl], depth)

crawlHashtags(main_hashtag, hashtagdict)
