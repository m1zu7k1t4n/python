# coding: utf-8

def is_percent_check(arrayset,percent):


def soso_sort(arrayset, percent, tuple_address=0):
    '''

    :param arrayset: list or tuple or ndarray
    :param percent: int
    :return: list
    '''

    if type(arrayset[0]) == (tuple or list):
        sorted_key = lambda x: x[tuple_address]
    else:
        sorted_key = None

    if percent == 100:
        return sorted(arrayset, key=sorted_key)
    elif percent == 0:
        return arrayset

    if percent == 20