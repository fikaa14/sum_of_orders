import tkinter
import math
from tkinter import messagebox

def RedoviKolone1(brelem):
    kolone=math.ceil(math.sqrt(brelem/2))
    redovi=2*kolone

    return redovi, kolone

def Cancel():
    for i in nizCheckButtona:
        i.set(0)

def Order():
    suma = 0
    for i, button in enumerate(nizCheckButtona):
        if button.get():
            suma = suma + float(lista[i][-5:-1])
    suma = format(suma, ".2f")
    tkinter.messagebox.showinfo("Message","Your order is successful. The total is: " + suma)

window = tkinter.Tk()

lista = ["Pizza(3.50)", "Ham sandwich(2.00)", "Burger(3.50)", "Cesar salad(4.00)", "Pasta(5.50)","Omellete(3.00)", "Lasagne(5.00)", "Pancakes(2.50)",]

window.title("Menu")

elementi = len(lista) #dobijam broj elemenata liste

redovi, kolone = RedoviKolone1(elementi) #funkcija pomocu koje od broja elemenata dobijam broj redova i kolona

nizCheckButtona = []
for i, item in enumerate(lista):
    red = i%redovi
    kolona = i//redovi
    checkButton = tkinter.IntVar() #od check buttona pravim varijable koje cu dodati u niz CheckButtona
    check = tkinter.Checkbutton(window, text=item, variable=checkButton).grid(row=red, column=kolona,sticky='w')
    nizCheckButtona.append(checkButton)

frame = tkinter.Frame(window)
frame.grid(row=redovi, columnspan=kolone)

frame1 = tkinter.Frame(frame)
frame1.pack(side = "left")
order = tkinter.Button(frame1, text="Order", command=Order).pack()
#na ovaj nacin bi trebali da su button order i button cancel uvijek na dnu i u sredini
frame2 = tkinter.Frame(frame)
frame2.pack(side= "right")
cancel = tkinter.Button(frame2, text="Cacel", command= Cancel).pack()

window.mainloop()
