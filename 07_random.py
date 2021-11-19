import random 

# =============================================================================
# pismeno = random.choice("qwertzuiopasdfghjklyxcvbnm")
# print(pismeno)
# 
# cislo = random.randint(0, 5)
# print(cislo)
# =============================================================================

kamen, nuzky, papir = 1, 2, 3

volba_pocitace = random.randint(1, 3)

i = 0
while i == 0:
    volba_uzivatele = input("Zadejte (kámen, nůžky papír): ")
    if(volba_uzivatele == "kámen"):
        volba_uzivatele = kamen
        i = 1
    elif(volba_uzivatele == "nůžky"):
        volba_uzivatele = nuzky
        i = 1
    elif(volba_uzivatele == "papír"):
        volba_uzivatele = papir
        i = 1
    else:
        print("Zadáno špatně!")

if(volba_pocitace == 1):
    print("Počítač si vybral kámen!")
elif(volba_pocitace == 2):
    print("Počítač si vybral nůžky!")
elif(volba_pocitace == 3):
    print("Počítač si vybral papír!")

if volba_pocitace == volba_uzivatele:
    print("Remíza!")
elif (volba_pocitace == 1 and volba_uzivatele == 2) or (volba_pocitace == 2 and volba_uzivatele == 3) or (volba_pocitace == 1 and volba_uzivatele == 3):
    print("Vyhrál počítač!")
elif volba_uzivatele == 1 or volba_uzivatele == 2 or volba_uzivatele == 2:
    print("vyhrál jsi!")