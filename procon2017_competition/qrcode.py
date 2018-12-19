# coding: utf-8

from UserModules.QRcode_Module import *
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()

    # 画面に表示する
    cv2.imshow('frame', frame)

    # キーボード入力待ち
    key = cv2.waitKey(1) & 0xFF

    # qが押された場合は終了する
    if key == ord('q'):
        break
    # sが押された場合は保存する
    if key == ord('s'):
        path = "qr.jpg"
        cv2.imwrite(path, frame)
        strings = scan(path)
        print(strings)
        # if strings == "Not":
        #     with open("forme.csv", "w") as forme:
        #         result = strings
        #         result = result[0].split(":")
        #         with open("forme.csv") as f:
        #             f.write(result[0])
        #             for var in result[1:]:
        #                 sp = var.split(" ")
        #                 for i in sp[:-1]:
        #                     f.write(i)
        #                     f.write(",")
        #                 f.write(i[-1:-2] + "\n")


# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
