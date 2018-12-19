#coding: utf-8
import wave
import struct
import numpy as np
from pylab import *
import func.sound_module as sm
import pygame
from pygame.locals import *
import sys

#正弦波
def createSineWave (A, f0, fs, length):
    """振幅A、基本周波数f0、サンプリング周波数 fs、
    長さlength秒の正弦波を作成して返す"""
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):  # nはサンプルインデックス
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# ノコギリ波
def createSawtoothWave (A, f0, fs, length):
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for k in range(1, 10):
            s += (A / k) * np.sin(2 * np.pi * k * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# 合成波
def createCombinedWave (A, freqList, fs, length):
    """freqListの正弦波を合成した波を返す"""
    data = []
    if not len(freqList):
        return b""
    amp = float(A) / len(freqList)
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for f in freqList:
            s += amp * np.sin(2 * np.pi * f * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    sm.play(data, 8000, 16)


# 矩形波
def createSquareWave (A, f0, fs, length):
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for k in range(1, 10):
            s += (A / (2*k-1)) * np.sin((2*k-1) * 2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# 三角波
def createTriangleWave (A, f0, fs, length):
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for k in range(0, 10):  # サンプルごとに10個のサイン波を重ね合わせ
            s += (-1)**k * (A / (2*k+1)**2) * np.sin((2*k+1) * 2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data

if __name__ == "__main__" :
    freqs = {
    "C4" : 262,
    "Cp4" : 277,
    "D4" : 294,
    "Dp4" : 311,
    "E4" : 330,
    "F4" : 349,
    "Fp4" : 370,
    "G4" : 392,
    "Gp4" : 415,
    "A4" : 440,
    "Ap4" : 466,
    "B4" : 494,
    "C5" : 523
    }
    freqList = [262, 294, 330, 349, 392, 440, 494, 523]  # ドレミファソラシド
    chordList = [(262, 330, 392),  # C（ドミソ）
                 (294, 370, 440),  # D（レファ#ラ）
                 (330, 415, 494),  # E（ミソ#シ）
                 (349, 440, 523),  # F（ファラド）
                 (392, 494, 587),  # G（ソシレ）
                 (440, 554, 659),  # A（ラド#ミ）
                 (494, 622, 740)]  # B（シレ#ファ#）
    datas = b''
    As = 1.0
    sample = 8000
    leng = 0.7
    # # datas += createTriangleWave(As, freq, sample, leng)
    # for f in freqList:
    #     datas += createSineWave(As, f, sample, leng)
    #     datas += createTriangleWave(As, f, sample, leng)
    #     datas += createSquareWave(As, f, sample, leng)
    #     datas += createSawtoothWave(As, f, sample, leng)
    # for f in chordList:
    #     datas += createCombinedWave(As, f, sample, leng)
    # # sm.play(datas, 8000, 16)
    # sm.save(datas, 8000, 16, "waves.wav")

    SCREEN_SIZE = (640, 480)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    framerate = 60
    clock = pygame.time.Clock()

    pygame.display.set_caption("piano")

    sysfont = pygame.font.SysFont(None, 40)
    freq = []
    while True:
        # 押されているキーをチェック
        freq = []
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_q]:
            freq.append(freqs["C4"])
        if pressed_keys[K_w]:
            freq.append(freqs["D4"])
        if pressed_keys[K_e]:
            freq.append(freqs["E4"])
        if pressed_keys[K_r]:
            freq.append(freqs["F4"])
        if pressed_keys[K_t]:
            freq.append(freqs["G4"])
        if pressed_keys[K_y]:
            freq.append(freqs["A4"])
        if pressed_keys[K_u]:
            freq.append(freqs["B4"])
        if pressed_keys[K_i]:
            freq.append(freqs["C5"])
        createCombinedWave(As, freq, sample, leng)
        font = sysfont.render("".join(str(freq)), True, (0, 0, 0))
        screen.fill((255,255,255))
        screen.blit(font, (20,100))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT: sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key == K_ESCAPE:
                    sys.exit()
        clock.tick(framerate)