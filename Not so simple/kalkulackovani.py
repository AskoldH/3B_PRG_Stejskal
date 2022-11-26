from tkinter import *

def main():
    okno = Tk()
    okno.title("Kalkulačkování")

    okno.minsize(250, 200)
    okno.maxsize(250, 200)

    label = Label(okno, text=('Kalkulačka'), font=("Arial", 24))
    label.pack()

    frame_1 = Frame(okno)
    frame_1.pack()

    frame_2 = Frame(okno)
    frame_2.pack()

    label = Label(frame_1, text=('1. Číslo:'), font=("Arial", 13))
    label.pack(side="left")

    label = Label(frame_2, text=('2. Číslo:'), font=("Arial", 13))
    label.pack(side="left")

    number_1 = StringVar()
    number_2 = StringVar()

    input_1 = Entry(frame_1, state="normal", textvariable=number_1)
    input_1.pack(side="left")

    input_2 = Entry(frame_2, state="normal", textvariable=number_2)
    input_2.pack(side="left")

    frame_3 = Frame(okno)
    frame_3.pack()

    number_3 = StringVar()

    def get_result(operator):
        number_3.set(eval(f"{number_1.get()} {operator} {number_2.get()}"))

    plus_butoon = Button(frame_3, text="+", command=lambda:get_result("+"))
    plus_butoon.pack(side="left")

    minus_butoon = Button(frame_3, text="-", command=lambda:get_result("-"))
    minus_butoon.pack(side="left")

    multiplication_butoon = Button(frame_3, text="*", command=lambda:get_result("*"))
    multiplication_butoon.pack(side="left")

    divide_butoon = Button(frame_3, text="//", command=lambda:get_result("//"))
    divide_butoon.pack(side="left")

    modulo_butoon = Button(frame_3, text="%", command=lambda:get_result("%"))
    modulo_butoon.pack(side="left")

    frame_4 = Frame(okno)
    frame_4.pack()

    frame_5 = LabelFrame(frame_4, bd=1, relief="sunken", text="Výsledek")
    frame_5.pack()

    input_3 = Entry(frame_5, state="readonly", textvariable=number_3)
    input_3.pack()

    end_butoon = Button(frame_4, text="END", command=okno.destroy)
    end_butoon.pack()

    okno.mainloop()

if __name__ == '__main__':
    main()