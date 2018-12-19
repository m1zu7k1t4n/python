#coding: utf-8
import wave
import struct
import numpy as np
from pylab import *
import sound_module as sm


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
    return data


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
    freqList = [262, 294, 330, 349, 392, 440, 494, 523]  # ドレミファソラシド
    chordList = [(262, 330, 392),  # C（ドミソ）
                 (294, 370, 440),  # D（レファ#ラ）
                 (330, 415, 494),  # E（ミソ#シ）
                 (349, 440, 523),  # F（ファラド）
                 (392, 494, 587),  # G（ソシレ）
                 (440, 554, 659),  # A（ラド#ミ）
                 (494, 622, 740)]  # B（シレ#ファ#）
    freq = 262
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
    for f in chordList:
        datas += createCombinedWave(As, f, sample, leng)
    sm.play(datas, 8000, 16,)
    # sm.save(datas, 8000, 16, "waves.wav")