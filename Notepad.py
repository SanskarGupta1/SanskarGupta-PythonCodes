from tkinter import *
import tkinter.filedialog as Tf
import tkinter.messagebox as Tm

root = Tk()

root.geometry("1100x530")
root.title("SGTech")

TextArea = Text(root, font="Comicsanse 14 normal")
TextArea.pack(fill=BOTH, expand=True)

RlPath = ""
CurrentContent = ""

def Open():
    global RlPath

    Path = Tf.askopenfilename(filetypes=[("All files", "*.*"), ("Text files", "*.txt"),
                                         ("Python files", "*.py")])

    if Path != "":
        RlPath = Path

        with open(f"{RlPath}", "r") as reader:
            FileContent = reader.read()

        TextArea.delete('1.0', END)
        TextArea.insert('1.0', FileContent)


def CheckNOpen():
    global CurrentContent

    GetContent = TextArea.get('1.0', END)

    if GetContent != CurrentContent:
        GetAns = Tm.askyesnocancel("SGTech", "Do you want to save this file?")

        if GetAns == TRUE:
            Save()
            Open()
        elif GetAns == FALSE:
            Open()
        else:
            pass
    else:
        Open()


def Save():
    global RlPath, CurrentContent


    if RlPath != "":

        Content = TextArea.get('1.0', END)
        CurrentContent = Content

        with open(f"{RlPath}", "w") as writter:
            writter.write(Content)
    else:
        Path = Tf.asksaveasfilename(filetypes=[("All files", "*.*"), ("Text files", "*.txt"),
                                               ("Python files", "*.py")])

        if Path != "":
            RlPath = Path

            Content = TextArea.get('1.0', END)
            CurrentContent = Content

            with open(f"{RlPath}", "w") as writter:
                writter.write(Content)


def SaveAs():
    global RlPath, CurrentContent

    Path = Tf.asksaveasfilename(filetypes=[("All files", "*.*"), ("Text files", "*.txt"),
                                           ("Python files", "*.py")])

    if Path != "":
        RlPath = Path

        Content = TextArea.get('1.0', END)
        CurrentContent = Content

        with open(f"{RlPath}", "w") as writter:
            writter.write(Content)

MenuBar = Menu(root)

Functions = Menu(MenuBar, tearoff=0)

Functions.add_command(label="Open", command=CheckNOpen)
Functions.add_separator()
Functions.add_command(label="Save", command=Save)
Functions.add_command(label="SaveAs", command=SaveAs)
Functions.add_separator()
Functions.add_command(label="Exit", command=exit)

MenuBar.add_cascade(menu=Functions, label="More options")

root.config(menu=MenuBar)
root.mainloop()
