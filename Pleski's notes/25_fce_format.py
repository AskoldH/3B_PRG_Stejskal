
def main():
    # cislo = 13
    # cislo_str = str(hex(cislo)) + str(cislo) + str(bin(cislo))
    # print(cislo_str)
    import random
    cisla = [random.randint(1, 1000) for i in range(10)]
    for cislo in cisla:
        print("{:>4}".format(cislo) + "{:>3}".format("Kč"))
        print("{:<4}".format(cislo) + "{:>3}".format("Kč"))
if __name__ == '__main__':
    main()