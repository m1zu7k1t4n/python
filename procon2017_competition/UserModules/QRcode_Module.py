# coding: utf-8

import qrcode
from PIL import Image
import zbarlight


def scan(*paths):
    """
    :param path: file path 
    :return: 
    """
    codes = []
    for path in paths:
        with open(path, 'rb') as image_file:
            image = Image.open(image_file)
            image.load()
        try:
            codes.append(zbarlight.scan_codes('qrcode', image)[0])
        except:
            print("{0} : QRcode Not Found".format(path))
            codes.append(b'Not')
    result = [var.decode() for var in codes]
    return result


def make(data, savename="QRCode.png"):
    """
    :param data: input_data 
    :param savename: savename
    :return: Not return
    """
    img = qrcode.make(data)
    img.save(savename)

