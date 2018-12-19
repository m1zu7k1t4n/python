import zenhan
import tweepy
import sys

CONSUMER_KEY = 'E9v6u5ZD0BzyFpsNjkHyLK9Ei'
CONSUMER_SECRET = 'isWOywQh6HwUZSRDi16mSE4wMUU6qzqylPMAolyPpzOEq8EBGj'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '2404678368-2VbxDRkTKNexcK8ReVTj7gbck1GfAZ7mq4euUyj'
ACCESS_SECRET = 'kn56g4kC1gArOBFdp6lAa2DO5khEg1AsL2n7IZsiAczcA'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


def tweet(strs):
    strs = strs.replace(" ", "　")
    data = strs.split("　")
    maxstr = len(max(data, key=len))
    newstr = list()
    result = ""
    for word in data:
        word = word.replace("ー", "｜")
        word = word.replace("-", "｜")
        newstr.insert(0, zenhan.h2z(word + ("　" * (maxstr - len(word)))))
    for vert in range(maxstr):
        for side in range(len(newstr) - 1):
            result += newstr[side][vert] + zenhan.h2z(" ")
        side += 1
        result += newstr[side][vert]
        result += "\r\n"
    try:
        if result[0] == "　":
                result = "、" + result[1:]
        api.update_status(result)
    except Exception:
        leng = len(result)
        line_div = (leng // 140) + 1
        tweets = list()
        result = ""
        for vert in range(maxstr):
            for side in range(len(newstr) - 1):
                result += newstr[side][vert] + zenhan.h2z(" ")
            side += 1
            result += newstr[side][vert]
            result += "\r\n"
            if (vert % ((maxstr // line_div) - 1) == 0) and (vert != 0):
                tweets.insert(0, result)
                result = ""
        tweets.insert(0, result)
        for res in tweets:
            if res[0] == "　":
                res = "、" + res[1:]
            api.update_status(res)
            # print(res)

def main():
    comm = sys.argv
    tweet(comm[1])


if __name__ == '__main__':
    main()
