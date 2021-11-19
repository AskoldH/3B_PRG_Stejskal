# -*- coding: utf-8 -*-
"""
Řetězce (string)
- uzavřeny v apostrofech (') nebo v uvozovkách (")
- trojí uvozovky mohou uzavírat i více řádků
"""
"""
existuje knihovna string
- mnoho užitečných proměnných a funkcí

Např:
    string.ascii_letters
    string.digits
    atd.
"""
import string


#x=u"""Víceřádkový
#pokusný
#řetězec
#"""
#print x

"""
Speciální znaky - začínají lomítkem
\' - apostrof
\" - uvozovka
\\ - lomítko
\n - nový řádek
"""

ret= "Specialni \nznaky: \' \\\\n \" "
#print ret



"""
Formátovací operátor %
- slouží ke vkládání a formátování různých
  datových typů do řetězce
Obecně:
"...%zkratka typu %f..." % (N-tice hodnot)  

Zkratky typů:
%i celé číslo
%f desetinné
%s řetězec
%x hexadecimální tvar
%o osmičkový tvar

%5.2f číslo bude složeno z 5 znaků, z toho 2
      budou za desetinnou tečkou, chybějící znaky
      budou nahrazeny mezerami zleva

%-8.2f číslo bude složeno z 8 znaků, z toho 2
      budou za desetinnou tečkou, chybějící znaky
      budou nahrazeny mezerami zprava

%4i  obdobně pro celá čísla 
%-4i
"""
import math


den=4
mesic=6
rok=2019

#ret="Dnešní datum je %2i.%2i.%i" % (den,mesic,rok)
#print (ret)

#ret="Ludolfovo číslo je %10.2f. Chapeš?" % (math.pi)
#print (ret)

#cislo=2567
#hexastring="Převedeno na hexa: %x" % (cislo)
#print(hexastring)
#
#
#barva="#%02x%02x%02x" % (12,150,255)
#print(barva)
#
#jmeno="Jmenuji se %s." % ("Petr")
#print(jmeno)


"""
Indexování
K jednotlivým částem řetezce lze přistoupit 
pomocí [].
Kladné hodnoty číslují znaky zleva, záporné zprava.      
"""

ret="patek"
#print ret[-1]

"""
Operátor : (slice)
- vrací podřetězec
[:n] - vrátí prvních n znaků
[n:] - vrátí podřetězec od pozice n do konce
[m:n] - vrátí podřetězec od pozice m do n
"""

ret="abeceda"
#print (ret[:3])
#print (ret[-5:])
#print ret[1:4]

"""
Funkce str()
- převede libovolný typ na řetězec
"""


sez=[1,3,8]
ret=str(sez)
#print ret
#print sez[0]
#print ret[0]

"""
w="Retezec %s retezec" % 'vlozeny text'
print w
"""
"""
z=65327
y="Hexadecimalni %x oktalove %o" % (z,z)
print y
"""
"""
slovnik={'cislo':1000000,'text':'nejaky text'}
v="Slovnik %(text)s" % slovnik
print v

"""
"""
Některé další řetězcové funkce
ret.split(znak,n) - vrátí seznam podřetězců, oddělovačem
                  je daný znak, automaticky je to mezera
                  - n říká, kolik odělovačů se použije
ret.replace("s1","s2") - nahradí v řetězci všechny 
                  výskyty s1 retezcem s2  

ret.upper() - vrátí řetězec převedený na velké znaky
ret.lower() - na malé znaky
"""

"""
veta="Toto je pokusná věta složená ze slov."
seznam=veta.split(" ",2)
print(veta)
print(seznam)
"""

"""
ret="22 3 28 20 16"
sez=ret.split(" ")
cisla=[]
for i in sez:
    cisla.append(int(i))
print(sez)
print(cisla)
"""


# ret="Mival bil v Kijove"
# novy=ret.replace("i","y")
# print (novy)


# kod="<html> <H1>Nadpis</H1> </html>"
# novy=kod.replace("H1", "h1")
# print(novy)



"""
Úkol:
1) Vložte číslo 20 pětkrát do řetězce pomocí všech 
   možných typů (%i,%f,%x,%o,%s).
2) Vypište pod sebe 10 náhodných čísel z 
   intervalu (0-1000) na 5 míst s měnou 'Kč' tak, aby:
   a) čísla ve sloupci byla zarovnána vlevo
      12   Kc
      897  Kc
      6    Kc
   b) čísla ve sloupci byla zarovnána vpravo     
        12 Kc
       897 Kc
         6 Kc
3) Načtěte z klávesnice řetězec, zjistěte jeho 
   délku a vypište jeho posledních 5 znaků   
4) Načtěte datum jako řetězec (dd.mm.rrrr) a vypište 
   jaké datum bude za 14 dnů opět v podobě řetězce. 
   Použijte split() pro získání částí data.

DU: Načtěte řetězec čísel oddělených čárkami a 
    spočítejte součet těchto čísel.
    Př: vstup: 2,6,15,7
        vystup: 30
"""

