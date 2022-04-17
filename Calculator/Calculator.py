from tkinter import *
import tkinter.messagebox as Tm

root = Tk()

root.title("SGTech")

root.geometry("440x640")
root.maxsize(440, 640)


def AddDigit(event):
    Number = event.widget.cget("text")
    Value.insert(END, Number)

def ShowResult():
    try:
        Result = eval(Value.get())

        Value.delete(0, END)
        Value.insert(END, Result)
    except Exception as e:
        Tm.showerror("SGTech", str(e))


def SNC(event):
    Symbol = event.widget.cget("text")

    if Symbol == "X2":
        TextValue = int(Value.get())
        TextValue = TextValue * TextValue

        Value.delete(0, END)
        Value.insert(END, str(TextValue))
    else:
        TextValue = int(Value.get())
        TextValue = TextValue * TextValue * TextValue

        Value.delete(0, END)
        Value.insert(END, str(TextValue))


NumValue = StringVar()

Value = Entry(root, textvariable=NumValue, justify=RIGHT, font="Comicsanse 40 normal")
Value.pack(fill=X, pady=7, padx=11)

Num = 1

CalFrame1 = Frame(root)
CalFrame1.pack(fill=X, anchor=N)

for i in range(3):
    B1 = Button(CalFrame1, text=Num, font="Comicsanse 40 normal", width=3)
    B1.bind("<ButtonRelease-1>", AddDigit)
    B1.pack(side=LEFT)
    Num += 1

Plus = Button(CalFrame1, text="+", font="Comicsanse 40 normal", width=4)
Plus.bind("<ButtonRelease-1>", AddDigit)
Plus.pack(side=LEFT)

CalFrame2 = Frame(root)
CalFrame2.pack(fill=X, anchor=N)

for i in range(3):
    B2 = Button(CalFrame2, text=Num, font="Comicsanse 40 normal", width=3)
    B2.bind("<ButtonRelease-1>", AddDigit)
    B2.pack(side=LEFT)
    Num += 1

Minus = Button(CalFrame2, text="-", font="Comicsanse 40 normal", width=4)
Minus.bind("<ButtonRelease-1>", AddDigit)
Minus.pack(side=LEFT)

CalFrame3 = Frame(root)
CalFrame3.pack(fill=X, anchor=N)

for i in range(3):
    B3 = Button(CalFrame3, text=Num, font="Comicsanse 40 normal", width=3)
    B3.bind("<ButtonRelease-1>", AddDigit)
    B3.pack(side=LEFT)
    Num += 1

Divide = Button(CalFrame3, text="/", font="Comicsanse 40 normal", width=4)
Divide.bind("<ButtonRelease-1>", AddDigit)
Divide.pack(side=LEFT)

CalFrame4 = Frame(root)
CalFrame4.pack(fill=X, anchor=N)

L1 = ['0', '.', '*']

for i in range(3):
    BO = Button(CalFrame4, text=L1[i], font="Comicsanse 40 normal", width=3)
    BO.bind("<ButtonRelease-1>", AddDigit)
    BO.pack(side=LEFT)
    Num += 1

Clear = Button(CalFrame4, text='C', font="Comicsanse 40 normal", width=4,
               command=lambda: Value.delete(0, END))
Clear.pack(side=LEFT)

CalFrame5 = Frame(root)
CalFrame5.pack(fill=X, anchor=N)

S = Button(CalFrame5, text='X2', font="Comicsanse 40 normal", width=3)
S.bind("<ButtonRelease-1>", SNC)
S.pack(side=LEFT)

Cub = Button(CalFrame5, text='X3', font="Comicsanse 40 normal", width=3)
Cub.bind("<ButtonRelease-1>", SNC)
Cub.pack(side=LEFT)

Equal = Button(CalFrame5, text='=', font="Comicsanse 40 normal", width=3, command=ShowResult)
Equal.pack(side=LEFT)

root.mainloop()
