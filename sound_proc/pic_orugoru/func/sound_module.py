# coding: utf-8


def filename():
    import tkinter.filedialog as fd
    Dir = "C:"
    Type = [('音楽ファイル','*.wav')]
    filepath = fd.askopenfilename(filetypes=Type, initialdir=Dir)
    return filepath

# 正弦波
def sin(A, f0, fs, length):
    import struct
    import numpy as np
    """振幅A、基本周波数f0、サンプリング周波数 fs、
    長さlength秒の正弦波を作成して返す"""
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:
            s = 1.0
        if s < -1.0:
            s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# ノコギリ波
def saw(A, f0, fs, length):
    import struct
    import numpy as np
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for k in range(1, 10):
            s += (A / k) * np.sin(2 * np.pi * k * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:
            s = 1.0
        if s < -1.0:
            s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# 合成波
def combine(A, freqList, fs, length):
    import struct
    import numpy as np
    """freqListの正弦波を合成した波を返す"""
    data = []
    amp = float(A) / len(freqList)
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for f in freqList:
            s += amp * np.sin(2 * np.pi * f * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:
            s = 1.0
        if s < -1.0:
            s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# 矩形波
def square(A, f0, fs, length):
    import struct
    import numpy as np
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for k in range(1, 10):
            s += (A / (2 * k - 1)) * \
                np.sin((2 * k - 1) * 2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:
            s = 1.0
        if s < -1.0:
            s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


# 三角波
def triangle(A, f0, fs, length):
    import struct
    import numpy as np
    data = []
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for k in range(0, 10):  # サンプルごとに10個のサイン波を重ね合わせ
            s += (-1)**k * (A / (2 * k + 1)**2) * \
                np.sin((2 * k + 1) * 2 * np.pi * f0 * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:
            s = 1.0
        if s < -1.0:
            s = -1.0
        data.append(s)
    # [-32768, 32767]の整数値に変換
    data = [int(x * 32767.0) for x in data]
    # バイナリに変換
    data = struct.pack("h" * len(data), *data)  # listに*をつけると引数展開される
    return data


def save(data, sampling, bit, filename):
    """
    波形データをWAVEファイルへ出力
    data:bytes, sampling:sampling rate, bit: normal is 16bit, filename:Using name
    """
    import wave
    import pyaudio
    p = pyaudio.PyAudio()
    with wave.open(filename, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sampling)
        wf.writeframes(data)


def play(data, sampling, bit):
    """
    波形データを再生
    data: bytes, sampling: sampling rate, bit: normal is 16bit
    """
    import pyaudio
    import wave
    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=int(sampling),
                    output=True)
    # チャンク単位でストリームに出力し音声を再生
    chunk = 1024
    sp = 0  # 再生位置ポインタ
    buffer = data[sp:sp + chunk]
    while buffer != b'':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp + chunk]
    stream.close()
    p.terminate()


import struct
import numpy as np
