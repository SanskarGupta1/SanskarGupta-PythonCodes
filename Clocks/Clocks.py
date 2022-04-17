from tkinter import *
from time import strftime
import tkinter.messagebox as Tm

Hour, Min, Sec, Run = 0, 0, 0 ,1
DisplayClock = 1
DisplayTimer = 1

GetHour = 0
GetMin = 0
GetSec = 0
SGTech = Tk()

SGTech.geometry('700x600')
SGTech.title("SGTech")

def StartTimer():
    global DisplayClock, ClockLabel

    DisplayClock = 0
    ClockLabel.config(text=f"0:0:0")

    HourValue = StringVar()
    MinValue = StringVar()
    SecValue = StringVar()

    HourValue.set('0')
    MinValue.set('0')
    SecValue.set('0')


    def TimerManager():
        global DisplayTimer

        if DisplayTimer == 1:
            Timer()
            SGTech.after(1000, TimerManager)
        else:
            DisplayTimer = 1
            return

    def Timer():
        global ClockLabel, GetHour, GetMin, GetSec

        if GetHour <= 0 and GetMin <= 0 and GetSec <= 0:
            ClockLabel.config(text=f"{GetHour}:{GetMin}:{GetSec}")
            return
        elif GetHour == 0 and GetMin != 0 and GetSec != 0:
            GetSec -= 1
            if GetSec == 0:
                GetMin -= 1
                GetSec = 60
        elif GetHour == 0 and GetMin == 0 and GetSec != 0:
            GetSec -= 1
            if GetSec == 0:
                ClockLabel.config(text=f"{GetHour}:{GetMin}:{GetSec}")
                return
            else:
                pass
        elif GetHour == 0 and GetMin != 0 and GetSec == 0:
            GetMin -= 1
            GetSec = 60

        elif GetHour != 0 and GetMin == 0 and GetSec == 0:
            GetHour -= 1
            GetMin = 59
            GetSec = 60
        elif GetHour != 0 and GetMin != 0 and GetSec == 0:
            GetHour -= 1
            GetMin = 59
            GetSec = 60

        ClockLabel.config(text=f"{GetHour}:{GetMin}:{GetSec}")

    def Set():
        global GetHour, GetMin, GetSec
        try:
            GetHour = int(HourEntry.get())
            GetMin = int(MinEntry.get())
            GetSec = int(SecEntry.get())
        except:
            Tm.showerror("SGTech", "Invalid values given.")
            quit()

    def StopTimer():
        global DisplayTimer
        DisplayTimer = 0

    def ResetTimer():
        global GetHour, GetMin, GetSec, DisplayTimer, ClockLabel
        GetHour = 0
        GetMin = 0
        GetSec = 0

        DisplayTimer = 0
        ClockLabel.config(text=f"{Hour}:{Min}:{Sec}")
        return

    def QuitTimer():
        global DisplayTimer
        HourLabel.destroy()
        HourEntry.destroy()

        MinLabel.destroy()
        MinEntry.destroy()

        SecLabel.destroy()
        SecEntry.destroy()

        Start.destroy()
        Pause.destroy()
        Reset.destroy()
        Quit.destroy()

        SetTime.destroy()

        DisplayTimer = 0
        ClockManager()


    HourLabel = Label(text="Hour: ", font="Comicsanse 15 bold", bg='black', fg='white')
    HourLabel.pack()

    HourEntry = Entry(textvariable=HourValue, font="Comicsanse 15 bold", justify=RIGHT)
    HourEntry.pack()

    MinLabel = Label(text="Min: ", font="Comicsanse 15 bold", bg='black', fg='white')

    MinLabel.pack()
    MinEntry = Entry(textvariable=MinValue, font="Comicsanse 15 bold", justify=RIGHT)
    MinEntry.pack()

    SecLabel = Label(text="Sec: ", font="Comicsanse 15 bold", bg='black', fg='white')
    SecLabel.pack()

    SecEntry = Entry(textvariable=SecValue, font="Comicsanse 15 bold", justify=RIGHT)
    SecEntry.pack()

    SetTime = Button(SGTech, text="Set time", font="Comicsanse 10 bold", command=Set)
    SetTime.pack(pady=10)

    Start = Button(text='Start', bg='black', fg='white', font="Comicsanse 35 bold", command=TimerManager)
    Start.pack(side=LEFT, anchor=S, padx=6)

    Pause = Button(text='Pause', bg='black', fg='white', font="Comicsanse 35 bold", command=StopTimer)
    Pause.pack(side=LEFT, anchor=S, padx=6)

    Reset = Button(text='Reset', bg='black', fg='white', font="Comicsanse 35 bold", command=ResetTimer)
    Reset.pack(side=LEFT, anchor=S, padx=6)

    Quit = Button(text='Quit', bg='black', fg='white', font="Comicsanse 35 bold", command=QuitTimer)
    Quit.pack(side=LEFT, anchor=S, padx=6)


