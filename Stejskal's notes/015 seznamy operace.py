# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 @author: Radek
"""
"""
        Seznamy a jejich operace
append(hodnota)       - přidá hodnotu na konec seznamu
count(hodnota)        - zjistí počet výskytů dané hodnoty
insert(index, hodnota)- vloží hodnotu na pozici v seznamu
pop(index)            - odebere prvek z dané pozice
remove(hodnota)       - odebere první výskyt této hodnoty
sort()                - setřídí seznam podle velikosti

delka=len(seznam)     - zjištění velikosti seznamu
""" 

"""
seznam=[100,2012,1000,3,1,500,17]
seznam=seznam+[2012]
seznam.append(2012) 
print (seznam)


print ("Pocet 2012: ",seznam.count(2012))


seznam.insert(0,"Vlozeno") #vloží hod. na začátek
print (seznam)


#Pokud neuvedeme index, odebírá z konce seznamu
x=seznam.pop(0) #Odebere prvek z pozice 0
print (x)
print (seznam)


seznam.remove(2012) #Odebere první výskyt
print (seznam)


seznam.sort()
print (seznam)


ret=["beta","c","a","alfa"]
ret.sort()
print(ret)


print (u"Seznam má",len(seznam),u"prvků.")
"""

"""
Úkol:
1) Napište cyklus, který bude načítat z klávesnice 5 
   čísel a postupně je bude dávat na konec prázdného 
   seznamu. Seznam nakonec vypište.
2) Vygenerujte a vypište seznam 20-ti náhodných čísel.
3) Vygenerujte seznam 20-ti náh. čísel od 1 do 10,
   seznam setřiďte a vytvořte k němu seznam druhých
   mocnin. Oba seznamy vypište.
4) Zjistěte, kolikrát se v mocninách vyskytuje 81.
   Odstraňte všechna čísla 81 ze seznamu mocnin. 
5) Uložte do seznamu 6 náhodných hodů kostkou a zjistěte,
   jestli padla postupka tj. všechny hodnoty od 1 do 6.
6) Do seznamu "karty" vložte názvy karet. Vytvořte seznam
   "balicek" a vložte do něj zamíchané názvy karet.
   Help: karty=["♥7","♦7","♣7","♠7", ...]
7) Napište simuaci sportky. Člověk zadá 6 čísel, poté 
   počítač vylosuje také 6 čísel a vypíše, kolik čísel
   jsme uhádli. Čísla  musí být z intervalu 1-49. Čísla
   se nesmí opakovat.
"""

import random
tiket=[]
while len(tiket)<6:
    cislo=int(input("Zadej číslo do tiketu:"))
    if cislo<1 or cislo>49:
        print("Číslo mimo rozsah!")
    elif cislo not in tiket:
        tiket.append(cislo)
    else:
        print("Číslo uz je vsazeno!")

tiket.sort()
print(tiket)


print("Váš tiket:",tiket)

losovani=[]
while len(losovani)<6:
    cislo=random.randint(1,49)
    if cislo not in losovani:
        losovani.append(cislo)
losovani.sort()
print("Losovaná čísla:",losovani)


        
uhodnuto=[]
for i in tiket:
    if i in losovani:
        uhodnuto.append(i)

print("Uhodnutá čísla:",uhodnuto)        








"""
DU) 
1) Naprogramujte jakoukoli hru s kostkami pro alespoň dva 
   hráče, jeden z nich bude počítač. 
2) Hra musí být dostatečně složitá a pro pro uchování hodů 
   bude používat seznamy. Příliš jednoduché hry budou vráceny
   k přepracování.
3) Musí být zobrazena pravidla.
4) Hra po spuštění zobrazí jednoduché textové menu:
   
   1) Zobraz pravidla
   2) Hrát hru
   3) Konec
   Zadej svou volbu:
       
   Po ukončení hry se program vrací do menu, nedojde k ukončení
   aplikace!
5) Hody hráčů (člověka i počítače) musí proběhnout až po stisku 
   klávesy Enter! 
   Použijte tento příkaz, který v podstatě způsobí čekání programu, 
   dokud uživatel nestiskne Enter: input("Stiskni Enter...").
   Snažte se o přehledné výpisy stavu hry - např. průběžné body
   za kolo a také celkové od začátku hry.
6) Každý musí mít jinou hru! :)   
""" 
