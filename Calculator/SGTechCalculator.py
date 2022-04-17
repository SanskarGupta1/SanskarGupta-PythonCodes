from tkinter import *
import tkinter.messagebox as Tm

SGTech = Tk()

SGTech.geometry("600x730")
SGTech.title("SGTech.ico")

def InsData(event):
    Num = event.widget.cget("text")
    OutPutWin.insert(END, Num)

    Manager()


def OpHandler(event):
    Op = event.widget.cget("text")

    Manager()

    if Op == 'X2':
        Dta = OutPutWin.get()
        OutPutWin.delete("0", END)

        try:
            Dta = eval(Dta)
            Sq = Dta * Dta

            OutPutWin.insert(END, Sq)
        except EXCEPTION as e:
            e = str(e)
            Tm.showerror("SGTech", e)
    elif Op == 'X3':
        Dta = OutPutWin.get()
        OutPutWin.delete("0", END)

        try:
            Dta = eval(Dta)
            Sq = Dta * Dta * Dta

            OutPutWin.insert(END, Sq)
        except EXCEPTION as e:
            e = str(e)
            Tm.showerror("SGTech", e)
    elif Op == '+' or Op == '-' or Op == '/' or Op == '*':
        OutPutWin.insert(END, Op)
    elif Op == '=':
        GetDone = eval(OutPutWin.get())
        OutPutWin.delete("0", END)
        OutPutWin.insert(END, GetDone)

    else:
        OutPutWin.insert(END, Op)


def Clear(event):
    OutPutWin.delete("0", END)


def Manager():
    if len(OutPutWin.get()) > 14:
        Tm.showwarning("SGTech", "Warning! Please clear the numbers. The numbers have exceeded the safe limit of\n"
                                 "14 numbers so if you will do calculations now then your computer may\n"
                                 " crash sir/mam.")


Data = StringVar()

OutPutWin = Entry(SGTech, textvariable=Data,
                  font="Comicsanse 40 bold", justify=RIGHT)
OutPutWin.pack(fill=X, padx=7, pady=11)

CalFrame = Frame(SGTech, bg='light gray')
CalFrame.pack(side=LEFT, fill=Y)

Number = 1

CalFrame1 = Frame(CalFrame, bg='light gray')
CalFrame1.pack(fill=X, anchor=NW)

for i in range(3):
    B1 = Button(CalFrame1, text=f"{Number}", width=5,
                height=2, font="Comicsanse 31 bold")
    B1.pack(side=LEFT, anchor=NW, ipadx=7.9)
    B1.bind("<ButtonRelease-1>", InsData)

    Number += 1

Plus = Button(CalFrame1, text='+', width=5,
              height=2, font="Comicsanse 31 bold")
Plus.pack(side=LEFT, anchor=NW, ipadx=5)
Plus.bind("<ButtonRelease-1>", OpHandler)

CalFrame2 = Frame(CalFrame, bg='light gray')
CalFrame2.pack(fill=X, anchor=NW)

for i in range(3):
    B2 = Button(CalFrame2, text=f"{Number}", width=5,
                height=2, font="Comicsanse 31 bold")
    B2.bind("<ButtonRelease-1>", InsData)
    B2.pack(side=LEFT, anchor=NW, ipadx=7.9)

    Number += 1

Minus = Button(CalFrame2, text='-', width=5,
               height=2, font="Comicsanse 31 bold")
Minus.pack(side=LEFT, anchor=NW, ipadx=5)
Minus.bind("<ButtonRelease-1>", OpHandler)

CalFrame3 = Frame(CalFrame, bg='light gray')
CalFrame3.pack(fill=X, anchor=NW)

for i in range(3):
    B3 = Button(CalFrame3, text=f"{Number}", width=5,
                height=2, font="Comicsanse 31 bold")
    B3.pack(side=LEFT, anchor=NW, ipadx=7.9)
    B3.bind("<ButtonRelease-1>", InsData)

    Number += 1

Mult = Button(CalFrame3, text='*', width=5,
              height=2, font="Comicsanse 31 bold")
Mult.pack(side=LEFT, anchor=NW, ipadx=5)
Mult.bind("<ButtonRelease-1>", OpHandler)

Operations = [".", "0", "X2", "X3"]

CalFrame4 = Frame(CalFrame, bg='light gray')
CalFrame4.pack(fill=X, anchor=NW)

for i in range(len(Operations)):
    Operation = Button(CalFrame4, text=f"{Operations[i]}",
                       width=5, height=2, font="Comicsanse 31 bold")
    Operation.pack(side=LEFT, anchor=NW, ipadx=7.9)
    Operation.bind("<ButtonRelease-1>", OpHandler)

Divide = Button(CalFrame, text="/", width=5,
                height=2, font="Comicsanse 31 bold")
Divide.pack(side=LEFT, anchor=NW, ipadx=7.9)
Divide.bind("<ButtonRelease-1>", OpHandler)

C = Button(CalFrame, text="CA", width=5,
           height=2, font="Comicsanse 31 bold")
C.pack(side=LEFT, anchor=NW, ipadx=7.9)
C.bind("<ButtonRelease-1>", Clear)

Equals = Button(CalFrame, text="=", width=5,
                height=2, font="Comicsanse 31 bold")
Equals.pack(side=LEFT, anchor=NW, ipadx=7.9)
Equals.bind("<ButtonRelease-1>", OpHandler)

SGTech.mainloop()
