#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:33:38 2020

@author: gokhansilahtaroglu
"""
print('merhaba dünya')
a = 2
print(a)
print(a * a)
print('****')

#donguler   WHILE
sayac = 1
while sayac <=5:
    print(sayac)
    sayac = sayac +1
    
# for dongusu
    
for sayac2 in 1,2,77,4,5:
    print(sayac2)
    
for i in range(0,7):
    print(i)

#range(baslangic,bitis,adim)

for n in range(21,0,-3):
    print(n,end = ';')
    
    
toplam = 0   
for k in range(100):
    toplam = toplam + k
print(toplam)



#listeler 

liste1 = [2,-3,0,4,-1]
liste2 = [24.2,4,'kelime',print, 19,-0.03, 'son']
print(liste1)
print(liste2)


#liste icinde gezme
for eleman in liste2:
    print(eleman)
for eleman in liste1:
    print(eleman + 5)
for eleman in reversed(liste1):
    print(eleman)
    
    
#listeyi csv dosyasına yazmak
liste1 = [2,-3,0,4,-1]
with open('deneme_dosyasi.csv','w') as dosi:
    for sayi in liste1:
        dosi.write('%s,' %sayi)
        
#iki boyutlu diziler veya matrisler

matris1 = [[100,14,8,22,71],[0,243,68,1,30],
           [90,21,7,67,112],[115,299,70,150,8]]
print(matris1)

with open('bizim_matris.xls','w') as f:
    for i in matris1:
        f.write('%s\n' %i)

        

