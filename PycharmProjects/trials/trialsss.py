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
f5 = Frame(top, width=1072, height=746)
f6 = Frame(top, width=1072, height=746)

for frame in (f1, f2, f3, f4, f5, f6):
    frame.grid(row=0, column=0, sticky='news')

image2 = Image.open('Football_Pitch1.jpg')
image1 = ImageTk.PhotoImage(image2)
background_label = Label(f1, image=image1)
background_label.pack()

no_teams = ''
entries = ''
no_teams1 = ''
entries1 = ''
no_teams2 = ''
entries2 = ''
# Knockout drop downs
def knock1():
    tkvar = StringVar(f1)

    choices = (4, 8, 16)
    tkvar.set(4)

    popupMenu = OptionMenu(f1, tkvar, *choices)
    lbl2 = Label(f1, text="Choose number of Teams", font=("Arial",15,"bold"))
    lbl2.place(x=180, y=330)
    popupMenu.place(x=180, y=370)

    def change_dropdown(*args):
        global no_teams
        no_teams = tkvar.get()
        print(no_teams)

    tkvar.trace('w', change_dropdown)

# group and knockout drop downs
def gandk():
    raise_frame(f4)
    background_label = Label(f4, image=image1)
    background_label.pack()

    b1 = Button(f4, text='KNOCK-OUT', command=knock1, font=("Arial", 20, "bold"), fg='white', relief=RAISED, bd=8,
                highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    b1.place(x=180, y=200)

    b2 = Button(f4, text='GROUP & \nKNOCK-OUT', command=gandk, font=("Arial", 20, "bold"), fg='white', relief=RAISED,
                bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    b2.place(x=645, y=200)

    b3 = Button(f4, text='SEEDED', font=("Arial", 20, "bold"), command=seed_group, fg='white', relief=RAISED, bd=8,
                highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    b3.place(x=180, y=530)
    b4 = Button(f4, text='UNSEEDED', font=("Arial", 20, "bold"), command=unseed_group, fg='white', relief=RAISED, bd=8,
                highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    b4.place(x=645, y=530)

    tkvar1 = StringVar(f4)

    choices1 = (8, 16)
    tkvar1.set(8)

    popupMenu1 = OptionMenu(f4, tkvar1, *choices1)
    lbl3 = Label(f4, text="Choose number of Teams", font=("Arial",15,"bold"))
    lbl3.place(x=645, y=330)
    popupMenu1.place(x=645, y=370)

    def change_dropdown1(*args):
        global no_teams1
        no_teams1 = tkvar1.get()
        print(tkvar1.get())

    tkvar1.trace('w', change_dropdown1)

# No of groups
    tkvar2 = StringVar(f4)

    choices2 = (2, 4)
    tkvar2.set(2)

    popupMenu2 = OptionMenu(f4, tkvar2, *choices2)
    lbl4 = Label(f4, text="Choose number of Groups", font=("Arial",15,"bold"))
    lbl4.place(x=645, y=430)
    popupMenu2.place(x=645, y=470)

    def change_dropdown2(*args):
        global no_teams2
        no_teams2 = tkvar2.get()
        print(tkvar2.get())

    tkvar2.trace('w', change_dropdown2)

# Knockout Buttons
b1 = Button(f1, text='KNOCK-OUT', command = knock1, font=("Arial",20,"bold"), fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b1.place(x=180, y=200)

b2 = Button(f1, text='GROUP & \nKNOCK-OUT', command = gandk, font=("Arial",20,"bold"), fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b2.place(x=645, y=200)

# FRAME 2.1.1 (UNSEEDED GROUP)

def unseed_group():
    raise_frame(f5)
    background_label = Label(f5, image=image1)
    background_label.pack()
    global entries1
    entries1 = []
    if int(no_teams1) < 10:
        for i in range(int(no_teams1)):
            label111 = Label(f5, text='Team ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110,
                                                                                                    y=150 + (60 * i))
            en = Entry(f5, bd=3, bg='white', justify=CENTER, width=25)
            en.place(x=250, y=155 + (60 * i))
            entries1.append(en)

    else:
        i = 0
        while i < 8:
            lbl103 = Label(f5, text='Team ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110,
                                                                                                  y=150 + (60 * i))
            en1 = Entry(f5, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=250, y=155 + (60 * i))
            entries1.append(en1)
            i = i + 1

        while 7 < i < 16:
            lbl104 = Label(f5, text='Team ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=610, y=150 + (
            60 * (i - 8)))
            en1 = Entry(f5, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=750, y=155 + (60 * (i - 8)))
            entries1.append(en1)
            i = i + 1

    bb5 = Button(f5, text='SUBMIT', font=("Arial", 20, "bold"), command=unseed_grp, fg='white', relief=RAISED, bd=8,
                 highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    bb5.place(x=410, y=620)
    # def hallo():
    #   print(entries[1].get())
    # button = Button(f2, text="krijg", command=hallo).place(x=500, y=400)

# FRAME 2.1.2 (SEEDED GROUP)
def seed_group():
    raise_frame(f5)
    background_label = Label(f5, image=image1)
    background_label.pack()
    global entries1
    entries1 = []
    if int(no_teams1) < 10:
        for i in range(int(no_teams1)):
            label111 = Label(f5, text='Team Rank ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110,
                                                                                                         y=150 + (
                                                                                                         60 * i))
            en = Entry(f5, bd=3, bg='white', justify=CENTER, width=25)
            en.place(x=250, y=155 + (60 * i))
            entries1.append(en)

    else:
        i = 0
        while i < 8:
            lbl103 = Label(f5, text='Team Rank ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110,
                                                                                                       y=150 + (60 * i))
            en1 = Entry(f5, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=250, y=155 + (60 * i))
            entries1.append(en1)
            i = i + 1

        while 7 < i < 16:
            lbl104 = Label(f5, text='Team Rank ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=610, y=150 + (
            60 * (i - 8)))
            en1 = Entry(f5, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=760, y=155 + (60 * (i - 8)))
            entries1.append(en1)
            i = i + 1

    bb5 = Button(f5, text='SUBMIT', font=("Arial", 20, "bold"), command=seed_grp, fg='white', relief=RAISED, bd=8,
                 highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    bb5.place(x=410, y=620)


# FRAME 2.1 (UNSEEDED)
def unseed_wind():
    raise_frame(f2)
    background_label = Label(f2, image=image1)
    background_label.pack()
    global entries
    entries = []
    if int(no_teams) < 10:
        for i in range(int(no_teams)):
            label111 = Label(f2, text='Team ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110, y=150 + (60*i))
            en = Entry(f2, bd=3, bg='white', justify=CENTER, width=25)
            en.place(x=250, y=155 + (60*i))
            entries.append(en)

    else:
        i=0
        while i < 8:
            lbl103 = Label(f2, text='Team ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110, y=150 + (60 * i))
            en1 = Entry(f2, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=250, y=155 + (60*i))
            entries.append(en1)
            i = i + 1

        while 7 < i < 16:
            lbl104 = Label(f2, text='Team ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=610, y=150 + (60 * (i - 8)))
            en1 = Entry(f2, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=750, y=155 + (60*(i-8)))
            entries.append(en1)
            i = i + 1

    bb5 = Button(f2, text='SUBMIT', font=("Arial",20,"bold"), command=unseed_knock, fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    bb5.place(x=410, y=620)
    #def hallo():
     #   print(entries[1].get())
    #button = Button(f2, text="krijg", command=hallo).place(x=500, y=400)

# FRAME 2.2 (Seeded)

def seed_wind():
    raise_frame(f2)
    background_label = Label(f2, image=image1)
    background_label.pack()
    global entries
    entries = []
    if int(no_teams) < 10:
        for i in range(int(no_teams)):
            label111 = Label(f2, text='Team Rank ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110, y=150 + (60*i))
            en = Entry(f2, bd=3, bg='white', justify=CENTER, width=25)
            en.place(x=250, y=155 + (60*i))
            entries.append(en)

    else:
        i=0
        while i < 8:
            lbl103 = Label(f2, text='Team Rank ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=110, y=150 + (60 * i))
            en1 = Entry(f2, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=250, y=155 + (60*i))
            entries.append(en1)
            i = i + 1

        while 7 < i < 16:
            lbl104 = Label(f2, text='Team Rank ' + str(i + 1) + ':', font=("Arial", 15, "bold")).place(x=610, y=150 + (60 * (i - 8)))
            en1 = Entry(f2, bd=3, bg='white', justify=CENTER, width=25)
            en1.place(x=760, y=155 + (60*(i-8)))
            entries.append(en1)
            i = i + 1

    bb5 = Button(f2, text='SUBMIT', font=("Arial",20,"bold"), command=seed_knock, fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
    bb5.place(x=410, y=620)

# FRAME 3.2 Seed Knock

def seed_knock():
    raise_frame(f3)
    background_label = Label(f3, image=image1)
    background_label.pack()
    if int(no_teams) == 4:
        teamA = Button(f3, text=entries[0].get() + '(1)', font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=70, y=130)
        teamB = Button(f3, text=entries[2].get() + '(3)', font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=70, y=530)
        teamC = Button(f3, text=entries[1].get() + '(2)', font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=780, y=130)
        teamD = Button(f3, text=entries[3].get() + '(4)', font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=780, y=530)
        teamAB = Button(f3, font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=290, y=330)
        teamCD = Button(f3, font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=570, y=330)

    if int(no_teams) == 8:
        teamA = Button(f3, text=entries[0].get() + '(1)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=130)
        teamB = Button(f3, text=entries[1].get() + '(2)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=130)
        teamC = Button(f3, text=entries[4].get() + '(5)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=280)
        teamD = Button(f3, text=entries[5].get() + '(6)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=280)
        teamE = Button(f3, text=entries[2].get() + '(3)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=430)
        teamF = Button(f3, text=entries[3].get() + '(4)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=430)
        teamG = Button(f3, text=entries[6].get() + '(7)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=580)
        teamH = Button(f3, text=entries[7].get() + '(8)', font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=580)
        teamAB = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=250, y=205)
        teamCD = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=250, y=505)
        teamEf = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=680, y=205)
        teamGH = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=680, y=505)
        teamF1 = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=360, y=350)
        teamF2 = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=570, y=350)

    if int(no_teams) == 16:
        teamA = Button(f3, text=entries[0].get() + '(1)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=130)
        teamB = Button(f3, text=entries[11].get() + '(12)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=130)
        teamC = Button(f3, text=entries[14].get() + '(15)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=205)
        teamD = Button(f3, text=entries[2].get() + '(3)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=205)
        teamE = Button(f3, text=entries[5].get() + '(6)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=280)
        teamF = Button(f3, text=entries[8].get() + '(9)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=280)
        teamG = Button(f3, text=entries[9].get() + '(10)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=355)
        teamH = Button(f3, text=entries[6].get() + '(7)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=355)
        teamI = Button(f3, text=entries[4].get() + '(5)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=430)
        teamJ = Button(f3, text=entries[10].get() + '(11)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=430)
        teamK = Button(f3, text=entries[13].get() + '(14)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=505)
        teamL = Button(f3, text=entries[7].get() + '(8)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=505)
        teamM = Button(f3, text=entries[3].get() + '(4)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=580)
        teamN = Button(f3, text=entries[1].get() + '(2)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=580)
        teamO = Button(f3, text=entries[12].get() + '(13)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=655)
        teamP = Button(f3, text=entries[15].get() + '(16)', font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=655)
        teamQ1 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=167)
        teamQ2 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=167)
        teamQ3 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=317)
        teamQ4 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=317)
        teamQ5 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=467)
        teamQ6 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=467)
        teamQ7 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=617)
        teamQ8 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=617)
        teamS1 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=280, y=242)
        teamS2 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=670, y=242)
        teamS3 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=280, y=542)
        teamS4 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=670, y=542)
        teamFF1 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=2, width=10).place(x=380, y=372)
        teamFF2 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=2, width=10).place(x=565, y=372)


# FRAME 3.1 Unseeded knock
def unseed_knock():
    raise_frame(f3)
    background_label = Label(f3, image=image1)
    background_label.pack()
    if int(no_teams) == 4:
        teamA = Button(f3, text=entries[0].get(), font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=70, y=130)
        teamB = Button(f3, text=entries[1].get(), font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=70, y=530)
        teamC = Button(f3, text=entries[2].get(), font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=780, y=130)
        teamD = Button(f3, text=entries[3].get(), font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=780, y=530)
        teamAB = Button(f3, font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=290, y=330)
        teamCD = Button(f3, font=("Arial",25,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=10).place(x=570, y=330)

    if int(no_teams) == 8:
        teamA = Button(f3, text=entries[0].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=130)
        teamB = Button(f3, text=entries[1].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=130)
        teamC = Button(f3, text=entries[2].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=280)
        teamD = Button(f3, text=entries[3].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=280)
        teamE = Button(f3, text=entries[4].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=430)
        teamF = Button(f3, text=entries[5].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=430)
        teamG = Button(f3, text=entries[6].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=50, y=580)
        teamH = Button(f3, text=entries[7].get(), font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=880, y=580)
        teamAB = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=250, y=205)
        teamCD = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=250, y=505)
        teamEf = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=680, y=205)
        teamGH = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=680, y=505)
        teamF1 = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=360, y=350)
        teamF2 = Button(f3, font=("Arial",20,"bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=570, y=350)

    if int(no_teams) == 16:
        teamA = Button(f3, text=entries[0].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=130)
        teamB = Button(f3, text=entries[1].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=130)
        teamC = Button(f3, text=entries[2].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=205)
        teamD = Button(f3, text=entries[3].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=205)
        teamE = Button(f3, text=entries[4].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=280)
        teamF = Button(f3, text=entries[5].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=280)
        teamG = Button(f3, text=entries[6].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=355)
        teamH = Button(f3, text=entries[7].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=355)
        teamI = Button(f3, text=entries[8].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=430)
        teamJ = Button(f3, text=entries[9].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=430)
        teamK = Button(f3, text=entries[10].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=505)
        teamL = Button(f3, text=entries[11].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=505)
        teamM = Button(f3, text=entries[12].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=580)
        teamN = Button(f3, text=entries[13].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=580)
        teamO = Button(f3, text=entries[14].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=20, y=655)
        teamP = Button(f3, text=entries[15].get(), font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=940, y=655)
        teamQ1 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=167)
        teamQ2 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=167)
        teamQ3 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=317)
        teamQ4 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=317)
        teamQ5 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=467)
        teamQ6 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=467)
        teamQ7 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=150, y=617)
        teamQ8 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=800, y=617)
        teamS1 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=280, y=242)
        teamS2 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=670, y=242)
        teamS3 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=280, y=542)
        teamS4 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=1, width=8).place(x=670, y=542)
        teamFF1 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=2, width=10).place(x=380, y=372)
        teamFF2 = Button(f3, font=("Arial", 15, "bold"), fg='white', relief=RAISED, state=DISABLED, bd=4, highlightbackground='white', activebackground='white', bg='white', height=2, width=10).place(x=565, y=372)

