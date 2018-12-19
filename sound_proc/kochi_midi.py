# -*- coding:utf-8 -*-
''' MIDI keyboard
鍵盤の下の方を押すほど大音量
'''
from tkinter import *
import pygame.midi
from pygame.locals import *
import time

INSTRUMENT = 0  # 楽器の種類 (0-127)
# 0: Piano, 19:Organ, 56:Trumpet, 91:Voice 等
WIDTH, HEIGHT = 920, 128  # 画面の大きさ
KEY_WIDTH = WIDTH // 23  # 鍵盤の幅
NOTE_CENTER = 60  # 中央の音。C(ド) の音を指定
BLACK_KEY = (1, 0, 1, 1, 0, 1, 1) * 4  # ０＝白鍵　 1 ＝黒鍵

pygame.midi.init()
midiout = pygame.midi.Output(pygame.midi.get_default_output_id())
midiout.set_instrument(INSTRUMENT)
keys = WIDTH // KEY_WIDTH
note_start = NOTE_CENTER - 14
note_no = None
vel = 0


def ButtonPress(event):
    mX = event.x
    mY = event.y
    index = -1
    val = 0
    for key, b in enumerate(BLACK_KEY):
        if b:
            val += 2
    else:
        val += 1
    if b:
        if key == 0:
            if mX < KEY_WIDTH // 3 and mY < 3 * HEIGHT // 5:
                note_no = note_start
                vel = 128 * mY * 5 // (3 * HEIGHT)
                midiout.note_on(note_no, vel)
                index = key
                print(note_no)
            else:
                x = key * KEY_WIDTH - KEY_WIDTH // 3
                if x < mX and mX < x + 2 * KEY_WIDTH // 3 and mY < 3 * HEIGHT // 5:
                    note_no = note_start + val - 2
                    vel = 128 * mY * 5 // (3 * HEIGHT)
                    midiout.note_on(note_no, vel)
                    index = key
                    print(note_no)
    if index == -1:
        val = 0
        for key in range(keys):
            if BLACK_KEY[key]:
                val += 2
            else:
                val += 1
            x = key * KEY_WIDTH
            if x < mX and mX < x + KEY_WIDTH:
                note_no = note_start + val - 1
                vel = 128 * mY // HEIGHT
                midiout.note_on(note_no, vel)
                index = key
                print(note_no)
    if index == -1:
        return


def ButtonRelease(event):
    mX = event.x
    mY = event.y
    index = -1
    val = 0
    for key, b in enumerate(BLACK_KEY):
        if b:
            val += 2
        else:
            val += 1
        if b:
            if key == 0:
                if mX < KEY_WIDTH // 3 and mY < 3 * HEIGHT // 5:
                    note_no = note_start
                    vel = 128 * mY * 5 // (3 * HEIGHT)
                    midiout.note_off(note_no, vel)
                    index = key
                else:
                    x = key * KEY_WIDTH - KEY_WIDTH // 3
                    if x < mX and mX < x + 2 * KEY_WIDTH // 3 and mY < 3 * HEIGHT // 5:
                        note_no = note_start + val - 2
                        vel = 128 * mY * 5 // (3 * HEIGHT)
                        midiout.note_off(note_no, vel)
                        index = key
    if index == -1:
        val = 0
        for key in range(keys):
            if BLACK_KEY[key]:
                val += 2
            else:
                val += 1
            x = key * KEY_WIDTH
            if x < mX and mX < x + KEY_WIDTH:
                note_no = note_start + val - 1
                vel = 128 * mY // HEIGHT
                midiout.note_off(note_no, vel)
                index = key
    if index == -1:
        return


def SetInstrument():
    a = int(content.get())
    midiout.set_instrument(a)


def EndMidi():
    pygame.midi.quit()

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<ButtonPress-1>", ButtonPress)
canvas.bind("<ButtonRelease-1>", ButtonRelease)
button = Button(root, text='INSTRUMENT SET',
                command=SetInstrument).pack(side=LEFT)
content = StringVar()
entry = Entry(root, textvariable=content).pack(side=LEFT)
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill='blue')
for key in range(keys):
    x = key * KEY_WIDTH
    canvas.create_rectangle(x + 1, 0, x + KEY_WIDTH - 1, HEIGHT, fill='white')
for key, b in enumerate(BLACK_KEY):
    if b:
        if key == 0:
            x = key * KEY_WIDTH
            canvas.create_rectangle(
                x, 0, x + KEY_WIDTH // 3 - 1, 3 * HEIGHT // 5, fill='black')
        else:
            x = key * KEY_WIDTH - KEY_WIDTH // 3
            canvas.create_rectangle(
                x + 1, 0, x + 2 * KEY_WIDTH // 3 - 1, 3 * HEIGHT // 5, fill='black')
content.set(0)
button = Button(root, text='END MIDI', command=EndMidi).pack(side=LEFT)

root.mainloop()
