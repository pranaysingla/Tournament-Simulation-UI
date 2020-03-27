from tkinter import *
from PIL import Image, ImageTk
import tkinter.font


def raise_frame(frame):
    frame.tkraise()


top = Tk()
top.geometry("1072x746")
f1 = Frame(top, width=1072, height=746)
f2 = Frame(top, width=1072, height=746)
f3 = Frame(top, width=1072, height=746)
f4 = Frame(top, width=1072, height=746)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

image2 = Image.open('Football_Pitch1.jpg')
image1 = ImageTk.PhotoImage(image2)
background_label = Label(f1, image=image1)
background_label.pack()


# Knockout drop downs
def knock1():
    tkvar = StringVar(f1)

    choices = (4, 8, 16, 32, 64)
    tkvar.set(4)

    popupMenu = OptionMenu(f1, tkvar, *choices)
    lbl2 = Label(f1, text="Choose number of Teams", font=("Arial",15,"bold"))
    lbl2.place(x=180, y=330)
    popupMenu.place(x=180, y=370)

    def change_dropdown(*args):
        no_teams = tkvar.get()
        print(tkvar.get())

    tkvar.trace('w', change_dropdown)

# group and knockout drop downs

def gandk():
    tkvar1 = StringVar(f1)

    choices1 = (8, 16, 32)
    tkvar1.set(8)

    popupMenu1 = OptionMenu(f1, tkvar1, *choices1)
    lbl3 = Label(f1, text="Choose number of Teams", font=("Arial",15,"bold"))
    lbl3.place(x=645, y=330)
    popupMenu1.place(x=645, y=370)

    def change_dropdown1(*args):
        no_teams1 = tkvar1.get()
        print(tkvar1.get())

    tkvar1.trace('w', change_dropdown1)

# No of groups
    tkvar2 = StringVar(f1)

    choices2 = (2, 4, 8)
    tkvar2.set(2)

    popupMenu2 = OptionMenu(f1, tkvar2, *choices2)
    lbl4 = Label(top, text="Choose number of Groups", font=("Arial",15,"bold"))
    lbl4.place(x=645, y=430)
    popupMenu2.place(x=645, y=470)

    def change_dropdown2(*args):
        no_teams2 = tkvar2.get()
        print(tkvar2.get())

    tkvar2.trace('w', change_dropdown2)

# Knockout Buttons
b1 = Button(f1, text='KNOCK-OUT', command = knock1, font=("Arial",20,"bold"), fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b1.place(x=180, y=200)

b2 = Button(f1, text='GROUP & \nKNOCK-OUT', command = gandk, font=("Arial",20,"bold"), fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b2.place(x=645, y=200)

# Seed Buttons

b3 = Button(f1, text='SEEDED', font=("Arial",20,"bold"), fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b3.place(x=180, y=530)

b4 = Button(f1, text='UNSEEDED', font=("Arial",20,"bold"), fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b4.place(x=645, y=530)

Button(f1, text='Go to frame 2', command=lambda: raise_frame(f2)).place(x=700, y=600)
Label(f2, text='FRAME 2').pack()

raise_frame(f1)
top.mainloop()
