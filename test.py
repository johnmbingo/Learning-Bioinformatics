import random

from PersonalDNAtoolkit import *


def practicingcountingnuc(s):
    tmpnucdict = {}
    for nuc in list(s):
        if nuc in tmpnucdict:
            tmpnucdict[nuc] += 1
        else:
            tmpnucdict[nuc] = 1
    return tmpnucdict

#You can also use counter(list(s))

print(practicingcountingnuc(randomDNAstring))
print(randomDNAstring)


    
    

