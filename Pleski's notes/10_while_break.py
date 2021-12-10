# 1 pět čisel
def pet_cisel():
    i = 5
    while i > 0:
        if int(input("Zdadejte číslo: ")) < 0: break
        i -= 1
    print("Číslo bylo záporné!")

# 2 ciferný součet
def ciferny_soucet():
    user_input = input("Zadejte číslo: ")
    soucet = 0
    i = 0
    while i < len(user_input):
        soucet += int(user_input[i])
        i += 1
    print(f"""Ciferný součet je {soucet}!""")

# 3 myslím si
def myslim_si():
    import random
    i = random.randint(0, 100)
    user_input = int(input("Zadejte číslo které si myslím: "))
    pokusy = 1
    while i != user_input:
        pokusy += 1
        if i < user_input: print("Měnší!")
        elif i > user_input: print("Větší!")
        user_input = int(input("Zadejte číslo které si myslím: "))
    print(f"""Správně, na {pokusy}. pokus!""")

# spuštění
while True:
    user_input = input("Zadejte úkol(ciferný součet, pět čísel, myslím si, pro konec \"end\"): ")
    if user_input == "ciferný součet":
        ciferny_soucet()
    elif user_input == "pět čísel":
        pet_cisel()
    elif user_input == "myslím si":
        myslim_si()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")
