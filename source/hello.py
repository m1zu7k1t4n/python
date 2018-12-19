# coding: UTF-8

def end():
    print()

print("長さに関するもの")
msg = "abcdefghi"
print(len(msg))
print(msg.find("g"))
print(msg[2:5])

print("----明示的な型変換")
print(5 + int("5"))
age = 20
print("I'm" + str(age))

print("----リスト 多言語で言う配列")
sales = [255, 120, 350, 203, "abc"]
print(len(sales)) # 5
print(sales[2]) # 350
sales[2] = 100
print(sales[2]) # 100
print(sales[4])

print("----リスト 要素の追加")
sales = ["A", "B", "C"]
sales.append("D")
print(sales)     # ["A", "B", "C", "D"]

print("----リスト 別のリストの要素の追加")
sales = ["A", "B", "C"]
sales.extend(["D", "E"])
print(sales)      # ["A", "B", "C", "D", "E"]

print("----リスト リストの連結")
sales == ["A", "B", "C"]
newsales = sales + ["D", "E"]
print(newsales)    # ["A", "B", "C", "D", "E"]
newsales = sales * 3 #積の回数だけ同じリストを後ろに追加
print(newsales)

print("リストによる文字列取り出し")
x = ["python","voip","spam"]
for i in x:
    for v in i:
    print(v)
    print()
end()

print("----in 真偽値で判断")
print(120 in sales) # True

print("----range 数字の連番を単純に作成する")
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3,10))) # [3, 4, 5, 6, 7, 8, 9]
print(list(range(3,10,2))) # [3, 5, 7, 9]

print("----sort : reverse")
sales = [100, 40, 74, 30]
print(sales)
sales.reverse() # [30, 74, 40, 100]
print(sales)
sales.sort() # [30, 40, 74, 100]
print(sales)
sales.reverse() # [100, 74, 40, 30]
print(sales)

print("----文字列とリスト")
d = "2013/12/15"
print(d.split("/")) # [100, 74, 40, 30]
a = ["a", "b" , "c"]
print("-".join(a)) # a-b-c

print("----タプル（変更ができない）") # 小括弧で区切る
b = (2, 6, 9)
print(len(b)) # 3
print(b * 3) # (2, 6, 9, 2, 6, 9, 2, 6, 9)
# b[2] = 10 などの書き換えはできない

print("----リストタプルの相互変換")
c = list(b) #リストへ変換
print(str(c) + " リスト形式")
d = tuple(c) #タプルへ変換
print(str(d) + " タプル形式")

print("----セット(集合型) 重複を許さない")
a = set([1, 2, 3, 4])
b = set([3, 4, 5])
c = set([1, 2, 3, 4, 3, 2])
print(c) # set([1, 2, 3, 4])
# "-" 差集合を求める
print(a - b) # set([1, 2])
# "|" 和集合を求める
print(a | b) # set([1, 2, 3, 4, 5])
# "&" 席集合を求める
print(a & b) # set([3, 4])
# "^" どちらかにしかないものを求める
print(a ^ b) # set([1, 2, 5])

print("----辞書 key value") #  dict 波括弧を使う
sales = {"frendsA":100, "frendsB":200, "frendsC":300}
print("""sales = {"frendsA":100, "frendsB":200, "frendsC":300}""")
print(sales) # {'frendsA': 100, 'frendsC': 300, 'frendsB': 200}
#必ずしも入れた順に並ぶとは限らない
print(str(sales["frendsA"]) + " frendsAの値")
sales["frendsB"] = 500
print(sales)
print("frendsC" in sales) # True:真偽値で返される

print("----一覧を返す keys, values, items")
print(str(list(sales.keys())) + ":keys()")
print(str(list(sales.values())) + ":values()")
print(str(list(sales.items())) + ":items()")

print("----%による値の入れ込み")
a = 10
b = 1.23456789
c = "frendsA"
d = {"frendsB":200, "frendsC":400}
print("age: %d" % a)
print("age: %10d" % a)
print("age: %010d" % a)
print("price: %f" % b)
print("price: %.2f" % b)
print("name: %s" % c)
print("sales: %(frendsB)d" % d)
print("%d and %f" % (a, b))

print("----条件分岐")
score = 100
if score > 60:
    print("ok!")
    print("OK!")
# 比較演算子 > < >= <= == !=
# 論理演算し and or not
if score > 60 and score < 120:
    print("andOK!")
if 80 < score < 120:
    print("範囲制限OK！")
# elif else の使い方
if score > 60:
    print("ok!")
elif score > 40:
    print("oh...")
else:
    print("dam!")
