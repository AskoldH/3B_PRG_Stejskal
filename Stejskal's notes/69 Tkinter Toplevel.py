# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:01:49 2013

@author: Radek
"""
"""
Množství otevřených oken je možno regulovat pomocí 
globální proměnné.
"""

from tkinter import *

hlavni=Tk()
#pocet=0   

#def ZavriOkno1():
#    global okno1
#    global pocet    
#    pocet=0
#    okno1.destroy()    

def ZobrazOkno1():
    global okno1
    try:
        if okno1.winfo_exists()==0:    
            okno1=Toplevel()
            okno1.title(u"První okno")
        
            tlZavriOkno1=Button(okno1,text=u"Zavři toto okno",command=okno1.destroy)
            tlZavriOkno1.pack()
    except NameError:
        okno1=Toplevel()
        okno1.title(u"První okno")
        
        tlZavriOkno1=Button(okno1,text=u"Zavři toto okno",command=okno1.destroy)
        tlZavriOkno1.pack()
    
def ZobrazOkno2():
    okno2=Toplevel()
    okno2.title(u"Druhé okno")

    tlZavriOkno2=Button(okno2,text=u"Zavři toto okno",command=okno2.destroy)
    tlZavriOkno2.pack()   
    tlZavriAplikaci=Button(okno2,text=u"Zavři celou aplikaci",command=hlavni.destroy)
    tlZavriAplikaci.pack() 

    
tlac1 = Button(hlavni, text="Zobraz prvni podokno",command=ZobrazOkno1)
tlac1.pack()
tlac2 = Button(hlavni, text="Zobraz druhe podokno",command=ZobrazOkno2)
tlac2.pack()

hlavni.mainloop()

"""
Úkoly:
1) Umožněte uživateli otevřít z hlavního okna 2 podokna. Jedno bude 
   zelené a druhé červené. Zajistěte, aby nešlo otevřít více než 1
   vedlejší okno.
"""