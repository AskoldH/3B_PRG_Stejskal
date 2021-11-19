# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011

@author: Radek
"""
"""
continue - přeruší aktuální iteraci, cyklus 
           pokračuje další iterací
break - přeruší vykonávání cyklu
"""           

#co bude dělat tento cyklus a kdy skončí?
"""
import random
x=1
while x!=10:
    x=random.randint(2,10)
    if x%2==0:
        continue
    print (x)
    if x==5:
        break


"""
"""
while True:
    heslo=input("Zadej vánoční kód:")
    if heslo=="jedle":
        break
    print("Špatný kód, zadej znovu.")

print("Spávný kód! Veselé Vánoce!")
"""

""" 
Úkol:
0) Pomocí cyklu načítejte 5 čísel. Když bude zadáno záporné
   číslo, použijte break. 
1) Načtěte číslo a spočítejte je ciferný součet.
2) Naprogramujte hru myslím si číslo.
   Rozšíření: Vypsat počet pokusů.
"""

pocet=0
while pocet<5:
    cislo=int(input("Zadej kladné číslo:"))
    if cislo<0:
        break
    pocet+=1