# if文の特殊構文
print("OK!" if score > 120 else "Dam!")
print("OK!" if score > 80 else "Dam!")

print("----for文によるループ処理")
sales = [13, 2576, 24, 354]
sum = 0
for sale in sales:
    print(sale)

# elseで処理を抜けるときに一度だけ実行させることが出来る
for sale in sales:
    sum += sale
else:
    print(sum)

print("--NomalRange")
for i in range(10):
    print(i)

print("--ContinueRange:4を飛ばす") # continueに入った場合そのループの処理から次に移る
for i in range(10):
    if i == 4:
        continue
    print(i)

print("--BreakRange:4で抜ける") # breakに入った場合そのループ処理を抜ける
for i in range(10):
    if i == 4:
        break
    print(i)

print("--辞書でループ処理--")
users = {"frendsA": 200, "frendsB": 300, "frendsC": 400}
for key,value in list(users.items()):
    print("key: %s value: %d" % (key, value))
for key in list(users.keys()):
    print(key)
for value in list(users.values()):
    print(value)

print("--whileループ処理--")
n = 0
while n < 10:
    print(n)
    n += 1
else:
    print("end")

n = 0
while n < 10:
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1
else :
    print("end")

n = 0
while n < 10:
    if n == 4:
        break
    print(n)
    n += 1
else:
    print("end")

print("--関数を使う--")
def hello():
    print("helloPython\n")
hello()

def hello(name):
    print("helloPython for %s \n" % name)
hello("genta")

def hello(name,num):
    print("helloPython for %s \n" % name * num)
hello("kojima", 2)
hello("batako", 3)

def hello(name,num = 5):
    print("helloPython for %s \n" % name * num)
hello("kenji")
hello(num = 2,name = "sasuke")

def hello(name,num = 5):
    return "helloPython for %s \n" % name * num
s = hello("maruko",2)
print(s)

print("--passを使う--")#関数の中身は後で書きたい時に使う
def pass_func():
    pass

print("--map,lambdaを使う--")#リストを用いたりして使える、また無名関数も使える
def pow_func(x):
    return x * x
print(list(map(pow_func, [3, 4, 5])))

print([x * x for x in [3, 4, 5]])#lambdaで無名関数を作る　使い捨て関数

print("--オブジェクトを作ってみよう--")
#オブジェクト(変数と関数をまとめたもの)
#クラス:オブジェクトの設計図
#インスタンス:クラスを実体化したもの
class User(object):
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("my name is %s!" % self.name)
class SuperUser(User):
    def shout(self):
        print("%s is SUPER!!" % self.name)

"""

class内で定義されたselfはclass自身を指していて
self.nameの場合、Userクラスのname変数という使い方になる

"""

tom = SuperUser("Tom")
tom.greet()
tom.shout()

print("--モジュールを使う--")
import math, random
print(math.ceil(5.2)) #6
for i in range(5):
    print(random.random())
end()
print("random.shuffleを使う")
alist = list(range(11))
print(alist)
random.shuffle(alist)
print(alist)
end()

print("--with構文--")
#close()を呼び出す場合、予め終了地点が定められてる時に
#with構文内に収めることで安全に終了処理を呼び出すことできる

print("--osの機能を使う--")
#import os
#"os.system('ls -l')"
#wgetの並列ダウンロードの呼び出し
#os.system('xargs -P 20 -n 1 wget -q -nc $1 -P ./Directory < ' + filepath)

#win32guiの色々
#win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)
#hwnd ウィンドウのハンドル情報
#win32con.WM_SETTEXT,外部のWindowsに文字列を入力
#第3引数　未使用
#第4関数　入力したい文字列
#"win32gui.SendMessage(self.play, win32con.BM_CLICK, 0, 0)"
#self.play ウィンドウの中のself.playの文字列と同じものを選択
#wind32con.BM_CLICK windowsのクリックを内部的に処理
#第3引数　第4引数　未使用

print("複数のfor..inを含む内包表記")
a = range(3)
b = range(4)
a = [x + y for x in a for y in b]
print(a)
end()

print("複素数リテラル")
c1 = 1 + 1j
c2 = 2 + 4j
print(c1 + c2)
end()

print("n個おきのスライス")
b = list(range(20))
b = b[::2]
print(b)
end()

print("スライスによるリストのコピー")
a = list(range(10))
b = a
print(b)
print(b is a)
c = a[:]
print(c)
print(c is a)
end()

print("Ellipsisと呼ばれる省略オブジェクト 肯定的でTrueを渡す処理")
print(...)
print(bool(...))
if ...:
    print("ok")
else:
    print("no")
end()

print("キーワード限定引数")
def KeywordOnly(number, *, string):
    print(number)
    print(string)

