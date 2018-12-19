from serial import Serial
import re
import msvcrt
pattern = r'^.*?\n$'
repatter = re.compile(pattern)
exit_word = b"xxxxxxxx"

with Serial('COM4', 115200,timeout=0.05) as s:
    while True:
        try:
            recv = s.read(20000)
            char_fit = recv.decode('utf-8')
            print(char_fit, end='')
            if msvcrt.kbhit():
                kb = msvcrt.getch()
                exit_word += kb
                exit_word = exit_word[1:]
                if exit_word == b'exit_con':
                    break
                s.write(kb)
        except KeyboardInterrupt:
            send = b"\x03"
            s.write(send)

