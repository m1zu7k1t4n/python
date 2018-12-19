#coding: utf-8
import wavech
import struct
import numpy as np
from pylab import *
from func.sound_module import *

if __name__ == "__main__":
    import pandas as pd
    from tqdm import tqdm
    freqdict = {
        "si0":247,
        "do":262,
        "do#":277,
        "re":293,
        "re#":311,
        "mi":330,
        "fa":350,
        "fa#":370,
        "so":392,
        "so#":415,
        "ra":440,
        "si":494,
        "do2":523,
        "do2#":555,
        "mi2":660,
        "mu":0,
    }
    allData = b''
    df = pd.read_csv('gakuhu.txt')
    for l,i in tqdm(zip(df['length'],df['interval']),total=len(df['length'])):
        data = sin(0.5, freqdict[i], 8000.0, 0.25*l)
        allData += data
    save(allData,8000,16,"picsound_sin.wav")