KeywordOnly(1,string="str")
print()

print("関数アノテーション 引数と返り値の注釈をつける(強制ではない)")
def FuncAnot(x: int, y: int) -> int:
    return x + y

print(FuncAnot(3,4))
print(FuncAnot("hoge","asd"))
end()

print("グローバル変数の関数内定義")
def GlobalNumber():
    global globalnumber
    globalnumber = 10
GlobalNumber()
print(globalnumber)

print("一つ外側のスコープに属する変数への代入が可能になる")
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c = make_counter()
print(c())
print(c())
print(c())
end()

print("デコレータを作成する関数")
def deco(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('--start--')
        func(*args,**kwargs)
        print('--end--')
    return wrapper

@deco
def test():
    print('Hello Decorator')

test()
end()

print("デコレータを使った処理速度の計測")
def timer(func,times):
    import functools
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(times):
        timestop = []
        print("watch start")
        timestart = time.time()
        func(*args, ** kwargs)
        timestop.append(time.time() - timestart)
        print("time:%03.3f" % (sum(timestop)/len(timestop)))
    return wrapper

@timer
def fortest():
    c = 0
    for i in range(1,1000001):
        c += i
    else:
        print(c)


fortest()
end()

print("引数付きデコレータ")

def greet(before, after):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(before)
            func(*args, **kwargs)
            print(after)
        return wrapper
    return decorator

@greet('Hi','bye')
def introduce(name):
    print(name)

introduce('ypaaaaaaaaaaaa')
end()

print("クラスデコレータ(簡易シングルトン)")

def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class C(object):
    pass

c1 = C()
c2 = C()
print(c1 is c2)
end()

print("関数で中にある関数を呼び出す処理を作る")
def outside(a, b):
    def inside(c, d):
    return c + d
    return inside(a, b)
print(outside(1, 2))

print("クロージャ　関数を予め与えられている引数を覚えている関数")
def outside(a, b):
    def inside(c):
    return a + b + c
    return inside
c = outside(1, 2)
print(c(3))

print("yield from 他のイテレータから値を返すジェネレータを作れる")

def g():
    yield from range(5)
    yield from range(10)

print([i for i in g()])
end()

print("例外処理")
try:
    a = 10 / 0
except Exception as e:
    print("%r" % e )

print("例外を連鎖するときに、送出元の例外を保持する")
try:
    raise Exception('e1') from Exception('e2')
except Exception as e:
    print(e.__cause__)
end()

print("マルチスレッドの使い方")
import threading, time

def prints(name, sleep_time):
    for i in range(2):
        print(name + ': ' + str(i))
        time.sleep(sleep_time)

thread1 = threading.Thread(target=prints, args=('A', 1,))  # Initialize
thread2 = threading.Thread(target=prints, args=('B', 1,))
thread1.start()
#thread1.join() #WAIT HERE
thread2.start()
thread1.join()
thread2.join()
end()

print("マルチスレッドのネットワークIO")
#import threading, time, urllib2
import urllib.request

def get_html(url):
    current_time = time.time()
    response = urllib.request.urlopen(url)
    html = response.read()
    print(url + ': ' + str(time.time() - current_time))

urls = ['http://www.google.com', 'http://www.yahoo.co.jp/', 'https://www.bing.com/']
threads = []

# Start Threads
current_time = time.time()
for url in urls:
    thread = threading.Thread(target=get_html, args=(url,))
    thread.start()
    threads.append(thread)

# Wait Threads
for thread in threads:
    thread.join()

print('Time: ' + str(time.time() - current_time))
end()

print("継承によるマルチスレッドの実現")
# Class definition

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(2):
            print('MyThread: ' + str(i))
            time.sleep(1)

# Run threads

mt = MyThread()  # create thread instance
mt.start()  # start the thread
for i in range(2):
    print('Main: ' + str(i))
    time.sleep(1)
end()
"""
マルチスレッドのクラスを継承した際にrunメソッドを親クラスからオーバーライドした
ここで定義されたものは継承元のstart()より内部呼び出しが起きる為、runメソッドは使用してはいけない
もし使用した場合単純にシングルスレッドになる
"""

print("引数ありのマルチスレッド")
class MyThread(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        for i in range(2):
            print(self.name + ': ' + str(i))
            time.sleep(self.sleep_time)

thread1 = MyThread('A', 1)
thread2 = MyThread('B', 1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end()

print("マルチスレッドによるフィボナッチ数列の解")
class MyThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count
        self.return_value = None   # RETURN VALUE

    def run(self):
        sum_value = 0
        for i in range(1, 1 + self.count):
            sum_value += i
            time.sleep(0.1)
        self.return_value = sum_value   # SET RETURN VALUE

    def get_value(self):  # GETTER METHOD
        return self.return_value

thread1 = MyThread(5)
thread1.start()
thread1.join()
print(thread1.return_value)  # 15
print(thread1.get_value())   # 15


print("numpyの色々") #http://qiita.com/yubais/items/bf9ce0a8fefdcc0b0c97
import matplotlib.pyplot as plt
import numpy.random as npr
import numpy as np
from math import sin, pi
np.set_printoptions(threshold=np.inf)

a = npr.rand()
b = npr.rand(100) #乱数を100個生成
c = npr.rand(100,100)

d = npr.rand(100) * 40 + 30 #30~70の乱数を100個生成

""" 標準正規分布。いわゆるガウシアン。標準正規分布ならば randn() で、平均・分散を指定したい場合は normal() を用いる。"""
e = npr.randn()         # 標準正規分布 (平均0, 標準偏差1)
f = npr.randn(100) + 50      # 標準正規分布を10個生成
g = npr.randn(10,10)    # 標準正規分布による 10x10 の行列
h = npr.normal(50,10)   # 平均50、標準偏差10の正規分布
i = npr.beta(a=3, b=5)

city = ["Sapporo","Sendai","Tokyo","Nagoya","Kyoto","Osaka","Fukuoka"]

j = npr.choice(city)                     # 1個をランダム抽出
k = npr.choice(city,10)                  # 10個をランダム抽出（重複あり）
l = npr.choice(city,5,replace=False) # 5個をランダム抽出（重複なし)

weight = [0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1]
m = npr.choice(city, 10,p=weight)

R = npr.randn(1000)
plt.hist(R,bins=100)
plt.show()

L = 10000                            # 歩数
M = [-1,1]
step = npr.choice(M,L)      # +1 or -1 をL個生成
position = np.cumsum(step)             # 位置の変化
plt.plot(position)
plt.show()
print(np.sum(step))
print(np.sum(position))

print("ネストを減らすitertools") #http://python.civic-apps.com/reduce-nest-loop/
#いつも使うネストループ
for i in range(10):
    for v in range(10):
    print(i, v):

#itertools.productを用いたネストをしないループ
import itertools
for (i, v) in itertools.product(range(10), range(10)):
    print(i, v,)

for (i, v, m) in itertools.product(range(10), range(10), range(10)):
    print(i, v, m)

print("配列の部分列の全取得") #http://python.civic-apps.com/reduce-nest-loop/
#いつも使うネストループ
text = 'ABCDE'
l = len(text)
for f in range(l + 1):
    for e in range(f + 1, l + 1):
    print(text[f:e])

#itertools.combinationsを用いたネストしないループ
text = 'FGHIJ'
l = len(text)
for (f, e) in itertools.combinations(range(l+1), 2):
    print(text[f:e])

print("高レベルなファイル操作") #http://python.civic-apps.com/shutil/
import os
os.mkdir("FileOperate")
with open("./FileOperate/test1.txt", "w") as f:
    f.write("高レベルなファイル操作の実験ファイルだよ！")

#ファイルのコピー
import shutil
shutil.copy("./FileOperate/test1.txt", "./FileOperate/test2.txt")

#ディレクトリまるごとコピー
shutil.copytree("./FileOperate", "./DirOperate")

#ディレクトリまるごと削除
shutil.rmtree("./FileOperate")

#ディレクトリやファイルを移動
shutil.move("./DirOperate", "FileOperate")


print("with文で使えるコンテキストマネージャ型") #http://python.civic-apps.com/with-contextmanager/
from contextlib import contextmanager
@contextmanager
def context_with():
    print("before")
    yield #withのブロック内での処理が行われる
    print("after")

with context_with():
    print(2+3)

print("ジェネレータ関数")
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
    yield number
    number += step

for x in my_range(1, 5):
    print(x)

print("JITコンパイラを使う　高速化手順")
from numba import jit
@jit
def numb():
    for i in range(1000000, 1010001):
    for j in range(2, i):
        if i % j == 0:
        break
        if j == i - 1:
        print(i)
end()

print("桁切り")
a = 1.23456
print(str(round(a,2))) # 1.23 四捨五入

print("クイックソートの３行ソート")
def quicksort(x):
    if x==[]: return []
    return (quicksort( [a for a in x[1:] if a <= x[0]] ) + [x[0]] + quicksort( [a for a in x[1:] if a > x[0]] ))

data = np.random.rand(10) * 100
print(quicksort(data))

print("コマンドライン引数")
import sys

args = sys.argv
print(args[1])
print(args[2])
