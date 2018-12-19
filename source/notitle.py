# coding: utf-8


def matching(keyword, piece):
    piece_length = len(piece)
    for key_length range(len(keyword)):
        not_flag = True
        for k, p in zip(keyword[key_length:key_length + piece_length], piece):
            if not (p == k or p == "?"):
                not_flag = False
                break


                # return "UNRESTORABLE"
                # return keyword[0:key_length] + piece + keyword[key_length+piece_length:len(keyword)]


S_d = input()
T = input()

print(matching(S_d, T))
