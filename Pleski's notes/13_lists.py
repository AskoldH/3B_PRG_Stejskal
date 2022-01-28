# 1 přepisování
def prepis():
    list = [0, 0, 0, 0, 0]
    print(list)
    for i in range(5):
        user_input = int(input(f"""Zadejte {i + 1}. číslo: """))
        list[i] = user_input
    print(list)

    largest, smallest, largest_2nd, largest_2nd_value = list[0], list[0], list[-1], list[-1]
    twenty_in_list = "není"

    for number in list:
        if largest_2nd < number:
            largest_2nd = number

        if number > largest:
            largest_2nd = largest_2nd_value = largest
            largest = number

        if number > largest_2nd_value and number < largest:
            largest_2nd_value = number
        if number < smallest:
            smallest = number

        if number == 20:
            twenty_in_list = "je"

    print(f"""Největší zadané číslo je '{largest}', druhé největší číslo je '{largest_2nd}', druhá největší hodnota je '{largest_2nd_value}', \
nejmenší je '{smallest}' a hodnota 20 {twenty_in_list} v seznamu!""")

# 2 na konec append
def na_konec_append():
    list = []
    for i in range(5):
        list.append(input("Zadejte hodnotu: "))
    print(list)

# 3 20 random čísel
import random
def random_20():
    random_20_list = []
    random_20_list_squere = []

    for i in range(20):
        random_num = random.randint(0, 10)
        random_20_list.append(random_num)
        random_20_list_squere.append(random_num*random_num)

    num_of_81 = random_20_list_squere.count(81)
    for i in range(num_of_81):
        random_20_list_squere.remove(81)
    print(f"""Číslo 81 je v seznamu { num_of_81 }, první list je { sorted(random_20_list) },
druhý je { sorted(random_20_list_squere) }.""")

# 4 kostka
import random
def kostka():
    pokusy = []
    for i in range(6):
        pokusy.append(random.randint(1, 6))
    print("Byly hozeny čísla:", pokusy, "!")

    for i in range(6):
        if (i+1) in pokusy: pokusy.remove(i+1)

    if len(pokusy) == 0:
        print("Byla to postupka!")

    else: print("Postupka to nebyla!")

# 5 balicek karet
import random
def balicek():
    karty = []
    for i in range(9):
        karty.append(("♥" + str(i+1)))
        karty.append(("♠" + str(i+1)))
        karty.append(("♦" + str(i+1)))
        karty.append(("♣" + str(i+1)))
    print(karty)

    balicek_karet = []
    for i in range(len(karty)):
        balicek_karet.insert(random.randint(0, len(karty)), karty[i])
    print(balicek_karet)

# sportka
import random
def sportka():
    zadane = []
    vygenerovane = []
    for i in range(6):
        zadane.append(int(input("Zadejte číslo od 1 do 49: ")))

    while True:
        random_num = random.randint(1, 50)
        if len(vygenerovane) == 6: break
        elif vygenerovane.count(random_num) == 0:
            vygenerovane.append(random_num)

    pocet_spravnych = 0
    for num in zadane:
        pocet_spravnych += vygenerovane.count(num)
    print(f"""Trefil jsi { pocet_spravnych } čísel protože počítač vybral čísla { vygenerovane }!""")

while True:
    user_input = input("Zadejte úkol(přepisování, append, 20 random, kostka, balíček, sportka pro konec \"end\"): ")
    if user_input == "přepisování":
        prepis()
    elif user_input == "append":
        na_konec_append()
    elif user_input == "20 random":
        random_20()
    elif user_input == "kostka":
        kostka()
    elif user_input == "balíček":
        balicek()
    elif user_input == "sportka":
        sportka()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")