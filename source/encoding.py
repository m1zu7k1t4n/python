# coding: utf-8

import codecs

strings = "nittc-dmcc"


def encodes(string):
    strings = string
    # strings = strings.encode("ascii")
    for _ in range(1):
        strings = codecs.encode(strings, encoding="rot13")
    return strings


def decodes(string):
    strings = string
    for _ in range(1):
        strings = codecs.decode(strings, encoding="rot13")
    # strings = strings.decode("ascii")
    return strings


data = encodes(strings)
print(data)
data = decodes(strings)
print(data)
