# -*- coding: utf-8 -*-

from numpy import random

class PasswdGen(object):
    
    def __init__(self,mode=""):
        if "HIGH" == mode:
            self.c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*)(][;:~^=&%%$#!>?<'
        elif "MID" == mode:
            self.c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        elif "LOW" == mode:
            self.c = '0123456789'
        else:
            self.c = 'abcdefghijklmnopqrstuvwxyz0123456789'
    
    def Generator(self, leng=8, num=1):
        getNumbers = num
        lengs = leng
        cl = len(self.c)
        r = ""
        rLIST = []
        for n in range(getNumbers):
            r = ""
            for i in range(lengs):
                r += self.c[random.randint(0, cl)]
            else:
                rLIST.append(r)
        return rLIST




class HashGen(object):
    def __init__(self):
        ...
    
    def Encoder(self):
        ...
    
    def Decoder(self):
        ...
    
    def MPHFunction(self, *, string):
        #最小完全ハッシュ関数
        work = string[:]
        hash = 0
        #FactorialTable
        FACTOR = [24, 6, 2, 1, 0]
        for i in range(len(string) - 1):
            hash += work[i] * FACTOR[i];
            for j in range(1,len(string) - 1):
                if work[i] < work[j]:
                    work[j] -= 1
        return hash;
        

cl = [[1,2,3],[4,5,6],[7,8,9]]
print(cl[1][0])