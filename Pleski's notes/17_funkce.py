def AnaX(a, x):
    print(f"A na xtou je {a ** x}!")


def Linear(a, b):
    print(f"{-(b / a)}")


def Prumer(a, b, c):
    return (a + b + c) / 3


import random
def Kostka():
    return random.randint(1, 6)


import random
def VratSeznam(pocet, od, do):
    seznam = []
    for i in range(pocet):
        seznam.append(random.randint(od, do))
    return seznam


import random
def ZasifrujText(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        rnd = random.choice(abc)

def main():
    # AnaX(5, 3)
    # Linear(4, 2)
    # print(Prumer(1, 1, 2))
    # print(Kostka())
    # print(VratSeznam(4, 10, 15))
    ZasifrujText("Ahoj")

if __name__ == '__main__':
    main()
