# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:57:07 2012

@author: Radek
"""
"""
Slovníky (dictionary, hash, asociativní pole)
- vytvářejí se pomocí {}
- položky mají tvar INDEX(KLÍČ):HODNOTA
- indexovat můžeme pomocí lib. jednoduch. dat. typu
- indexy musí být unikátní
- k hodnotám se přistupuje pomocí klíčů
"""

#Praktická ukázka
#barvy={"cervena":"#ff0000", "zelena":"#00ff00"}
#nastaveni={"sirka":80,"titulek":"Název něčeho", "mail":"xxx@neco.cz"}
       

#slovnik={5:'pětka',1:"jednička",3:"trojka",2:"dvojka",4:"čtyřka"}
#print (slovnik)

#for i in slovnik:
#    print (slovnik[i])


#vložení nového klíče a hodnoty
#klic=6
#hodnota="šestka"
#slovnik[klic]=hodnota
#print (slovnik)
#
#
#del slovnik[6]
#print (slovnik)


#keys() - vrátí seznam klíčů ze slovníku
#values() - vrátí seznam hodnot
#pomocí operace in zjistíme, zda je hodnota uvnitř
#slovníku

#print (slovnik.keys())
#print (slovnik.values())
#print (6 in slovnik)


"""
Úkol:
1) Vytvořte si jednoduchý anglicko-český překladový 
   slovník, který obsahuje 5 položek.
   Pokuste se pomocí něj překládat uživatelské vstupy,
   pokud zadané slovo nebude ve slovníku, oznamte to
   uživateli.
2) Vytvořte si slovník přátel. Klíčem budou křestní
   jména, hodnotou bude seznam osobních údajů.
   Pomocí cyklu vypište pod sebe všechny osoby ze slovníku.
   ve tvaru:
   jmeno1 => [osobní údaje]    
   jmeno2 => [osobní údaje]
   ...   
"""   

pratele={"Josef":["Pepa","Olomouc","789 456 123"], "Jana":["Beruška","Dolany","777 894 567"]}

for i in pratele:
    print(i,"->",pratele[i])


