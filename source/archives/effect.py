import wave
import numpy as np
import struct
from math import pow

def distortion(data,amp = 5.0,level=0.7):
    out = []
    for d in data:
        d *= amp
        d = min(d,1.0)
        d = max(d,-1.0)
        out.append(d)
    return np.array(out) * level

def overdrive(data, amp = 3.0, level = 0.5):
    out = []
    for d in data:
        d = np.arctan(d) / (np.pi / 2.0)
        if d > 0:
            res = amp * d
        else:
            res = amp * d * 0.3
        res = min(res, 1.0)
        res = max(res, -1.0)
        out.append(d)
    return np.array(out) * level

a = 1  # 振幅
fs = 8000  # サンプリング周波数
f0 = 440  # 周波数
sec = 6  # 秒

swav = []

for n in np.arange(fs * sec):
    # サイン波を生成
    s = a * np.sin(2.0 * np.pi * f0 * n / fs)
    swav.append(s)
# サイン波を-32768から32767の整数値に変換(signed 16bit pcmへ)
swav = [int(x * 32767.0) for x in swav]
# バイナリ化
binwave = struct.pack("h" * len(swav), *swav)
binwave = overdrive(binwave)
# サイン波をwavファイルとして書き出し
w = wave.Wave_write("output.wav")
p = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(binwave)
w.close()
