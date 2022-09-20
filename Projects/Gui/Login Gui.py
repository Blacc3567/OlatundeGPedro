from atexit import register
from cProfile import label
from cgitb import grey, text
from functools import partial
from msilib.schema import Font
from textwrap import fill
from tkinter import * 
from tkinter import messagebox
from tkinter import font
from turtle import bgcolor, color


def login(username, reg):
	print("username entered :", username.get())
	print("password entered :", reg.get())
	return


root=Tk()
root.title("Welcome to AVA Login Page")
root.geometry("500x500")
root.configure(background= "white")




Header= Label(text="Welcome to A.V.A World", bg="black", width="300", height="2", font=("Hobo Std", 10, font.BOLD), fg= "white").pack()


Label(text="").pack() 


username =Label(root,text= "Login", font=("Stencil STD", 15, font.BOLD), bg= "white").pack(padx= 25, pady=25)
StringVar()
Button(root, username, text="Select", height="2", width="30", font=("Bahnschrift", 8)).pack() 
Label(text="").pack() 

reg =Label(root,text= "Register", font=("Stencil STD", 15, font.BOLD), bg= "white").pack(padx= 35, pady=35)

StringVar()

Button(root, reg, text="Register", height="2", width="30", font=("Bahnschrift", 8)).pack()
Label(text="").pack() 
Entry

login = partial(login, username, reg)

root.mainloop()