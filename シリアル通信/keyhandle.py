import msvcrt
import time


while True:
    time.sleep(0.01)
    if msvcrt.kbhit():
        kb = msvcrt.getch()
        print(kb)
