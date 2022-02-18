# slovnik
import time
def slovnik():
    slovnik = {"ahoj":"hi", "počítač":"computer", "obrazovka":"screen", "klávesnice":"keyboard", "paměť":"memory"}
    while True:
        start_time = time.time()
        user_input = input("Zadejte slovo k přeložení, pro přidání zadejte \"přidat\" nebo pro konec \"end\": ")
        if user_input == "end":
            break
        elif user_input == "přidat":
            czech_word = input("Zadejte české slovo: ")
            english_word = input("Zadejte překlad pro ono slovo: ")
            slovnik[czech_word] = english_word
        elif user_input in slovnik:
            print(f"""Překlad pro "{ user_input }" je "{ slovnik[user_input] }".""")
        else: print("Slovo není ve slovníku, zkuste jiné slovo.")
        execution_time = (time.time() - start_time)
        print(execution_time)

# pratele
def pratele():
    seznam_pratel = {"Dominik":{"město":"Jeseník", "telefon":"785 248 652", "délka vlasů":12},
                     "Ladislav": {"město": "Skrbeň", "telefon": "777 514 222", "délka vlasů": 0},
                     "Petr": {"město": "Šternberk", "telefon": "854 214 255", "délka vlasů": 6},
                     }

    for name in seznam_pratel.keys():
        print(f"""{ name } => Bydlí ve městě { seznam_pratel[name]["město"]}, 
           telefonní číslo je { seznam_pratel[name]["telefon"] }, 
           délka vlasů je { seznam_pratel[name]["délka vlasů"] } centimetrů!""")

# test rychlosti
import time
def test_rychlosti():
    slovnik = {}
    seznam = []
    for i in range(0, 1_000_000):
        slovnik[i] = i
        seznam.append(i)

    start_time_seznam = time.time()
    for i in range(0, 10_000):
        if 500_000 in seznam:
            pass
    execution_time_seznam = (time.time() - start_time_seznam)

    print(f"""Čas pro seznam je: { execution_time_seznam } sekund!""")

    start_time_slovnik = time.time()
    for i in range(0, 10_000):
        if 200_000 in slovnik:
            pass
    execution_time_slovnik = (time.time() - start_time_slovnik)

    print(f"""Čas pro slovník je: {execution_time_slovnik} sekund!""")

    print(f"""Slovnik byl { execution_time_slovnik / execution_time_seznam }x rychlejší!!""")

while True:
    user_input = input("Zadejte úkol(slovnik, přátele, test rychlosti nebo pro konec \"end\"): ")
    if user_input == "slovnik":
        slovnik()
    elif user_input == "přátelé":
        pratele()
    elif user_input == "test rychlosti":
        test_rychlosti()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")