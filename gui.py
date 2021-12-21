from glob import glob
import tkinter
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import cv2
import pytesseract
import pyperclip

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/tesseract/tesseract.exe'


def showImage():
    global fln
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG file", "*.png"),
                                                                                                   ("JPEG files", "*.jpg"), ("All files", "*.*")))
    img = Image.open(fln)
    resized_image = img.resize(
        (root.winfo_screenwidth() // 3, root.winfo_screenheight()), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resized_image)
    lbl.configure(image=img)
    lbl.image = img


def textDetect():
    global text
    image = fln
    text = pytesseract.image_to_string(image)
    ctext.delete(1.0, tkinter.END)
    ctext.insert(tkinter.END, text)


def copyText():
    pyperclip.copy(text)


root = tkinter.Tk()

frm = tkinter.Frame(root)
frm.pack(side=tkinter.RIGHT)

lbl = tkinter.Label(root)
lbl.pack(side=tkinter.LEFT)

ctext = tkinter.Text(root, height=500, width=52)
ctext.pack()

btn = tkinter.Button(frm, text="Browse image",
                     command=showImage)

btn2 = tkinter.Button(frm, text="Detection",
                      command=textDetect)
btn3 = tkinter.Button(frm, text="Copy text",
                      command=copyText)
btn.grid(row=0, column=0)
btn2.grid(row=1, column=0)
btn3.grid(row=3, column=0)
root.title("Text Extraction")
# Set geometry to fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
              root.winfo_screenheight()))
root.mainloop()
