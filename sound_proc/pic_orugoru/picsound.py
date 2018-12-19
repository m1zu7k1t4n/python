#coding: utf-8
import wave
import struct
import numpy as np
from pylab import *
from func.sound_module import *

if __name__ == "__main__":
    import pandas as pd
    from tqdm import tqdm
    freqdict = {
        "si3":247,
        "do4":262,
        "do#4":277,
        "re4":293,
        "re#4":311,
        "mi4":330,
        "fa4":350,
        "fa#4":370,
        "so4":392,
        "so#4":415,
        "ra4":440,
        "si4":494,
        "do5":523,
        "do#5":555,
        "re5": 293*2,
        "mi5":660,
        "mu":0,
    }
    allData = b''
    df = pd.read_csv('gakuhu.csv')
    for l,i in tqdm(zip(df['length'],df['interval']),total=len(df['length'])):
        data = square(0.5, freqdict[i], 8000.0, 0.25*int(l))
        allData += data
    save(allData,8000,16,"picsound.wav")
