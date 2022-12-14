from distutils.cmd import Command
import math
from tkinter import *
from tokenize import Number

root = Tk()
root.title("Simple Calculator")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg= "grey")

Enter = Entry(root, width= 80, bd= 2)
Enter.grid(row=0, column=0, columnspan=3, padx= 10, pady= 10)

def button_click (number):
    current = Enter.get()
    Enter.delete (0, END)
    Enter.insert(0, str(current) + str(number) )
 
def button_cleared ():
    Enter.delete (0, END)

def button_add ():
   first_number = Enter.get()
   global f_num 
   global math
   math = "addition"
   f_num = int(first_number)
   Enter.delete (0, END)

def button_equals_to ():
   second_number = Enter.get()
   if math == "addition":
      Enter.delete (0, END)
      Enter.insert(0,f_num + int(second_number))

   if math == "subtraction":
          Enter.delete (0, END)
          Enter.insert(0,f_num - int(second_number))

   if math == "multiplication":
          Enter.delete (0, END)
          Enter.insert(0,f_num * int(second_number))
   
   if math == "division":
          Enter.delete (0, END)
          Enter.insert(0,f_num / int(second_number))



def button_minus ():
   first_number = Enter.get()
   global f_num 
   global math
   math = "subtraction"
   f_num = int(first_number)
   Enter.delete (0, END)


def button_times ():
   first_number = Enter.get()
   global f_num 
   global math
   math = "multiplication"
   f_num = int(first_number)
   Enter.delete (0, END)

def button_division ():
   first_number = Enter.get()
   global f_num 
   global math
   math = "division"
   f_num = int(first_number)
   Enter.delete (0, END)


button_1 = Button(root, text="1", padx= 40, pady= 20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx= 40, pady= 20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx= 40, pady= 20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx= 40, pady= 20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx= 40, pady= 20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx= 40, pady= 20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx= 40, pady= 20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx= 40, pady= 20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx= 40, pady= 20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx= 40, pady= 20, command= lambda: button_click(0))
button_addition = Button(root, text="+", padx= 39, pady= 15, command=  lambda: button_add())
button_equals = Button(root, text="=", padx= 55, pady= 15, command= lambda: button_equals_to())
button_clear=Button(root, text="clear", padx= 50, pady= 15, command= lambda: button_cleared())
button_minus_eq=Button(root, text="-", padx= 50, pady= 15, command= lambda: button_minus())
button_multiply =Button(root, text="*", padx= 50, pady= 15, command= lambda: button_times())
button_divide =Button(root, text="/", padx= 50, pady= 15, command= lambda: button_division())
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_clear.grid(row= 5, column=1)
button_equals.grid(row= 8, column=2)
button_addition.grid(row= 7, column=2)
button_minus_eq.grid(row= 7, column=0)
button_multiply.grid (row=8, column= 0)
button_divide.grid (row= 8, column= 1)
root.mainloop()