def main():
    string = "ABC"
    vysledek = []

    for i in range(len(string)):
        for j in range(len(string) -1):
            for k in range(len(string) -2):
                vysledek.append(string[i] + string[j] + string[k])
    print(vysledek)


if __name__ == '__main__':
    main()