# Seed Buttons

def unseed_grp():
    raise_frame(f6)
    background_label = Label(f6, image=image1)
    background_label.pack()
    if int(no_teams1) == 8:
        heading = Label(f6, bg='chartreuse3', text='GROUP 1', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                        relief=GROOVE, width=15).place(x=170, y=110)
        heading = Label(f6, bg='chartreuse3', text='GROUP 2', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                        relief=GROOVE, width=15).place(x=710, y=110)

        heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                        relief=RIDGE, width=8).place(x=30, y=190)
        heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=130, y=190)
        heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=230, y=190)
        heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=330, y=190)
        heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=430, y=190)

        team1 = Label(f6, bg='chartreuse3', text=entries1[0].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=30, y=260)
        team1 = Label(f6, bg='chartreuse3', text=entries1[2].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=30, y=330)
        team1 = Label(f6, bg='chartreuse3', text=entries1[4].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=30, y=400)
        team1 = Label(f6, bg='chartreuse3', text=entries1[6].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=30, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=470)

        heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                        relief=RIDGE, width=8).place(x=570, y=190)
        heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=670, y=190)
        heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=770, y=190)
        heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=870, y=190)
        heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=970, y=190)

        team1 = Label(f6, bg='chartreuse3', text=entries1[1].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=570, y=260)
        team1 = Label(f6, bg='chartreuse3', text=entries1[3].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=570, y=330)
        team1 = Label(f6, bg='chartreuse3', text=entries1[5].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=570, y=400)
        team1 = Label(f6, bg='chartreuse3', text=entries1[7].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2,
                      relief=SUNKEN, width=8).place(x=570, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=470)

    if int(no_teams1) == 16:
        if int(no_teams2) == 2:
            heading = Label(f6, bg='chartreuse3', text='GROUP 1', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=170, y=110)
            heading = Label(f6, bg='chartreuse3', text='GROUP 2', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=710, y=110)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=30, y=190)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=130, y=190)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=230, y=190)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=330, y=190)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=430, y=190)

            team1 = Label(f6, bg='chartreuse3', text=entries1[0].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[2].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[4].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=360)
            team1 = Label(f6, bg='chartreuse3', text=entries1[6].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=410)
            team1 = Label(f6, bg='chartreuse3', text=entries1[8].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=460)
            team1 = Label(f6, bg='chartreuse3', text=entries1[10].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=510)
            team1 = Label(f6, bg='chartreuse3', text=entries1[12].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=560)
            team1 = Label(f6, bg='chartreuse3', text=entries1[14].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=610)

            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=610)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=570, y=190)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=670, y=190)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=770, y=190)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=870, y=190)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=970, y=190)

            team1 = Label(f6, bg='chartreuse3', text=entries1[1].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[3].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[5].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=360)
            team1 = Label(f6, bg='chartreuse3', text=entries1[7].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=410)
            team1 = Label(f6, bg='chartreuse3', text=entries1[9].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=460)
            team1 = Label(f6, bg='chartreuse3', text=entries1[11].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=510)
            team1 = Label(f6, bg='chartreuse3', text=entries1[13].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=560)
            team1 = Label(f6, bg='chartreuse3', text=entries1[15].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=610)

        if int(no_teams2) == 4:
            heading = Label(f6, bg='chartreuse3', text='GROUP 1', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=170, y=90)
            heading = Label(f6, bg='chartreuse3', text='GROUP 2', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=710, y=90)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=30, y=160)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=130, y=160)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=230, y=160)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=330, y=160)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=430, y=160)

            team1 = Label(f6, bg='chartreuse3', text=entries1[0].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=210)
            team1 = Label(f6, bg='chartreuse3', text=entries1[2].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[4].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[6].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN, width=8).place(x=130, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=360)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=570, y=160)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=670, y=160)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=770, y=160)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=870, y=160)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=970, y=160)

            team1 = Label(f6, bg='chartreuse3', text=entries1[1].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=210)
            team1 = Label(f6, bg='chartreuse3', text=entries1[3].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[5].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[7].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=360)




            heading = Label(f6, bg='chartreuse3', text='GROUP 3', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=170, y=410)
            heading = Label(f6, bg='chartreuse3', text='GROUP 4', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=710, y=410)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=30, y=480)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=130, y=480)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=230, y=480)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=330, y=480)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=430, y=480)

            team1 = Label(f6, bg='chartreuse3', text=entries1[8].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=530)
            team1 = Label(f6, bg='chartreuse3', text=entries1[10].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=580)
            team1 = Label(f6, bg='chartreuse3', text=entries1[12].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=630)
            team1 = Label(f6, bg='chartreuse3', text=entries1[14].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=680)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=570, y=480)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=670, y=480)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=770, y=480)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=870, y=480)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=970, y=480)

            team1 = Label(f6, bg='chartreuse3', text=entries1[9].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=530)
            team1 = Label(f6, bg='chartreuse3', text=entries1[11].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=580)
            team1 = Label(f6, bg='chartreuse3', text=entries1[13].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=630)
            team1 = Label(f6, bg='chartreuse3', text=entries1[15].get(), bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=680)



