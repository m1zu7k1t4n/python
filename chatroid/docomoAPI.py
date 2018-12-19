import requests
import json
import sys

class chat:
    def __init__(self):
        self.APIKEY = "676864354f46374d66684e657071513855486541682e6d50394d546e537955486e6c3038366c546c326844"
        self.zatsudan_url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY={}".format(self.APIKEY)
        self.payload = {
            "utt": "",
            "context": "",
            "nickname": "あらさん",
            "nickname_y": "アラサン",
            "sex": "男",
            "bloodtype": "O",
            "birthdateY": "1999",
            "birthdateM": "7",
            "birthdateD": "29",
            "age": "17",
            "constellations": "獅子座",
            "place": "富山",
            "mode": "dialog",
            "t": "20",
        }

    def zatsudan_request(self, serif):
        self.payload["utt"] = serif
        r = requests.post(self.zatsudan_url, data=json.dumps(self.payload))
        self.payload["context"] = r.json()['context']
        self.payload["mode"] = r.json()['mode']
        sys.stdout.write("yukari : ")
        print(r.json()['utt'])
        return r.json()['utt']
