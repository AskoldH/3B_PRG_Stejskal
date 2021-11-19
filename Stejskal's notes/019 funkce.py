# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:24:04 2011

@author: Radek
"""
"""
Vyhody podprogramů:
    1) Přehlednost
    2) Opakované použití - ušetříme psaní
    
Syntaxe:
def Název (parametr1,parametr2,...):
    blok příkazů
    return výsledný výraz

Pozn. Pokud neuvedeme return, vrací se vždy None    

Počet parametrů:
    a) žádné            def Fce()
    b) konkrétní počet  def Fce(x,y,z)
    c) proměnlivý počet def Fce(x,*param)

Implicitní hodnoty parametrů:
    V definici funkce může být do parametru 
    předána implicitní hodnota, která se použije
    v případě, že tento parametr nebude dosazen.
   !Všechny parametry vpravo od něj, musí být také
    implicitní.
"""    

#sez=[]
#print(sez.sort())


def Pozdrav():
    print ("Good morning!")

#Pozdrav()




def Pozdravy(pocet):
    for i in range(pocet):
        print ("Buenos dias!")

#Pozdravy(8)




def SuperPozdrav(pocet,text):
    for i in range(pocet):
        print (text)

#SuperPozdrav(5,'Guten Tag!')
#SuperPozdrav(4,"Wan shang chao")




def Mocnina():
    vstup=int(input("Zadej číslo pro umocnění:"))
    vys=vstup**2
    na3=vstup**3
    
    return (vys,na3)
#    print("Ahoj") #toto se ignoruje


#vysledek=Mocnina()
#print(vysledek)



"""
Úkol:
1) Napište podprogram AnaX(A,X), která bude mít dva parametry
   A a X a bude počítat a vypisovat hodnotu A na Xtou.
2) Napište podprogram Linear(a,b), která vypíše řešení lineární
   rovnice (ax+b=0). Má dva parametry a,b.     
3) Napište funkci Prumer, která vrátí (return) aritmetický
   průměr ze tří čísel.
4) Napište fci Kostka(), která vrátí hodnotu hodu kostkou.
5) Napište funkci VratSeznam(pocet, od, do), která vrátí
   seznam náh. čísel o daném počtu a rozsahu
6) Vytvořte fci ZasifrujText(text), která vrátí zašifrovaný
   text tak, že mezi jeho písmena vloží náhodná písmena navíc.
"""
import random

def VratSeznam(pocet, od, do):
    sez=[]
    for i in range(pocet):
        sez.append(random.randint(od,do))
    return sez    

print(VratSeznam(5,50,150))
        

def ZasifrujText(text):
    vysl=""
    abeceda="qwertzuiopasdfghjklyxcvbnm"
    
    for i in text:
        vysl+= i + random.choice(abeceda)    
       #vysl+= i + abeceda[random.randint(0,len(abeceda)-1)]    
    return vysl 

print(ZasifrujText("Velikonoce"))


"""
def PokusSParametry1(x,*par):
    print (x)
    print (par)
    print (par[0])


PokusSParametry1(1000,"jeden","dva","tri")
"""


"""
def PokusSParametry2(x=2,y,z):
    print (x)
    print (y)
    print (z)

PokusSParametry2(12,10)
"""


