# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:21:47 2013

@author: Radek
"""
"""
Souborové dialogy
- musíme importovat filedialog
- slouží k získání cesty k souboru, nic neotvírají
- danou cestu musíme použít v příkazu open

dialog -> řetězec s cestou -> open(cesta,"mód")
"""

from tkinter import filedialog
from tkinter import *

hlavni=Tk()


def Otevrit():
    cesta = filedialog.askopenfilename(title="Otevřít soubor") #,filetypes=(('Python File', ('*.py','*.pyw')),('Text File', '*.txt'),('All Files', '*')))
    print (cesta)
    #zde proběhne otevření souboru pro čtení, čtení a uzavření
    soubor=open(cesta,"r")
    data=soubor.read()
    soubor.close()
    print(data)

    
def Ulozit():
    cesta = filedialog.asksaveasfilename(defaultextension='.txt',title="Uložit soubor", initialdir="P:\\")
    print (cesta) 
    #zde proběhne otevření pro zápis, zápis a uzavření
    import random
    soubor=open(cesta,"w")
    for i in range(100):
        soubor.write(str(random.randint(500,999))+"\n")
    soubor.close()


"""
defaultextension='.txt',filetypes=(('Text File', '*.txt'),
                                                ('All Files', '*')),
"""


button1=Button(hlavni,text=u"Otevřít",command=Otevrit)
button1.pack(pady=3) 
button2=Button(hlavni,text=u"Uložit",command=Ulozit)
button2.pack(pady=3) 
mainloop()

"""
Úkol:
1) Zapište pod sebe do souboru 100 náhodných čísel mezi 500 a 999
   Použijte dialog asksaveasfilename. 
   
   Rozšíření:
   Uložte 100 náhodných barev v hexa kódu (#RRGGBB) pod sebou.
"""   