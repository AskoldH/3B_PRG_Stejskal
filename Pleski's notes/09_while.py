# # 1 - heslo
def heslo():
    input_password = input("Zadejte heslo: ")
    password = "monitor"
    attempt = 1

    while True:
        if input_password == password:
            print(f"""Heslo zadáno správně a to na {attempt}. pokus!""")
            break

        attempt += 1
        input_password = input("Heslo bylo zadáno špatně, zadejte ho znovu: ")


# # 2 - součet n hodnot
def soucet_n():
    n = int(input("Zadejte číslo n: "))
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    print(f"""Součet je {total}!""")


# # 3 - tabulka hodnot gon fcí
import math as m

def gon_fce():
    angle = 0
    print("uhel\t\tsin \t\t\tcos \t\t\ttg  \t\t\tcotg")
    while angle <= 90:
        angle_rad = m.radians(angle)
        value_sin = "%0.3f" % m.sin(angle_rad)
        value_cos = "%0.3f" % m.cos(angle_rad)
        if angle == 90:
            value_tg = "UD   "
        else:
            value_tg = "%0.3f" % m.tan(angle_rad)

        if angle == 0:
            value_cotg = "UD   "
        else:
            value_cotg = "%0.3f" % (1 / m.tan(angle_rad))
        print(f"""{angle}°\t\t\t{value_sin}\t\t\t{value_cos}\t\t\t{value_tg}\t\t\t{value_cotg}""")
        angle += 5


# # 4 Převod do bin z decimal
def prevod():
    number_d = int(input("Zadejte číslo: "))
    number_b = ''
    vysledek_deleni = number_d // 2
    zbytek = number_d % 2
    number_b += str(zbytek)

    def check_lenth(zbytky):
        for i in range(3, 999, 5):
            x = 1
            if len(zbytky) == i + x:
                x += 1
                return True

    while vysledek_deleni:
        zbytek = vysledek_deleni % 2
        vysledek_deleni = vysledek_deleni // 2
        number_b = str(zbytek) + number_b
        if check_lenth(number_b):
            number_b = " " + number_b

    print(number_b)

while True:
    user_input = input("Zadejte úkol(prevod, heslo, soucet_n, gon_fce, pro konec \"end\"): ")
    if user_input == "prevod":
        prevod()
    elif user_input == "heslo":
        heslo()
    elif user_input == "soucet_n":
        soucet_n()
    elif user_input == "gon_fce":
        gon_fce()
    elif user_input == "end":
        break
    else: print("Zadej to správně!")