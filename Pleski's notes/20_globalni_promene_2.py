# Napište program pro evidenci lidí (jmen):
#    Evidence bude v globálním seznamu.
#    Napište funkce:
#      Pridej(jmeno) - přidá jméno do evidnce
#      Smaz(jmeno) - smaže jméno v evidenci
#      Zjisti(jmeno) - vrátí True nebo False
#      Vypis() - vypíše celou evidenci


seznam_jmen = []


def pridej(jmeno):
    seznam_jmen.append(jmeno)


def smaz(jmeno):
    seznam_jmen.remove(jmeno)


def zjisti(jmeno):
    if jmeno in seznam_jmen:
        return True
    return False


def vypis():
    for jmeno in seznam_jmen:
        print(f"{seznam_jmen.index(jmeno) + 1}. {jmeno}")


def main():
    while True:
        user_input = input(
            "Vyberte funkci -> 1-Přidání jména, 2-smazání jména, 3-zjištění jestli je jméno v seznamu, 4-vypiš seznam: ")
        if user_input == '1':
            pridej(input("Zadej jméno které chceš přidat: "))
        elif user_input == '2':
            smaz(input("Zadej jméno které chceš smazat: "))
        elif user_input == '3':
            if zjisti(input("Zadejte jméno pro které chcete zjistit zda je v seznamu: ")):
                print("Jméno je v seznamu!")
            else:
                print("Jméno není v seznamu!")
        elif user_input == '4':
            vypis()


if __name__ == '__main__':
    main()
