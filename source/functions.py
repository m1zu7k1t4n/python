# coding: utf-8


def dakuon(strings):
    new_strings = []
    for word in strings:
        new_strings.append(word)
        new_strings.append('"')
    return "".join(new_strings)

print(dakuon("だれかかってーーーーーー"))