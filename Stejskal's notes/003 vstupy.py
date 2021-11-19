# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:49:38 2017

@author: Student
"""
"""
Vstup z klávesnice
------------------
text=input("Pokyn pro uživatele") 
  - vždy získáme řetězec!!!
  - můžeme použít též pro čekání na stisk klávesy
    Enter
"""                                    

# jmeno=input("Zadej svoje jméno: ")
# print("Tvoje jméno je",jmeno+".")

# input()

# input("Pro pokračování stiskni Enter...")
# print("Nashledanou příště!")



# vstup=input("Zadej číslo: ")
# cislo=int(vstup)
# print("Dvojnásobek je",2*cislo)



# a=int(input("Zadej základ: "))
# x=int(input("Zadej exponent: "))
# mocnina=a**x
# print("Výsledek je:", mocnina)



"""
Úkol:
1) Načtěte z klávesnice číslo a
   vypište zbytek po dělení číslem 10.
2) Načtěte z kláv. délku materiálu a na jak dlouhé
   kusy má být nařezán. Zjistěte kolik kusů získáte
   a jaký bude odpad.
3) Načtěte z kláv. ujeté kilometry (počet),
   spotřebované palivo (litry) a cenu za jeden litr.
   Spočítejte náklady na cestu, spotřebu na 100 km
   a náklady na 1 km. 

   Př: Vstup:  80 km, 4 l, 30 kč
       Výstup: 120 kč, 5.0 l, 1.5 kč
"""


km = int(input("Zadej počet ujetých km: "))
litry = int(input("Zadej počet spotřebovaných litrů: "))
cena = int(input("Zadej cenu za 1 litr: "))

naklady = litry * cena
spotreba = litry / km * 100
naklady_1km = naklady / km

print("Náklady na cestu jsou", naklady)
print("Spotřeba na 10 km je", spotreba)
print("Náklady na 1 km jsou", naklady_1km)














