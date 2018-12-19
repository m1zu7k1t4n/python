# -*- encoding: utf-8 -*-
import win32gui
import win32con
import time
import os


class VoiceRoidError(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return str(self.reason)


class VoiceRoid(object):
    def __init__(self):
        self.name = "VOICEROID＋ 結月ゆかり EX"
        self.parentHwnd = win32gui.FindWindow(None, self.name)
        if self.parentHwnd == 0:
            print("ゆかりさん起動中・・・")
        while self.parentHwnd == 0:
            os.system('start "" "C:\Program Files (x86)\AHS\VOICEROID+\YukariEX\VOICEROID.exe"')
            time.sleep(3)
            self.parentHwnd = win32gui.FindWindow(None, self.name)
        self.play = self.getHandle(text="再生")[0]
        self.textbox = self.getHandle(name="WindowsForms10.RichEdit20W")[0]

    def getHandle(self, **args):
        result = []

        def enumwindows(hwnd, args):
            if not args.get("text", None) is None:
                if args["text"] in win32gui.GetWindowText(hwnd):
                    result.append(hwnd)
            elif not args.get("name") is None:
                if args["name"] in win32gui.GetClassName(hwnd):
                    result.append(hwnd)

        win32gui.EnumChildWindows(
            self.parentHwnd,
            enumwindows,
            args
        )
        return result

    def sendText(self, hwnd, text):
        win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)

    def say(self, text):
        while True:
            time.sleep(0.15)
            if len(self.getHandle(text="一時停止")) < 1:
                break
        self.sendText(self.textbox, text)

        win32gui.SendMessage(self.play, win32con.BM_CLICK, 0, 0)

if __name__ == "__main__":
    import sys
    args = sys.argv
    print(args)

    if 1 < len(args):
        voiceroid = VoiceRoid()
        text = args[1]
        voiceroid.say(text)

