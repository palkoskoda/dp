#Simple To Do List GUI by Christian Thompson (@tokyoedtech)
#Python 2.7
#Part 2: Window Improvements and Updating the Listbox
from tkinter import *
from tkinter import ttk
import random

def doNothing():
    print("ok")

#Create root window
root = Tk()

# %% *****strana1****
def open():
    novySuborAdresa = filedialog.askopenfile(title="vloz subor", filetypes=(("servo trace","*.ST1"),("všetky typy","*.*")))
    novySuborLabel = Label(root, text=novySuborAdresa).pack()
    print(novySuborAdresa) 
    
nb = ttk.Notebook(root)
#nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

page1=ttk.Frame(nb)
nb.add(page1, text="Vložiť nový záznam")
nb.pack(expand=1, fill="both")
    
#frm = Frame(root)
#frm.pack(side=tk.LEFT, padx=10)

novyNazovText = Label(page1, text = "Názov")
noveHadzanieText = Label(page1, text = "Hádzanie")
noveHodinyText = Label(page1, text = "Hodiny")
novaPoznamkaText =Label(page1, text = "Poznámka")

novyNazovText.place(x=15,y=50)
noveHadzanieText.place(x=15,y=100)
noveHodinyText.place(x=15,y=150)
novaPoznamkaText.place(x=15,y=200)

novyNazov = StringVar()
noveHadzanie1=DoubleVar()
noveHadzanie2=DoubleVar()
noveHodiny=IntVar()
novaPoznamka=StringVar()

novyNazovEntry = Entry(page1, textvariable = novyNazov, width = "30")
noveHadzanie1Entry=Entry(page1, textvariable = novyNazov, width = "10")
noveHadzanie2Entry=Entry(page1, textvariable = novyNazov, width = "10")
noveHodinyEntry=Entry(page1, textvariable = novyNazov, width = "30")
novaPoznamkaEntry=Entry(page1, textvariable = novyNazov, width = "30")


novyNazovEntry.place(x=15,y=70)
noveHadzanie1Entry.place(x=15,y=120)
noveHadzanie2Entry.place(x=135,y=120)
noveHodinyEntry.place(x=15,y=170)
novaPoznamkaEntry.place(x=15,y=220)

tNovySubor = Button(page1, text="Vložiť súbor", command=open)
tNovySubor.place(x=15,y=250)


# %% *****strana2****

page2=ttk.Frame(nb)
nb.add(page2, text="Prehľad")
nb.pack()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project", command=doNothing)
subMenu.add_command(label="new asd", command=doNothing)
subMenu.add_command(label="este daco", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="old project", command=doNothing)
subMenu.add_command(label="old asd", command=doNothing)
subMenu.add_command(label="exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="Obnoviť", command=doNothing)
editMenu.add_command(label="new asd", command=doNothing)
editMenu.add_command(label="este daco", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="old project", command=doNothing)
editMenu.add_command(label="old asd", command=doNothing)
editMenu.add_command(label="exit", command=doNothing)


# ***** toolbar *****

#toolbar = Frame(root, bg="white")
# =============================================================================
# tObrazovka1 = Button(toolbar, text="Prehľad", command=doNothing, width=10)
# tObrazovka1.pack(side=LEFT, padx=2, pady=2 )
# tObrazovka2 = Button(toolbar, text="Stroj", command=doNothing, width=10)
# tObrazovka2.pack(side=LEFT, padx=2, pady=2 )
# tObrazovka3 = Button(toolbar, text="Algorytmy", command=doNothing, width=10)
# tObrazovka3.pack(side=LEFT, padx=2, pady=2 )
# tObrazovka4 = Button(toolbar, text="Vložiť", command=doNothing, width=10)
# tObrazovka4.pack(side=LEFT, padx=2, pady=2 )
# 
# toolbar.pack(side=TOP, fill=X)
# 
# frm = Frame(root)
# frm.pack(padx=10,pady=10)
# =============================================================================


tv = ttk.Treeview(page2, column=(1,2,3,4,5,6,7,8,9), show="headings", height="5")


tv.heading(1, text="Názov")
tv.heading(2, text="Frekvenčná charakteristika")
tv.heading(3, text="Hádzanie")
tv.heading(4, text="hodiny")
tv.heading(5, text="A1")
tv.heading(6, text="A2")
tv.heading(7, text="A3")
tv.heading(8, text="A4")
tv.heading(9, text="poznámka")

riadok1= tv.insert("",1,text = "prvy riadok", values = ("B1","C1"))
tv.insert(riadok1,"end",text = "A1.1", values = ("B1.1","C1.1"))
tv.pack()

tAktualizuj = Button(page2, text="Aktualizuj", command=open)
tAktualizuj.pack(side=TOP)

# %% ***** strana3 *****
page3=ttk.Frame(nb)
nb.add(page3, text="Hodnotenie strojov")
nb.pack()

nazovStrojaText = Label(page3, text = "Názov stroja:")
jzText = Label(page3, text = "Jednosmerná zložka: ")
a1Text = Label(page3, text = "A1:")
a2Text = Label(page3, text = "A2:")
a3Text =Label(page3, text = "A3:")

nazovStrojaText.place(x=20,y=50)
jzText.place(x=250,y=50)
a1Text.place(x=250,y=100)
a2Text.place(x=250,y=150)
a3Text.place(x=250,y=200)


# %% ***** strana3 *****
page4=ttk.Frame(nb)
nb.add(page4, text="Posudzovacie algoritmy")
nb.pack()

a1Text = Label(page4, text = "A1:")
a2Text = Label(page4, text = "A2:")
a3Text =Label(page4, text = "A3:")

a1Text.place(x=20,y=50)
a2Text.place(x=20,y=100)
a3Text.place(x=20,y=150)











# %% ***** status *****

status = Label(root, text="pripravujem sa...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)






root.title("Servo Trace analíza")
root.geometry("950x500")




# =============================================================================
# class BuckysButtons:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         
#         self.printButton = Button(frame, text="Print Message", command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#         
#         self.quitButton = Button(frame, text="quit", command=frame.quit)
#         self.quitButton.pack(side=LEFT)
# 
#     def printMessage(self):
#         print("fungovalo to :D")
#         
# =============================================================================
                

#b= BuckysButtons(root)




#def leftClick(event):
#    print("Ľavo")
    
#def middleClick(event):
#    print("Stred")

#def rightClick(event):
 #   print("Pravo")

#frame = Frame(root, width=300, height=250)
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)

#frame.pack()

#def printName(event):
#    print("Ahoj, volam sa pavuk")
    
#button_1=Button(root, text="vypíš moje meno")
#button_1.bind("<Button-1>", printName)
#button_1.pack()








#label_1 = Label(root, text="Tvoje meno")
#label_2 = Label(root, text="heslo")

#entry_1 = Entry(root)
#entry_2 = Entry(root)

#label_1.grid(row=0, sticky=E)
#label_2.grid(row=1, sticky=E)

#entry_1.grid(row=0, column=1)
#entry_2.grid(row=1, column=1)

#c= Checkbutton(root, text="Zapamätať prihlásenie")
#c.grid(columnspan=2)

#three = Label(root, text="tri", bg="blue", fg="white")
#three.pack(side=LEFT, fill=Y)


#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)

#button1=Button(topFrame, text="Button 1 ", fg="red")
#button2=Button(topFrame, text="Button 2 ", fg="green")
#button3=Button(topFrame, text="Button 3 ", fg="blue")
#button4=Button(topFrame, text="Button 4 ", fg="purple")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=BOTTOM)

root.mainloop()