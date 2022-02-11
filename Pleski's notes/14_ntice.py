# vytvoření n-tice
import random
def vytvoreni():
    ntice = (random.randint(1, 50), random.randint(1, 50), random.randint(1, 50))
    print(ntice)

# seznam s nticemi
def seznam():
    lst = []
    for i in range(0, 10):
        lst.append((random.randint(0,1), random.randint(0,1), random.randint(0,1)))
        print(lst[i])

while True:
    user_input = input("Zadejte úkol(vytvoření, seznam, pro konec \"end\"): ")
    if user_input == "vytvoření":
        vytvoreni()
    elif user_input == "seznam":
        seznam()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")