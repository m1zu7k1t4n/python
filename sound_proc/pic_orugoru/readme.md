# 使い方
## ファイル構成
- gakuhu.csv
- picsound.py
- picsource.py

gakuhuは１列目に８部音符を基準とした長さ
ex) 2 equal 4分音符
    4 equal 2分音符
    8 equal 全音符
2列目に音程(あまり極端な音域を取ることはできない)
ex) do4 equal 4度のド
    re#3 equal 3度のレ#

## 実行させるための必要事項
```shell
pip install -r requirements.txt
```

## 実行方法

楽譜をcsvに書き起こしたものをソースコード化するには
```shell
python picsource.py
```
とすればよい。**picsource.asm**が生成される。
BPMを合わせたい場合はpicsource.pyの中のbpmの変数を曲のBPMに書き換える。

楽譜をデバッグするためには(環境によるチェックをしていないため動かない可能性あり　デバッグして)
```shell
python picsound.py
```
とすればよい。picsound.wavが生成される。
