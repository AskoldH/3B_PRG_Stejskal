# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012

@author: Radek
"""
"""     Soubory (čtení)
        
readlines() - vrátí seznam řádků souboru od akt. poz.          
readline() - přečte řetězec od aktuální pozice do 
             konce řádku  
read(x) - přečte řetězec o zadané délce, když neuvedeme
          hodnotu, přečte celý soubor
        - při pokusu o čtení na konci souboru vrací
          prázdný řetězec ""
tell() - vrací aktuální pozici v souboru
seek(pocet) - posune aktuální pozici o daný počet
              bytů od začátku souboru
"""


# soub=open("narozeniny.txt","r")
# seznam=soub.readlines()
# soub.close()
# print (seznam)


#Jak se zbavit kocnců řádků? Např. takto:
#for i in range(len(sez)):
#    sez[i]=sez[i][0:-1]
#print (sez)



# soubor=open("narozeniny.txt","r")
# for i in range(2):
#     soubor.readline()
# radek=soubor.readline()
# soubor.close()
# print(radek)


# soubor=open("narozeniny.txt","r")
# vsechno=soubor.read()
# print (vsechno)
# soubor.close()

#ukázka příkazu tell()
# soubor=open("narozeniny.txt","r")
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# text=soubor.read(10)
# print(text)
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# soubor.close()


#ukázka příkazu seek()
# soubor=open("narozeniny.txt","r")
# soubor.seek(12)
# text=soubor.readline()
# print (text)
# soubor.close()


#ošetření otvírání a práce s koncem souboru
try:
    soubor=open("narozeniny.txt","r")
    radek="xxx"
    while radek!="":
        radek=soubor.readline()
        print(radek,end="")
    soubor.close()
except:
    print("Chyba při otvírání souboru!")


"""
Úkoly:
1) Otevřete soubor pokus.txt a vypište jeho 
   obsah do souboru kopie.txt. 
   Použijte buď readlines + writelines nebo read + write.
2) Přečtěte soubor PISMENA.TXT znak po znaku a 
   zjistěte, kolik je v něm písmen "a". Použijte read(1).
3) Načtěte ze souboru řetězec o délce 10 znaků a 
   vypište jej. Co se stane, když soubor bude kratší?
4) Vygenerujte soubor VSTUP.TXT, ve kterém budou dva
   sloupce dvojciferných čísel oddělené mezerou. V
   každém bude 100 čísel.
   Tento soubor postupně přečtěte a do jineho souboru
   vypište řádkové součty ve formátu a+b=c.
"""   
"""
Opakování
1) Otevřete nějaký soubor pro čtení, zjistěte aktuální
   pozici a vypište ji.
2) Načtěte od uživatele 5 řetězců do seznamu a pomocí 
   operace WRITELINES zapište seznam do souboru.
3) Pokuste se otevřít neexistující soubor v módu "a" a 
   přidat na konec krátký text.
4) Otevřete nějaký soubor pro čtení a spočítejte, kolik má
   znaků.   
"""    
    
    

