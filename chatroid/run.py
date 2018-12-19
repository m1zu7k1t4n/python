from docomoAPI import chat
from yukari import VoiceRoid
import sys

d = chat()
yukari = VoiceRoid()
print("チャットの準備が出来たみたい！")
while True:
    sys.stdout.write("you : ")
    text = input()
    if text == "":
        text = "ばいばーい"
        print("")
        text = d.zatsudan_request(text)
        yukari.say(text)
        break
    text = d.zatsudan_request(text)
    yukari.say(text)
