import TweetParser
import crawler
import json


#with open("jugendhackt.json") as cachefile:
#     json_data = json.loads(cachefile.read())
main_hashtag = "jugendhackt"
max_int = 2

hashtagdict = {}


def crawlHashtags(hashtagToCrawl, hashtagdict, depth=1):
    depth += 1
    try:
        json_data = crawler.gettweets(hashtagToCrawl)
    except:  # take care of all those ugly errors if there are some
        return hashtagdict
    hashtags = []
    if depth >= max_int:
        return hashtagdict
    for tweet in json_data:
        tweettext = TweetParser.TweetText(tweet)
        #print(tweettext.getHashtags(), tweet)
        for hashtag in tweettext.getHashtags():
            if (hashtag.lower() != main_hashtag.lower()) and (len(hashtag) > 1):
                hashtags.append(hashtag.lower())

    for hashtag in hashtags:
        hashtagdict[hashtag] = crawlHashtags(hashtag, hashtagdict, depth)

    return hashtagdict

hashtagdict = crawlHashtags(main_hashtag, hashtagdict)

with open(".cache/RecursiveJugendhackt.json", 'w') as cachefile:
    # json.dump(hashtagdict, cachefile)
    cachefile.write(json.dumps(hashtagdict))
