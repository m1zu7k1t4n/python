	LIST	P=PIC16F84A
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
	CALL	ODO4
	CALL	ORE5
	CALL	TIME100U
	CALL	ORE5
	CALL	ODO5
	MOVLW	D'7'
	CALL	MU
	CALL	ODO4
	CALL	OSO4
	CALL	OMI4
	CALL	ORA4
	MOVLW	D'7'
	CALL	MU
	CALL	ORA4
	CALL	OMI4
	CALL	OSO4
	CALL	ODO4

	GOTO	MAINLP


OMI4
	MOVWF	LEN
	INCF	LEN, F
OMI4_LEN
	MOVLW	D'82'
	MOVWF	CNT2
LOOP_OMI4
	BCF	PORTB, 0
	MOVLW	D'67'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'67'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_OMI4
	DECFSZ	LEN,	F
	GOTO	OMI4_LEN
	MOVLW	D'0'
	RETURN

OSO4
	MOVWF	LEN
	INCF	LEN, F
OSO4_LEN
	MOVLW	D'98'
	MOVWF	CNT2
LOOP_OSO4
	BCF	PORTB, 0
	MOVLW	D'43'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'43'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_OSO4
	DECFSZ	LEN,	F
	GOTO	OSO4_LEN
	MOVLW	D'0'
	RETURN

ORA4
	MOVWF	LEN
	INCF	LEN, F
ORA4_LEN
	MOVLW	D'110'
	MOVWF	CNT2
LOOP_ORA4
	BCF	PORTB, 0
	MOVLW	D'29'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'29'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_ORA4
	DECFSZ	LEN,	F
	GOTO	ORA4_LEN
	MOVLW	D'0'
	RETURN

ODO4
	MOVWF	LEN
	INCF	LEN, F
ODO4_LEN
	MOVLW	D'65'
	MOVWF	CNT2
LOOP_ODO4
	BCF	PORTB, 0
	MOVLW	D'107'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'107'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_ODO4
	DECFSZ	LEN,	F
	GOTO	ODO4_LEN
	MOVLW	D'0'
	RETURN

ORE5
	MOVWF	LEN
	INCF	LEN, F
ORE5_LEN
	MOVLW	D'146'
	MOVWF	CNT2
LOOP_ORE5
	BCF	PORTB, 0
	MOVLW	D'1'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'1'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_ORE5
	DECFSZ	LEN,	F
	GOTO	ORE5_LEN
	MOVLW	D'0'
	RETURN

ODO5
	MOVWF	LEN
	INCF	LEN, F
ODO5_LEN
	MOVLW	D'130'
	MOVWF	CNT2
LOOP_ODO5
	BCF	PORTB, 0
	MOVLW	D'11'
	CALL	BASETIME
	BSF	PORTB, 0
	MOVLW	D'11'
	CALL	BASETIME
	DECFSZ	CNT2,F
	GOTO	LOOP_ODO5
	DECFSZ	LEN,	F
	GOTO	ODO5_LEN
	MOVLW	D'0'
	RETURN

MU
	MOVWF	LEN
	INCF	LEN, F
MU_LEN
	MOVLW	D'25'
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

	MOVLW	D'84'
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

	END