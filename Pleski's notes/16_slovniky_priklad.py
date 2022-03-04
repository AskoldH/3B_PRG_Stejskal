def main():
    zbozi = {"chléb": 30,
             "máslo": 36,
             "mléko": 17,
             }

    key = input("Zadejte název zboží: ")
    value = int(input("Zadejte cenu v kč: "))
    zbozi[key] = value

    print("\nSlovník zboží:")
    for key in zbozi:
        print(f"{key}: {zbozi[key]} Kč")

    if "čokoláda" in zbozi:
        print("\nSlovo \"čokoláda\" je v seznamu!")

    else:
        print("\nSlovo \"čokoláda\" není v seznamu!")

    print("\nZdražený slovník zboží:")
    for key in zbozi:
        zbozi[key] += 5
        print(f"{key}: {zbozi[key]} Kč")

    del zbozi["chléb"]

    print("\nSlovník zboží bez chleba a zdražený:")
    for key in zbozi:
        print(f"{key}: {zbozi[key]} Kč")


if __name__ == '__main__':
    main()
