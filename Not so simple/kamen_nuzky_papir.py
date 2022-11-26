import random
from tkinter import *


player_points = pc_points = 0
def main():
    main_window = Tk()
    main_window.minsize(300, 300)
    main_window.maxsize(300, 300)
    main_window.title("Kámen, nůžky, papír, teď!")

    left_frame = LabelFrame(main_window, relief="sunken", text="Hráč", pady=40)
    left_frame.pack(side="left")
    left_frame.place(relx=0.32, rely=.36, anchor="center")

    user_info_label = Label(left_frame, text="1-kámen, 2-nůžky, 3-papír")
    user_info_label.pack()

    score_label = Label(main_window, text=f"Skóre je {player_points}:{pc_points}", font=("Arial", 15, "bold"))
    score_label.pack()

    chosen_number_user = StringVar()
    user_choise_input = Entry(left_frame, state="normal", textvariable=chosen_number_user)
    user_choise_input.insert(0, "1")
    user_choise_input.pack(side="left")

    right_frame = LabelFrame(main_window, height=50, relief="sunken", text="Počítač", padx=10, pady=53)
    right_frame.pack(side="left")
    right_frame.place(relx=.8, rely=.36, anchor="center")

    def get_computer_symbol(chosen_number):
        if chosen_number == 1: return "Kámen"
        elif chosen_number == 2: return "Nůžky"
        return "Papír"

    def calculate_winner():
        computer_chosen_number = random.randint(1, 3)
        computer_result_label["text"] = get_computer_symbol(computer_chosen_number)

        global pc_points
        global player_points

        kamen, nuzky, papir = 1, 2, 3
        if computer_chosen_number == int(chosen_number_user.get()):
            message_label["text"] = "Remíza!"
            message_label["bg"] = "grey"
        elif computer_chosen_number == kamen and int(chosen_number_user.get()) == nuzky:
            message_label["text"] = "Prohrál jsi!"
            message_label["bg"] = "red"
            pc_points += 1
        elif computer_chosen_number == kamen and int(chosen_number_user.get()) == papir:
            message_label["text"] = "Vyhrál jsi!"
            message_label["bg"] = "green"
            player_points += 1
        elif computer_chosen_number == nuzky and int(chosen_number_user.get()) == papir:
            message_label["text"] = "Prohrál jsi!"
            message_label["bg"] = "red"
            pc_points += 1
        elif computer_chosen_number == nuzky and int(chosen_number_user.get()) == kamen:
            message_label["text"] = "Vyhrál jsi!"
            message_label["bg"] = "green"
            player_points += 1
        elif computer_chosen_number == papir and int(chosen_number_user.get()) == nuzky:
            message_label["text"] = "Vyhrál jsi!"
            message_label["bg"] = "green"
            player_points += 1
        elif computer_chosen_number == papir and int(chosen_number_user.get()) == kamen:
            message_label["text"] = "Prohrál jsi!"
            message_label["bg"] = "red"
            pc_points += 1
        score_label["text"] = f"Skóre je {player_points}:{pc_points}"

    computer_result_label = Label(right_frame, text="#####")
    computer_result_label.pack()

    play_button = Button(main_window, text="Hrajeme", command=calculate_winner)
    play_button.pack(side="bottom")
    play_button.place(relx=.5, rely=.68, anchor="center")

    message_label = Label(main_window, text="", font=("Arial", 24))
    message_label["text"] = "Vybersi a hraj!"
    message_label.pack(side="bottom")
    message_label.place(relx=.5, rely=.8, anchor="center")

    end_button = Button(main_window, text="Konec", command=main_window.destroy)
    end_button.pack(side="bottom")
    end_button.place(relx=.5, rely=.92, anchor="center")

    main_window.mainloop()

if __name__ == '__main__':
    main()