import wave
import numpy as np
import struct
from math import pow

a = 1  # 振幅
fs = 8000  # サンプリング周波数
f0 = 247  # 周波数
sec = 3  # 秒

freq = {
    "C4":261,
    "D4":293,
    "E4":329,
    "F4":349,
    "G4":392,
    "A4":440,
    "B4":494,
    "C5":523,
}



swav = []
m = np.random.choice(list(freq.keys()))
mtemp = m
for n in np.arange(fs * sec):
    # サイン波を生成
    # if not n % 3500:
    #     while(m == mtemp):
    #         m = np.random.choice(list(freq.keys()))
    #     mtemp = m
    #     print(m)
    s = a * np.sin(2.0 * np.pi * freq["E4"] * n / fs)
    swav.append(s)
# サイン波を-32768から32767の整数値に変換(signed 16bit pcmへ)
swav = [int(x * 32767.0) for x in swav]

# バイナリ化
binwave = struct.pack("h" * len(swav), *swav)

# サイン波をwavファイルとして書き出し
w = wave.Wave_write("output.wav")
p = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(binwave)
w.close()
