#coding:utf-8
import wave
from numpy import *
from pylab import *
import func.sound_module as sm

def printWaveInfo(wf):
    """WAVEファイルの情報を取得"""
    print("チャンネル数: %d", wf.getnchannels())
    print("サンプル幅: %d", wf.getsampwidth())
    print("サンプリング周波数: %5.2f", wf.getframerate())
    print("フレーム数: %d", wf.getnframes())
    print("パラメータ: %s", wf.getparams())
    print("長さ（秒）: %5.2f", float(wf.getnframes()) / wf.getframerate())

if __name__ == '__main__':
    filename = sm.filename()
    wf = wave.open(filename, "r")
    printWaveInfo(wf)

    buffer = wf.readframes(wf.getnframes())
    print(len(buffer))  # バイト数 = 1フレーム2バイト x フレーム数

    # bufferはバイナリなので2バイトずつ整数（-32768から32767）にまとめる
    data = frombuffer(buffer, dtype="int16")

    # プロット
    plot(data[0:100])
    show()