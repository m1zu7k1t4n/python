# -*- coding: utf-8 -*-

from secure import PasswdGen

pwg = PasswdGen("HIGH")
print(pwg.Generator(50,10))