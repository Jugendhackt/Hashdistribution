import re


def parse_tweettext(tweettext):
    text = TweetText(tweettext)
    print(text)


class TweetText:
    def __init__(self, tweettext):
        self.tweettext = tweettext

    def getHashtags(self):
        hashtags = []
        stripchars = '.,;:?!"\'^`'

        text_parts = self.tweettext.split()
        for part in text_parts:
            if part.startswith("#"):
                hashtag = part
                hashtag.strip(stripchars)
                hashtags.append(hashtag)
            if "#" in part:
                pos = part.index("#")
                hashtag = part[pos:]
                if hashtag not in hashtags:
                    hashtag.strip(stripchars)
                    hashtags.append(hashtag)
        return hashtags