def seed_grp():
    raise_frame(f6)
    background_label = Label(f6, image=image1)
    background_label.pack()
    if int(no_teams1) == 8:
        heading = Label(f6, bg='chartreuse3', text='GROUP 1', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                        relief=GROOVE, width=15).place(x=170, y=110)
        heading = Label(f6, bg='chartreuse3', text='GROUP 2', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                        relief=GROOVE, width=15).place(x=710, y=110)

        heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                        relief=RIDGE, width=8).place(x=30, y=190)
        heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=130, y=190)
        heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=230, y=190)
        heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=330, y=190)
        heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=430, y=190)

        team1 = Label(f6, bg='chartreuse3', text=entries1[0].get() + '(1)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=30, y=260)
        team1 = Label(f6, bg='chartreuse3', text=entries1[3].get() + '(4)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=30, y=330)
        team1 = Label(f6, bg='chartreuse3', text=entries1[4].get() + '(5)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=30, y=400)
        team1 = Label(f6, bg='chartreuse3', text=entries1[7].get() + '(8)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=30, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=130, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=230, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=330, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=430, y=470)

        heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                        relief=RIDGE, width=8).place(x=570, y=190)
        heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=670, y=190)
        heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=770, y=190)
        heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=870, y=190)
        heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                         relief=RIDGE, width=8).place(x=970, y=190)

        team1 = Label(f6, bg='chartreuse3', text=entries1[1].get() + '(2)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=570, y=260)
        team1 = Label(f6, bg='chartreuse3', text=entries1[2].get() + '(3)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=570, y=330)
        team1 = Label(f6, bg='chartreuse3', text=entries1[5].get() + '(6)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=570, y=400)
        team1 = Label(f6, bg='chartreuse3', text=entries1[6].get() + '(7)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                      height=2,
                      relief=SUNKEN, width=8).place(x=570, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=260)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=330)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=400)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=670, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=770, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=870, y=470)
        team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                      width=8).place(x=970, y=470)

    if int(no_teams1) == 16:
        if int(no_teams2) == 2:
            heading = Label(f6, bg='chartreuse3', text='GROUP 1', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=170, y=110)
            heading = Label(f6, bg='chartreuse3', text='GROUP 2', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=710, y=110)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=30, y=190)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=130, y=190)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=230, y=190)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=330, y=190)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=430, y=190)

            team1 = Label(f6, bg='chartreuse3', text=entries1[0].get() + '(1)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[2].get() + '(3)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[4].get() + '(5)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=360)
            team1 = Label(f6, bg='chartreuse3', text=entries1[6].get() + '(7)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=410)
            team1 = Label(f6, bg='chartreuse3', text=entries1[8].get() + '(9)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=460)
            team1 = Label(f6, bg='chartreuse3', text=entries1[10].get() + '(11)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=510)
            team1 = Label(f6, bg='chartreuse3', text=entries1[12].get() + '(13)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=560)
            team1 = Label(f6, bg='chartreuse3', text=entries1[14].get() + '(15)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=610)

            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=610)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=570, y=190)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=670, y=190)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=770, y=190)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=870, y=190)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=970, y=190)

            team1 = Label(f6, bg='chartreuse3', text=entries1[1].get() + '(2)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[3].get() + '(4)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[5].get() + '(6)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=360)
            team1 = Label(f6, bg='chartreuse3', text=entries1[7].get() + '(8)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=410)
            team1 = Label(f6, bg='chartreuse3', text=entries1[9].get() + '(10)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=460)
            team1 = Label(f6, bg='chartreuse3', text=entries1[11].get() + '(12)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=510)
            team1 = Label(f6, bg='chartreuse3', text=entries1[13].get() + '(14)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=560)
            team1 = Label(f6, bg='chartreuse3', text=entries1[15].get() + '(16)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=410)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=460)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=510)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=560)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=610)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=610)

        if int(no_teams2) == 4:
            heading = Label(f6, bg='chartreuse3', text='GROUP 1', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=170, y=90)
            heading = Label(f6, bg='chartreuse3', text='GROUP 2', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=710, y=90)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=30, y=160)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=130, y=160)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=230, y=160)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=330, y=160)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=430, y=160)

            team1 = Label(f6, bg='chartreuse3', text=entries1[0].get() + '(1)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=210)
            team1 = Label(f6, bg='chartreuse3', text=entries1[7].get() + '(8)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[8].get() + '(9)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[15].get() + '(16)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=360)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=570, y=160)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=670, y=160)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=770, y=160)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=870, y=160)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=970, y=160)

            team1 = Label(f6, bg='chartreuse3', text=entries1[1].get() + '(2)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=210)
            team1 = Label(f6, bg='chartreuse3', text=entries1[6].get() + '(7)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=260)
            team1 = Label(f6, bg='chartreuse3', text=entries1[9].get() + '(10)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=310)
            team1 = Label(f6, bg='chartreuse3', text=entries1[14].get() + '(15)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=210)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=260)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=310)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=360)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=360)

            heading = Label(f6, bg='chartreuse3', text='GROUP 3', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=170, y=410)
            heading = Label(f6, bg='chartreuse3', text='GROUP 4', bd=5, font=("Arial", 15, "bold"), fg='red', height=2,
                            relief=GROOVE, width=15).place(x=710, y=410)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=30, y=480)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=130, y=480)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=230, y=480)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=330, y=480)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=430, y=480)

            team1 = Label(f6, bg='chartreuse3', text=entries1[2].get() + '(3)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=530)
            team1 = Label(f6, bg='chartreuse3', text=entries1[5].get() + '(6)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=580)
            team1 = Label(f6, bg='chartreuse3', text=entries1[10].get() + '(11)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=630)
            team1 = Label(f6, bg='chartreuse3', text=entries1[13].get() + '(14)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=30, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=130, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=230, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=330, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=430, y=680)

            heading = Label(f6, bg='chartreuse3', text='TEAM', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                            relief=RIDGE, width=8).place(x=570, y=480)
            heading1 = Label(f6, bg='chartreuse3', text='PLAYED', bd=5, font=("Arial", 10, "bold"), fg='black',
                             height=2,
                             relief=RIDGE, width=8).place(x=670, y=480)
            heading2 = Label(f6, bg='chartreuse3', text='WON', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=770, y=480)
            heading3 = Label(f6, bg='chartreuse3', text='DRAWN', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=870, y=480)
            heading4 = Label(f6, bg='chartreuse3', text='LOST', bd=5, font=("Arial", 10, "bold"), fg='black', height=2,
                             relief=RIDGE, width=8).place(x=970, y=480)

            team1 = Label(f6, bg='chartreuse3', text=entries1[3].get() + '(4)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=530)
            team1 = Label(f6, bg='chartreuse3', text=entries1[4].get() + '(5)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=580)
            team1 = Label(f6, bg='chartreuse3', text=entries1[11].get() + '(12)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=630)
            team1 = Label(f6, bg='chartreuse3', text=entries1[12].get() + '(13)', bd=1, font=("Arial", 10, "bold"), fg='blue4',
                          height=2,
                          relief=SUNKEN, width=8).place(x=570, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=530)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=580)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=630)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=670, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=770, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=870, y=680)
            team1 = Label(f6, bg='white', bd=1, font=("Arial", 10, "bold"), fg='blue4', height=2, relief=SUNKEN,
                          width=8).place(x=970, y=680)


b3 = Button(f1, text='SEEDED', font=("Arial",20,"bold"), command=seed_wind, fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b3.place(x=180, y=530)
b4 = Button(f1, text='UNSEEDED', font=("Arial",20,"bold"), command= unseed_wind, fg='white', relief=RAISED, bd=8, highlightbackground='white', activebackground='white', bg='green', height=2, width=13)
b4.place(x=645, y=530)


raise_frame(f1)
top.mainloop()