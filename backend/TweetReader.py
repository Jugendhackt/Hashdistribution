import TweetParser
import crawler
import json
import copy


def crawlHashtags(hashtagToCrawl, indict, maxdepth, depth=0):
    outdict = copy.copy(indict)
    depth += 1
    try:
        json_data = crawler.gettweets(hashtagToCrawl)
    except:  # take care of all those ugly errors if there are some
        return outdict
    hashtags = {}
    if depth >= maxdepth:
        return outdict
    for tweet in json_data:
        tweettext = TweetParser.TweetText(tweet)
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
        outdict[hashtag]['childs'] = list(crawlHashtags(hashtag, indict, maxdepth, depth).values())

    return outdict


def getTopHashtags(hashtag, maxdepth):
    hashtagdict = {}
    finallist = list(crawlHashtags(hashtag, hashtagdict, int(maxdepth)).values())
    finaldict = {"ht": "#" + hashtag, "count": 1, "childs": finallist}
    return json.dumps(finaldict)
