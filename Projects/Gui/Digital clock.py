from functools import partial
from pickle import MARK
from tkinter import *
import time
from time import strftime

app = Tk()
app.title("A.V.A Clock Machine")
app.geometry("500x500")
app.resizable(1,1)
app.configure(background="grey")

text_font= ("Boulder", 68, 'bold')
border_width = 25
fg = "black"
Label (app, font=text_font, bd=border_width, fg=fg, background="grey").pack()

Label(text="").pack()

def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(app, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black',
            bg="grey")
mark.pack(anchor = 'center')
time()
#clock = partial(app, text_font, border_width, fg, Label, digital_clock)
time()
mainloop()   