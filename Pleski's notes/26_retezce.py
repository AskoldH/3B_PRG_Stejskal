def main():
    # user_input = input("Zadejte řetězec: ")
    # delka_user_input = len(user_input)
    # print(user_input[:5])
    # print(user_input[-5:])
    # print(user_input[int(delka_user_input/2)])

    # user_input = input("Zadejte řetězec: ")
    # user_input_lst = user_input.split(",")
    # suma = 0
    # for number in user_input_lst:
    #     suma += int(number)
    # print(suma)

    user_input = input("Zadejte datum: ")
    user_input_list = user_input.split('.')
    dny = int(user_input_list[0])
    mesice = int(user_input_list[1])
    roky = int(user_input_list[2])

    dny += 14
    if dny > 30:
        dny -= 30
        mesice +=1
        if mesice > 12:
            mesice -= 12
            roky += 1

    print(f"Za 14 dní bude {dny}.{mesice}.{roky}!")

if __name__ == '__main__':
    main()