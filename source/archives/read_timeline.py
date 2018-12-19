# -*- coding: utf-8 -*-

"""
*注意*
フルパスを指定する際にフォルダ名などにスペースがあったりすると上手くいかなかったりします。
from http://qiita.com/MichaelAsterisk/items/7e71730ad948c11fe27d
"""

from time import sleep
import subprocess
import tweepy

"""
1.vrx.exeのフルパスを入れる
2.VOICEROIDのフルパスを入れる
3.keyを入れる
"""
PATH_VRX = r'C:\\Programs\\ReadVoiceroid\\vrx.exe'
PATH_VOICEROID = r'C:\Program Files (x86)\AHS\VOICEROID+\YukariEX\VOICEROID.exe'

CONSUMER_KEY = 'TKwqWeTjNwO7oTGhwzg1oDNhI'
CONSUMER_SECRET = 'i7en7WyWQgjgQJS0pUwP2DA9Awl3tVXqudpNghc7irCHnyEdrZ'
ACCESS_TOKEN = '2404678368-MtOPsbq6suvBmXMgBvwsA2qzVAMDarPkRwhtZVw'
ACCESS_SECRET = 'VdDcv9tL3xmgU4V0jrDGTQgMPbgWWNqwOkX0xV9P36z3J'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


cmd = "cmd /c start " + PATH_VOICEROID
subprocess.Popen(cmd)
sleep(3)  # Voiceroidの起動にかかる時間に応じて適当な数字に変えてください。ここでは3秒にしています。
cmd = r"cmd /c start " + PATH_VRX + " 。"
subprocess.Popen(cmd)


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        if status.text.find('RT @') != -1:  # RTは省いてます
            return True
        cmd = PATH_VRX + " " + status.user.name + "さんのつぶやき。" + status.text
        subprocess.Popen(cmd)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()
