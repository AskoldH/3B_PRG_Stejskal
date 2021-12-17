# 1 hvězdičky
def hvezdicky():
    user_input = int(input("Zadejte číslo: "))
    for i in range(user_input):
        print("*")

# 2 posloupnost
def posloupnost():
    for i in range(52, 80, 2):
        print(i)

# 3 nahodny pocet
import random
def nahodny():
    for random_int in range(random.randint(1, 50)):
        print(random.randint(1, 100))

# 4 celočiselny dělitel
def delitel():
    user_input = int(input("Zadejte číslo: "))
    print(f"""Číslo {user_input} je celočíselně dělitelné čísli: """, end="")
    for delitel in range(1, user_input):
        if not(user_input % delitel):
            print(delitel, end=", ")
    print(".")

# 5 prvocislo
def prvocislo():
    user_input = int(input("Zadejte číslo pro zjištění: "))
    for delitel in range(2, user_input):
        if not(user_input % delitel):
            print(f"""Číslo {user_input} není prvočíslo!""")
            return
    print(f"""Číslo {user_input} je prvočíslo!""")


# spuštění
while True:
    user_input = input("Zadejte úkol(hvězdičky, posloupnost, náhodný počet, dělitel, prvočíslo, pro konec \"end\"): ")
    if user_input == "hvězdičky":
        hvezdicky()
    elif user_input == "posloupnost":
        posloupnost()
    elif user_input == "náhodný počet":
        nahodny()
    elif user_input == "dělitel":
        delitel()
    elif user_input == "prvočíslo":
        prvocislo()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")