def StopWatch():
    global ClockLabel, DisplayClock
    DisplayClock = 0

    ClockLabel.config(text=f"{Hour}:{Min}:{Sec}")

    def StartStopWatch():
        global Run, Sec

        if Run != 1:
            Run = 1
            return
        else:
            Sec += 1
            stopWatch()
        SGTech.after(1000, StartStopWatch)

    def stopWatch():
        global Hour, Min, Sec, ClockLabel

        if Sec == 60:
            Min += 1
            Sec = 0

        if Min == 60:
            Hour += 1
            Min = 0

        ClockLabel.config(text=f"{Hour}:{Min}:{Sec}")

    def ResetWatch():
        global Hour, Min, Sec, Run, ClockLabel

        Hour = 0
        Min = 0
        Sec = 0

        ClockLabel.config(text=f"{Hour}:{Min}:{Sec}")

        Run = 0

    def Pause():
        global Run
        Run = 0

    def QuitStopWatch():
        global DisplayClock

        Start.destroy()
        Reset.destroy()
        Stop.destroy()
        Quit.destroy()

        ClockManager()

    Start = Button(text="Start", font="Comicsanse 32 bold",
                   bg='black', fg='white', command=StartStopWatch)
    Start.pack(side=LEFT, pady=10, padx=4, anchor=S, ipadx=11)

    Reset = Button(text="Reset", font="Comicsanse 32 bold",
                   bg='black', fg='white', command=ResetWatch)
    Reset.pack(side=LEFT, pady=10, padx=4, anchor=S, ipadx=11)

    Stop = Button(text="Stop", font="Comicsanse 32 bold",
                  bg='black', fg='white', command=Pause)
    Stop.pack(side=LEFT, pady=10, padx=4, anchor=S, ipadx=11)

    Quit = Button(text="Quit Sw", font="Comicsanse 32 bold",
                  bg='black', fg='white', command=QuitStopWatch)
    Quit.pack(side=LEFT, pady=10, padx=4, anchor=S, ipadx=11)

    SGTech.config(bg='black')


def Clock():
    global ClockLabel

    Time = strftime("%H:%M:%S %p")

    ClockLabel.config(text=Time)

ClockLabel = Label(SGTech, bg='black', fg='cyan',
                   font="Comicsanse 40 bold", text="0:00:00")

ClockLabel.pack(anchor=CENTER, side=TOP)

def ClockManager():

    global DisplayClock

    if DisplayClock == 1:
        Clock()
        SGTech.after(1000, ClockManager)
    else:
        DisplayClock = 1
        return

ClockManager()

MenuBar = Menu(SGTech)

Functions = Menu(MenuBar, tearoff=0)

Functions.add_command(label='Normal clock', command=Clock)
Functions.add_command(label='Stop watch', command=StopWatch)
Functions.add_command(label='Timer', command=StartTimer)
Functions.add_command(label='Exit', command=exit)

MenuBar.add_cascade(menu=Functions, label='Clock functions')

SGTech.config(menu=MenuBar, bg='black')

SGTech.mainloop()
