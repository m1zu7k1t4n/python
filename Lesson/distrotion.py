# coding:utf-8
import wave
import pyaudio
import struct
from pylab import *
import sound_module as sm

def distortion(data, gain, level):
    length = len(data)
    newdata = [0.0] * length
    for n in range(length):
        newdata[n] = data[n] * gain  # 増幅
        # クリッピング
        if newdata[n] > 1.0:
            newdata[n] = 1.0
        elif newdata[n] < -1.0:
            newdata[n] = -1.0
        # 音量を調整
        newdata[n] *= level
    return newdata

if __name__ == "__main__":
    # 音声をロード
    wf = wave.open("waves.wav")
    fs = wf.getframerate()
    length = wf.getnframes()
    data = wf.readframes(length)

    # エフェクトをかけやすいようにバイナリデータを[-1, +1]に正規化
    data = frombuffer(data, dtype="int16") / 32768.0

    # ここでサウンドエフェクト
    newdata = distortion(data, 200, 0.3)

    # 正規化前のバイナリデータに戻す
    newdata = [int(x * 32767.0) for x in newdata]
    newdata = struct.pack("h" * len(newdata), *newdata)

    # サウンドエフェクトをかけた音声を再生
    sm.play(newdata, fs, 16)
    # sm.save(newdata, fs, 16, "distortion.wav")