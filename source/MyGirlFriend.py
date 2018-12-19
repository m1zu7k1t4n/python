# coding: utf-8

class GirlFriend(object):
    def __init__(self, yourname="ふみ", myname="あなた"):
        self.yourname = yourname
        self.myname = myname
        print("{0}が私の運命の人なの？私{1}っていうの、よろしくね".format(myname, yourname))

    def check(self):
        print("いるよ")

    def __del__(self):
        print("私を捨てるの？そんなの絶対ゆるさない。ゆるさないんだから。ぜったいわたしはあなたからはなれたりしない")
        gf = GirlFriend(self.yourname, self.myname)


gf = GirlFriend()
print()
del gf
