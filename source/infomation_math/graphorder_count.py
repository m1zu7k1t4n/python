# encoding : utf-8
import csv

def solve(data):
    while(1):
        data.sort(reverse=True)
        S = data.pop(0)
        try:
            for i in range(S):
                data[i] -= 1
        except:
            return False
        if any(filter(lambda x: x < 0, data)):
            return False
        if len(data) == 1:
            return True

def isNotHands(indata):
    return len(list(filter(lambda x:x%2==1,indata))) % 2 == 1 or max(indata) >= (len(indata) + 1)

def isGraph(path):
    try:
        with open(path, "r", encoding="utf-8", errors="", newline="" ) as csv_file:
            f = csv.reader(csv_file,
                            delimiter=",",
                            doublequote=True,
                            lineterminator="\n",
                            quotechar='"',
                            skipinitialspace=True
                )
            cantDo = "グラフ化できない"
            canDo = "グラフ化できる"
            while(1):
                try:
                    indata = [int(x) for x in f.__next__()]
                except:
                    break
                print(cantDo if isNotHands(indata) else (canDo if solve(indata) else cantDo))
    except:
        print("{} のパスは不正です。".format(path))

if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) != 1:
        for path in args[1:]:
            isGraph(path)
    else:
        isGraph("input.csv")
