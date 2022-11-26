from tkinter import *

def main():
    # uvod
    # hlavni = Tk()
    # hlavni["bg"] = "yellow"
    # hlavni.minsize(500, 300)
    # hlavni.maxsize(1000, 600)
    # hlavni.resizable(False, False)
    #
    # nadpis = Label(hlavni, text=("Moje appka"), font=("Arial", 24), fg="red", bg="green")
    # nadpis.pack()
    #
    # tlacitko_3 = Button(hlavni, text="Konec", command=hlavni.destroy)
    # tlacitko_3.pack()
    #
    # hlavni.mainloop()

    # 1
    # okno = Tk()
    # okno.title("Počítadlo")
    #
    # okno.minsize(200, 200)
    # okno.maxsize(200, 200)
    #
    # label = Label(okno, text=('0'), font=("Arial", 24), fg="red", bg="green")
    # label.pack()
    #
    # def plus():
    #     label["text"] = int(label["text"]) +1
    #
    # def minus():
    #     label["text"] = int(label["text"]) -1
    #
    # def reset():
    #     label["text"] = 0
    #
    # plus_butoon = Button(text="PLUS", command=plus)
    # plus_butoon.pack()
    #
    # minus_butoon = Button(text="MINUS", command=minus)
    # minus_butoon.pack()
    #
    # reset_butoon = Button(text="RESET", command=reset)
    # reset_butoon.pack()
    #
    # end_butoon = Button(text="END", command=okno.destroy)
    # end_butoon.pack()
    #
    # okno.mainloop()

    # 2
    # import random
    # okno = Tk()
    # okno.title("Násobička")
    #
    # okno.minsize(200, 200)
    # okno.maxsize(200, 200)
    #
    # label = Label(text="4*5=20", font=("Arial", 24), fg="red", bg="green")
    # label.pack()
    #
    # def generate_problem():
    #     number_a = random.randint(0, 100)
    #     number_b = random.randint(0, 100)
    #     label["text"] = f"{number_a}*{number_b}={number_b*number_a}"
    #
    # button = Button(text="NEXT", command=generate_problem)
    # button.pack()
    #
    # okno.mainloop()

    # 3
    # okno = Tk()
    # okno.title("Kopie")
    #
    # frame_1 = Frame(okno, bd=1, relief="sunken")
    # frame_1.pack()
    #
    # frame_2 = Frame(okno, bd=1, relief="sunken")
    # frame_2.pack()
    #
    # entry_1 = Entry(frame_1, width=25)
    # entry_1.pack(side="right")
    #
    # label_1 = Label(frame_1, text=('VSTUP: '), font=("Arial", 24))
    # label_1.pack()
    #
    # label_2 = Label(frame_2, text=('VYSTUP: '), font=("Arial", 24))
    # label_2.pack(side="left")
    #
    # label_3 = Label(frame_2, text=(''), font=("Arial", 24))
    # label_3.pack()
    #
    # def copy_text():
    #     label_3["text"] = entry_1.get()
    #
    # button_1 = Button(okno, text=("KOPIE"), command=copy_text)
    # button_1.pack()
    #
    # okno.mainloop()

    # 4
    okno = Tk()
    okno.title("Kopie")

    frame_1 = Frame(okno, bd=1, relief="sunken")
    frame_1.pack()

    frame_2 = Frame(okno, bd=1, relief="sunken")
    frame_2.pack()

    entry_1 = Entry(frame_1, width=25)
    entry_1.pack(side="right")

    label_1 = Label(frame_1, text=('Tajná šifra: '), font=("Arial", 24))
    label_1.pack()

    label_2 = Label(frame_2, text=('VYSTUP: '), font=("Arial", 24))
    label_2.pack(side="left")

    label_3 = Label(frame_2, text=(''), font=("Arial", 24))
    label_3.pack()

    def copy_text():
        label_3["text"] = entry_1.get()

    button_1 = Button(okno, text=("ŠIFRUJ VSTUP"), command=copy_text)
    button_1.pack()

    button_2 = Button(okno, text=("KONEC"), command=okno.destroy)
    button_2.pack()

    okno.mainloop()
    pass

if __name__ == '__main__':
    main()
