# coding : utf-8
import random
import collections


class roulette(object):
    def __init__(self):
        self.doller = 0
        self.trial = 0
        self.iswin = ""

    def spin(self, bet):
        self.trial += 1
        self.doller -= bet
        catch = random.randint(0, 36)
        if catch == 0 or catch % 2 == 0:
            if not(catch == 10 or catch == 28):
                self.doller += 0
                self.iswin = "lose"
                return False
        else:
            self.doller += bet * 2
            self.iswin = "win"
            return True

    def __call__(self):
        return self.trial, self.doller, self.iswin


def betsum(bet_list):
    return bet_list[0] + bet_list[-1] * 2


def main():
    rou = roulette()
    winnum = 0
    bet_list = collections.deque([x for x in range(100)])
    for _ in range(100000):
        if rou.spin(betsum(bet_list)):
            bet_list.pop()
            bet_list.popleft()
            bet_list.append(betsum(bet_list))
        else:
            bet_list.append(betsum(bet_list))
        trial, doller, iswin = rou()
        winnum += 1 if iswin == "win" else 0
        if trial % 10000 == 0:
            print(
                f"試行回数: {trial}, お金: {doller}, 勝敗: {iswin}, 勝率: {winnum / trial}")


if __name__ == '__main__':
    main()
