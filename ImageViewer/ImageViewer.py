from tkinter import *
import tkinter.filedialog as Tf
from PIL import Image, ImageTk

root = Tk()

Images = []
CurrentImage = 0

LabelImage = Label(root)
LabelImage.pack()


def AddImage():
    global Images, NumOfImage, LabelImage

    Path = Tf.askopenfilename(filetypes=[("Jpg files", "*.jpg"), ("Png files", "*.png")])

    image = Image.open(Path)
    image = ImageTk.PhotoImage(image)

    Images.append(image)

    NumOfImage.config(text=len(Images))

    LabelImage.config(image=image)


def NextImage():
    global CurrentImage, LabelImage, Images

    CurrentImage += 1

    LabelImage.config(image=Images[CurrentImage])

def PrevImage():
    global CurrentImage, LabelImage, Images

    CurrentImage -= 1

    LabelImage.config(image=Images[CurrentImage])


Close = Button(root, text="Close app", command=exit)
Close.pack(side=BOTTOM, fill=X)

AddAnImage = Button(root, text="Add an image", command=AddImage)
AddAnImage.pack(side=BOTTOM, fill=X)

ImageBack = Button(root, text="<", command=PrevImage, width=10)
ImageBack.pack(side=LEFT, anchor=S, fill=X, expand=True)

NumOfImage = Label(root, text=len(Images), width=10)
NumOfImage.pack(side=LEFT, anchor=S)

ImageForward = Button(root, text=">", command=NextImage, width=10)
ImageForward.pack(side=RIGHT, anchor=S, fill=X, expand=True)

root.mainloop()

