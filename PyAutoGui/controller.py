# coding: utf-8

import pyautogui as pa
import time


def trans_number(strings):
    strings = strings.replace('\n', '')
    data = [int(x) for x in strings.split(" ")]
    return data


def pos_memory():
    f = open('mouse_pos.txt', 'w')
    now = pa.position()
    while True:
        next = pa.position()
        if now != next:
            f.write(str(now[0]) + " " + str(now[1]) + "\n")
            print("WriteNow")
        now = next
        if next == (0, 0):
            break
        time.sleep(0.07)
    f.close()


def pos_move():
    f = open('mouse_pos.txt', 'r')
    for row in f:
        x, y = trans_number(row)
        pa.moveTo(x, y)
    f.close()

def test():
    time.sleep(5)

    # 現在の位置を取得する
    x0,y0 = pa.position()

    # PyAutoGUIの各動作の間隔を0.1秒に指定
    pa.PAUSE = 0.1

    n = 256
    # マウスを押して
    pa.mouseDown(button="left")
    for v,i in enumerate(range(n)[::16]):
        # 左上，右上，右下，左下，左上と移動してみる

        pa.moveTo(x0 , y0)
        pa.moveTo(x0 + i , y0)
        pa.moveTo(x0 + i , y0 + i)
        pa.moveTo(x0 , y0 + i )
        pa.moveTo(x0 , y0)
        # マウスを戻す
    pa.mouseUp()
