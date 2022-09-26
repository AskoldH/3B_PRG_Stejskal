import pylab as p


def bad_input():
    print("\nChybně zadán příkaz!")


def calculate_y(x_values, choosen_fce):
    # this is so stupid, is there any other way?
    if choosen_fce == '1':
        y_values = p.sin(x_values)
    elif choosen_fce == '2':
        y_values = p.cos(x_values)
    elif choosen_fce == '3':
        y_values = x_values**2
    elif choosen_fce == '4':
        y_values = x_values ** 3
    elif choosen_fce == '5':
        y_values = 2*x_values
    else:
        return []
    return y_values


def get_plot_settings():
    return (input("Zadejte barvu grafu (př. red, green, blue, ...,  nebo v hexa formátu -> #103ee3, ...): "),
            input("Zadejte styl čáry grafu (plná-> '-', čárkovaná -> '--', tečkovaná -> ':', ...): "),
            input("Zadejte tloušťku čáry (př. 2 nebo 4): "),
            input("Zadejte popis osy x: "),
            input("Zadejte popis osy y: "),
            input("Zadejte popis grafu: "),
            )


def show_fce(choosen_fce):
    while True:
        if choosen_fce not in ('1', '2', '3', '4', '5'):
            return False
        user_settings = input("\nVyberte: default(d)-defaultní rozsah x hodnot a kroku, "
                              "advanced(a)-vlastní nastavení x hodnot a kroku: ")

        if user_settings in ("default", 'd'):
            x_values = p.arange(-10, 10, 0.1)
            break

        elif user_settings in ("advanced", 'a'):
            while True:
                user_scope_x = input("\nZadejte rozsah x hodnot(př. -> 2:8): ").split(":")
                user_step = input("Zadeje velikost kroku(př. -> 0.5 nebo 3): ")
                try:
                    x_values = p.arange(int(user_scope_x[0]), int(user_scope_x[1]), float(user_step))
                    break
                except (ValueError, IndexError):
                    bad_input()
            break
        else:
            bad_input()

    y_values = calculate_y(x_values, choosen_fce)
    if not len(y_values):
        return False

    while True:
        user_settings = input("\nVyberte: default(d)-defaultní zobrazení grafu, "
                              "advanced(a)-chci zobrazit upravit jak graf bude vypadat(všechny prarametry budou "
                              "povinné): ")

        if user_settings in ("default", 'd'):
            p.plot(x_values, y_values)
            break

        elif user_settings in ("advanced", 'a'):
            while True:
                try:
                    plot_settings = get_plot_settings()
                    p.plot(x_values, y_values, plot_settings[1], color=plot_settings[0], linewidth=plot_settings[2])
                    p.xlabel(plot_settings[3])
                    p.ylabel(plot_settings[4])
                    p.title(plot_settings[5])
                    break
                except:
                    bad_input()
            break

        else:
            bad_input()

    p.show()
    return True

def main():
    while True:
        user_menu = input("\nVyberte: run(r)-chci vybrat fci, end(e)-konec programu: ")
        if user_menu in ("end", 'e'):
            print("Ciao!")
            return
        elif user_menu in ("run", 'r'):
            while True:
                if show_fce(input("\nVyberte: 1-sin(x), 2-cos(x), 3-x**2, 4-x**3, "
                                  "5-2x: ")):
                    break

                bad_input()

        else:
            bad_input()


if __name__ == '__main__':
    main()