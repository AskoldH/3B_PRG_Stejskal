import random
from tkinter import *


random_number = random.randint(1, 100)
number_of_attems = 1

def main():
    main_window = Tk()
    main_window.minsize(350, 200)
    main_window.maxsize(350,00)
    main_window.title("Hádej číslo!")

    main_frame = Frame(main_window, relief="sunken", bd=3)
    main_frame.pack()
    # main_frame.place(relx=0.5, rely=.36, anchor="center")

    user_info_label_1 = Label(main_frame, text="Jaké číslo si myslím?", font=("Arial", 20, "bold"))
    user_info_label_1.pack()
    main_frame.place(relx=0.5, rely=.36, anchor="center")

    user_info_label_2 = Label(main_frame, text="(od 1 do 100)", font=("Arial", 12))
    user_info_label_2.pack()

    chosen_number_user = StringVar()
    user_choise_input = Entry(main_frame, state="normal", textvariable=chosen_number_user)
    user_choise_input.insert(0, "1")
    user_choise_input.pack()

    message_label = Label(main_window, text="", font=("Arial", 15, "bold"))
    message_label["text"] = "Vyber číslo a hraj!"
    message_label["bg"] = "grey"
    message_label.pack(side="bottom")
    # message_label.place(relx=.5, rely=.8, anchor="center")

    def check_value():
        global random_number
        global number_of_attems
        if random_number == int(chosen_number_user.get()):
            message_label["text"] = f"Uhodl jsi na {number_of_attems} pokusů! Hraj znova!"
            message_label["bg"] = "green"
            random_number = random.randint(1, 100)
            number_of_attems = 0
            return
        elif random_number < int(chosen_number_user.get()):
            message_label["text"] = "Hádáš moc velké!"
            message_label["bg"] = "orange"
        else:
            message_label["text"] = "Hádáš moc malé!"
            message_label["bg"] = "red"
        number_of_attems += 1



    check_button = Button(main_window, text="Hrajeme", command=check_value)
    check_button.pack(side="bottom")
    # check_button.place(relx=.5, rely=.92 , anchor="center")

    main_window.mainloop()

if __name__ == '__main__':
    main()