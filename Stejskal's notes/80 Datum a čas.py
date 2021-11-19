# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:31:18 2013

@author: Radek
"""
"""
existuje i knihovna time
"""


from datetime import *

dnes = datetime.now()

print (str(dnes))

print ("Aktualni rok: %i" % dnes.year)

print ("Aktualni mesic: %i" % dnes.month)
print ("Aktualni den: %i" % dnes.day)
print ("Aktualni hodina: %i" % dnes.hour)
print ("Aktualni minuta: %i" % dnes.minute)
print ("Aktualni vterina: %i" % dnes.second)
print ("Aktualni mikrosekunda: %i" % dnes.microsecond)

"""
Úkol:
1) Naprogramujte digitální hodiny, které 
   každou desetinu sekundy aktualizují svůj čas. 
   Zobrazujte pouze h:m:s. Využijte metodu after.
2) Zjistěte aktuální čas.
   Proveďte cyklus, který 1000 000x zvedne proměnnou
   o jedničku.
   Znovu zjistěte čas a vypište, jak dlouho cyklus 
   trval.
"""   














from tkinter import *
hlavni = Tk()

hodiny=Label(hlavni,font=("Arial",100))
hodiny.pack()

def AktualizujCas():
    ted=datetime.now()
    vystup="%02i:%02i:%02i" % (ted.hour,ted.minute,ted.second)
    hodiny["text"]=vystup
    hlavni.after(1000,AktualizujCas)

AktualizujCas()    

mainloop()



