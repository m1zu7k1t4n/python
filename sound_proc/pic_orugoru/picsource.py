import pandas as pd

bpm = 120

tonedict = {
    "do":261.6,
    "do#":277.2,
    "re":293.7,
    "re#":311.1,
    "mi":329.6,
    "fa":349.2,
    "fa#":370.0,
    "so":392.0,
    "so#":415.3,
    "ra":440.0,
    "ra#":466.2,
    "si":493.9,
	"mu":0.0
}

# {0}:音程の名前 {1}:音の波長の長さ {2}:音のサイクル数
overtone = """
{0}
	MOVWF	LEN
	INCF	LEN, F
{0}_LEN
	MOVLW	D'{1}'
	MOVWF	CNT2
LOOP_{0}
	BCF	PORTB, 0
	MOVLW	D'{2}'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'{2}'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_{0}
	DECFSZ	LEN,	F
	GOTO	{0}_LEN
	MOVLW	D'0'
	RETURN
"""

# {0}:実際の楽譜領域　{1}:音程の設定領域 {2}:無音の長さ設定領域　60[s]/(bpm*2)が設定値として入る予定
rowstring = """	LIST	P=PIC16F84A
	INCLUDE	"P16F84A.INC"

	__CONFIG _HS_OSC & _WDT_OFF

CNT1	EQU	0CH
CNT2	EQU	0DH
CNT3	EQU	0EH
CNT4	EQU	0FH
CNT5	EQU	10H
LEN	EQU	12H
MU_M	EQU	13H

	ORG	0H
MAIN
	BSF	STATUS,	RP0
	CLRF	TRISA
	CLRF	TRISB
	BCF	STATUS,	RP0
	BCF	STATUS,	C
	CLRF	PORTB
	MOVLW	D'0'
MAINLP
{0}
	GOTO	MAINLP

{1}
MU
	MOVWF	LEN
	INCF	LEN, F
MU_LEN
	MOVLW	D'{2}'
	MOVWF	MU_M
MU_LOOP
	CALL	TIME10M
	DECFSZ	MU_M,	F
	GOTO	MU_LOOP
	DECFSZ	LEN,	F
	GOTO	MU_LEN
	MOVLW	D'0'
	RETURN

BASETIME
	MOVWF	CNT1
L3
	CALL	TIME10U
	DECFSZ	CNT1,F
	GOTO	L3

	MOVLW	D'{3}'
	MOVWF	CNT1
L4
	CALL	TIME10U
	DECFSZ	CNT1,F
	GOTO	L4
	RETURN

TIME10U
	MOVLW	0x0F
	MOVWF	CNT3
	NOP
	NOP
LOOP1
	DECFSZ	CNT3,	F
	GOTO	LOOP1
	RETURN

TIME100U
	MOVLW	0xA5
	MOVWF	CNT4
	NOP
	NOP
LOOP2
	DECFSZ	CNT4,	F
	GOTO	LOOP2
	MOVLW	D'0'
	RETURN

TIME10M
	MOVLW	0x63
	MOVWF	CNT5
	NOP
	NOP
LOOP3
	CALL	TIME100U
	DECFSZ	CNT5,	F
	GOTO	LOOP3
	RETURN			;2

	END"""

df = pd.read_csv("gakuhu.csv")
gakuhu = ''
allovertone = ''
prev_interval = ''

for i,v in zip(df['length'],df['interval']):
	# 楽譜作成領域
	if prev_interval == v:
		gakuhu += "\tCALL\tTIME100U\n"
	prev_interval = v
	if v == "mu":
		gakuhu += "\tMOVLW\tD'{}'\n".format(int(i) - 1)
		gakuhu += "\tCALL\t{}\n".format(v.upper())
		continue
	if i != 1:
		gakuhu += "\tMOVLW\tD'{}'\n".format(int(i)-1)
	gakuhu +="\tCALL\t{}\n".format("O" + v.upper())

mostmax = -999
mostmin = 999
geta = 0
for v in set(df['interval']) - set(["mu"]):
	cycle = ((1 / (tonedict[v[:-1]] * 2 ** (int(v[-1]) - 4))) * 100000) / 2
	mostmax = max(mostmax,cycle)
	mostmin = min(mostmin,cycle)
geta = int(mostmax - mostmin)
assert geta <= 255, str(geta) + "で255より波数を畳み込めるサイズより大きいです"
mostmin = int(mostmin)
mostmin -= 1
for v in set(df['interval']) - set(["mu"]):
	# 音程作成領域
	cycle = ((1 / (tonedict[v[:-1]] * 2 ** (int(v[-1]) - 4))) * 100000) / 2 # サイクル数
	waves = (tonedict[v[:-1]] * 2 ** (int(v[-1]) - 4) * ((60)/(bpm*2)))
	assert (int(cycle) - mostmin) <= 255 and int(waves) <= 255, str(int(cycle)) + " : " + str(int(waves)) + " でcycleか波数が255より波数を畳み込めるサイズより大きいです"
	allovertone += overtone.format("O" + v.upper(),int(waves),int(cycle) - mostmin)

with open("picsource.asm", "w") as f:
	f.write(rowstring.format(gakuhu,allovertone,int((60*100)/(2*bpm)),mostmin))
