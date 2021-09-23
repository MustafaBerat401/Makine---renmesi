#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:03:45 2018

@author: sadievrenseker
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

#Random Selection (Rastgele Seçim)
"""
import random

N = 10000
d = 10 
toplam = 0
secilenler = []
for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    toplam = toplam + odul
    
    
plt.hist(secilenler)
plt.show()
"""

# UCB

N = 10000 # 10000 tıklama
d = 10 # toplam 10 ilan var
oduller = [0] * d # ilk başta bütün ilanların ödülü sıfır
tiklamalar = [0] * d # o ana kadar ki tıklamalar
toplam = 0 # toplam ödül
secilenler = []

for n in range(1,N):

    ad = 0 # seçilen ilan
    max_ucb = 0

    for i in range(0,d):

        if(tiklamalar[i] > 0):
            ortalama = oduller[i] / tiklamalar[i]
            delta =math.sqrt(3/2* math.log(n)/tiklamalar[i])
            ucb = ortalama + delta

        else:
            ucb = N*10

        if max_ucb < ucb: # maxtan büyük bir ucb çıktı
            max_ucb = ucb
            ad = i

    secilenler.append(ad)  
    tiklamalar[ad] = tiklamalar[ad] + 1
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul
    
print('TOPLAM ÖDÜL')
print(toplam)

plt.hist(secilenler)
plt.show()







