# 1 vložení hvězdičky
def vlozeni_hvezdicky():
    user_input = input("Zadejte slovo: ")
    final_word = ''
    for letter in user_input:
        final_word += letter + '*'
    print(final_word)

# 2 počítání áček
def pocitani_a():
    user_input = input("Zadejte slovo: ")
    pocet_a = 0
    for letter in user_input:
        if letter == 'a' or letter == 'A':
            pocet_a += 1
    print(f"""Ve slově je { pocet_a } "a"!""")

# 3 součet cifer
def soucet_cifer():
    user_input = input("Načtěte řetězec: ")
    ciferny_soucet = 0
    for char in user_input:
        try:
            int(char)
            ciferny_soucet += int(char)
        except: pass
        # nebo
        # cisla = "0123456789"
        # if char in cisla: ciferny_soucet += int(char)
    print(f"""Ciferný součet číslic v řetězci je { ciferny_soucet}!""")

# dnešní datum
import datetime
date = datetime.date
def datum():
    for i in range(8):
        for j in range(6):
            print(date)

# jména
def jmena():
    jmeno = "Askold"
    poradove_cislo = 1
    for i in range(30):
        for j in range(5):
            print(f"""{ poradove_cislo }. { jmeno }""")
            poradove_cislo += 1
        print()

# výpis
def vypis():
    user_input = int(input("Zadejte číslo: "))
    cislo = 1
    for i in range(user_input):
        print(cislo, end="")
        cislo += 1

# dělitelé
import random
def vypis_delitelu():
    n = int(input("Zadejte číslo: "))
    for i in range(n):
        nahodne_cislo = random.randint(0, 10)
        print(str(nahodne_cislo) + '. ', end='')
        for i in range(nahodne_cislo):
            if (nahodne_cislo % (i + 1)) == 0:
                print(str(i + 1) + ' ', end="")
        print()


# spuštění
while True:
    user_input = input("Zadejte úkol(vložení hvězdičky, počítání a, ciferný součet, dnešní datum, jména, výpis, výpis dělitelů, pro konec \"end\"): ")
    if user_input == "vložení hvězdičky":
        vlozeni_hvezdicky()
    elif user_input == "počítání a":
        pocitani_a()
    elif user_input == "ciferný součet":
        soucet_cifer()
    elif user_input == "dnešní datum":
        datum()
    elif user_input == "jména":
        jmena()
    elif user_input == "výpis":
        vypis()
    elif user_input == "výpis dělitelů":
        vypis_delitelu()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")