import TweetParser
import crawler
import json
import server
import copy
import pprint

# with open("jugendhackt.json") as cachefile:
#     json_data = json.loads(cachefile.read())
main_hashtag = "#jugendhackt"
max_int = 3


def crawlHashtags(hashtagToCrawl, indict, maxdepth, depth):
    outdict = copy.copy(indict)
    #depth += 1
    try:
        json_data = crawler.gettweets(hashtagToCrawl)
    except:  # take care of all those ugly errors if there are some
        return outdict
    hashtags = {}
    if depth >= maxdepth:
        return outdict
    for tweet in json_data:
        tweettext = TweetParser.TweetText(tweet)
        # print(tweettext.getHashtags(), tweet)
        for hashtag in tweettext.getHashtags():
            if (hashtag.lower() != hashtagToCrawl.lower()) and (len(hashtag) > 1):
                hashtag = hashtag.lower()
                if hashtag in hashtags:
                    hashtags[hashtag] += 1
                else:
                    hashtags[hashtag] = 1
    hashtuples = hashtags.items()
    sorted_tuple = sorted(hashtuples, key=lambda x: x[1])[-5:]

    for hashtag, count in sorted_tuple:
        outdict[hashtag] = {}
        outdict[hashtag]['ht'] = hashtag
        outdict[hashtag]['count'] = count
        outdict[hashtag]['childs'] = list(crawlHashtags(hashtag, indict, depth).values())

    return outdict


def getTopHashtags(hashtag, maxdepth):
    hashtagdict = {}
    finallist = list(crawlHashtags(hashtag, hashtagdict, int(5)).values())
    finaldict = {"ht": "#" + hashtag, "count": 1, "childs": finallist}
    return json.dumps(finaldict)

# with open(".cache/RecursiveJugendhackt.json", 'w') as cachefile:
#    # json.dump(hashtagdict, cachefile)
#    #import pdb;pdb.set_trace()
#    cachefile.write(json.dumps(finaldict))


# print(json.dumps(finaldict, indent=4))
