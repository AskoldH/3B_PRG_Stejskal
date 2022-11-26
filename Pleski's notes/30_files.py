def main():
    # 1
    # file = open("data.txt", 'w')
    # for i in range(1000):
    #     file.write(str(i)+"\n")
    # file.close()

    # 2
    # with open('pokus.txt', 'r') as first_file, open('kopie.txt', 'w') as second_file:
    #     for line in first_file:
    #         second_file.write(line)

    # 3
    # with open("PISMENA.txt", 'r') as file:
    #     text = file.read()
    #     pocet_acek = 0
    #     for char in text:
    #         if char == 'a':
    #             pocet_acek += 1
    #     print(pocet_acek)

    # 4
    # with open("data.txt", 'r') as file:
    #     text = file.read()[:10]
    #     print(text)

    # 5
    # import random
    # with open("VSTUP.txt", 'w') as input_file:
    #     for i in range(100):
    #         input_file.write(f"{random.randint(0, 100)} {random.randint(0, 100)}\n")
    #
    # with open("VSTUP.txt", 'r') as input_file, open("VYSTUP.txt", 'w') as output_file:
    #     lines = input_file.readlines()
    #     for line in lines:
    #         numbers = line.split()
    #         output_file.write(f"{numbers[0]}+{numbers[1]}={int(numbers[0])+int(numbers[1])}\n")

    # 6
    # with open("data.txt", 'r') as file:
    #     file.readline()
    #     print(file.tell())

    # 7
    # retezce = []
    # for i in range(5):
    #     retezce.append(input("Zadejte řetězec: "))
    #
    # print(retezce)
    # with open("data.txt", 'a') as file:
    #     for line in retezce:
    #         file.write(f"{line}\n")

    # 8
    # with open("abraka.txt", 'a') as file:
    #     file.write("Ahojda")

    # 9
    # with open("data.txt", 'r') as file:
    #     print(len(file.read()))
    pass

if __name__ == '__main__':
    main()