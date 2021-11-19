# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:37:21 2012

@author: Radek
"""
"""
Metoda place
Umožňuje umístění komponenty na konkrétní souřadnice:
a) Absolutní - v pixelech, počítá se z levého horního rohu
   place(x= , y= )
b) Relativní - v desetinných číslech, nejmenší hodnota je 0 a
               největší je 1
   place(relx= , rely= )

Můžeme přidat i parametr anchor, což je kotevní bod komponety.
Jsou tyto: n, ne, e, se, s, sw, w, nw, center

POZOR! V jednom okně nelze kombinovat více zobrazovacích metod!
"""

from tkinter import *

hlavni = Tk()

napis=Label(hlavni,text="Toto je text na abs. souřadnicích")
napis.place(x=50, y=50, anchor="nw")

napis2=Label(hlavni,text="Toto je text na relativních. souřadnicích")
napis2.place(relx=0.5, rely=0.5, anchor="center")

tlacitko=Button(hlavni,text="Konec",command=hlavni.destroy)
tlacitko.place(x=50,y=100,width=100,height=40)
   
hlavni.mainloop()

"""
Úkol:
1) Stanovte si velikost okna.
   Umístěte do okna tři tlačítka "Konec" na náhodné 
   souřadnice tak, aby nepřekračovalo hranice okna.
"""   








