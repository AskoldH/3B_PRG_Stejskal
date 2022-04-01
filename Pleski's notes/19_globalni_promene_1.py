# Napište program pro simulaci bankovního účtu. Bude mít 3 funkce:
#    Vklad(castka) - přidá peníze na účet
#    Vyber(castka) - odebere peníze z účtu
#    Zustatek()    - vypíše zůstatek na účtu
#    S účtem budou funkce pracovat jako s globální proměnnou 'ucet'.
#    Snažte se v programu přehledně komunikovat s uživatelem.

ucet = 0

def vklad(vklad_v_kc):
    global ucet
    ucet += vklad_v_kc

def vyber(vyber_v_kc):
    global ucet
    ucet -= vyber_v_kc
    if ucet < 0:
        print(f"Máte na účtu pouze { ucet },- Kč, výběr nelze uskutečnit!")
        ucet += vyber_v_kc

def zustatek():
    print(f"Na vašem účtu máte { ucet },- Kč!")

def main():
    while True:
        user_input = input("Vyberte akci -> 1-vklad, 2-výběr, 3-zobrazení zůstatku: ")
        if user_input == '1':
            user_input = input("Zadejte vklad: ")
            vklad(int(user_input))

        elif user_input == '2':
            user_input = input("Zadejte výběr: ")
            vyber(int(user_input))

        elif user_input == '3':
            zustatek()

if __name__ == '__main__':
    main()


