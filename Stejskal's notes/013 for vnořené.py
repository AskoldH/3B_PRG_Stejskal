3# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:36:08 2013

@author: Radek
"""

"""
Vnořené cykly
"""

"""
pocet=int(input("Zadej delku strany:"))
for y in range(pocet):
    for x in range(pocet):
        print("* ",end="")
    print() 
"""


#Napsat kód pro čtverec.

      
"""
Úkol:
1) Vytvořte cyklus, který vypíše 6x dnešní datum.
   Celý cyklus zopakujte druhým cyklem 8x. 
    
2) Napište program, který 5x pod sebou vytiskne vaše 
   jméno (cyklem).
   Celý program zopakujte 30x (cyklem), vždy po 5-ti jménech
   vložte prázdný řádek.
   Napište před každé jméno jeho celkové pořadové číslo.
    
3) Vytvořte následující výpis pro libovolné n (toto bylo 4):
   1 : 1
   2 : 12 
   3 : 123
   4 : 1234

4) Načtěte n, vygenerujte n náhodných čísel a vypište
   ke každému z nich všechny jeho dělitele.
   Př: n=3
   4: 1 2 4
   18: 1 2 3 6 9 18
   11: 1 11
5) Vypište pyramidu z hvězdiček o výšce n.
   Př: n=4
      *
     ***
    *****
   ******* 
6) Zkuste vytisknout šachovnici 8x8 (nxn) ze dvou zvolených znaků:
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @s . @ .
7) Máme řetězec "abcdefghijklmnopqrstuvwxyz". Načtěte z
   klávesnice počet hesel a vygenerujte z počátečního
   řetězce daný počet náhodných hesel délky 7 znaků.
"""

n=int(input("Zadej výšku pyramidy:"))
mezery=n-1
hvezdy=1

for i in range(n):
    for m in range(mezery):
        print(" ",end="")
    for h in range(hvezdy):
        print("*",end="")
    mezery=mezery-1
    hvezdy=hvezdy+2
    print()








