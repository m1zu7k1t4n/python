#coding: utf-8
import func.sound_module as sm

if __name__ == "__main__" :
    # 音のリスト　平均十二階律を取るため音は2の12乗根 1.05946 を計算に用いる
    freqList = [262, 294, 330, 349, 392, 440, 494, 523]  # ドレミファソラシド
    chordList = [(262, 330, 392),  # C（ドミソ）
                 (294, 370, 440),  # D（レファ#ラ）
                 (330, 415, 494),  # E（ミソ#シ）
                 (349, 440, 523),  # F（ファラド）
                 (392, 494, 587),  # G（ソシレ）
                 (440, 554, 659),  # A（ラド#ミ）
                 (494, 622, 740)]  # B（シレ#ファ#）
    # 初期化項目
    datas = b''
    As = 1.0 #振幅
    sample = 8000 #サンプリングレート
    leng = 0.55 #音の長さ

    for f in freqList:
        datas += sm.sin(As, f, sample, leng)
    #     datas += sm.triangle(As, f, sample, leng)
    #     datas += sm.square(As, f, sample, leng)
    #     datas += sm.saw(As, f, sample, leng)
    # for f in chordList:
    #     datas += sm.combine(As, f, sample, leng)
    # sm.play(datas, 8000, 16,)
    sm.save(datas, 8000, 16, "waves.wav")