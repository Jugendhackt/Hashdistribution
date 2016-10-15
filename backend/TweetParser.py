import re


def parse_tweettext(tweettext):
    text = TweetText(tweettext)
    print(text)


class TweetText:
    def __init__(self, tweettext):
        self.tweettext = tweettext

    def getHashtags(self):
        hashtags = []
        stripchars = '.,;:?!…"()'

        text_parts = self.tweettext.split()
        for part in text_parts:
            if "#" in part:
                pos = part.index("#")
                hashtag = part[pos:]
                hashtag = hashtag.strip(stripchars)
                #import pdb;pdb.set_trace()
                if hashtag not in hashtags:
                    hashtags.append(hashtag)
        return hashtags
