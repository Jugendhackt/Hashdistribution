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
                if hashtag not in hashtags:
                    hashtags.append(hashtag)
        return hashtags
