from cProfile import label
from cgitb import grey
from tkinter import *
from turtle import right 
from textblob import TextBlob



root = Tk()
root.title("Spell Checker")
root.geometry("500x500")
root.config(background="grey")

def check_spelling():
     a = TextBlob(enter_text.get())
     right = str(a.correct())

     cs = Label(root, text="Correct text is : ", font=("Times New Roman", 20),bg="grey", fg="white")
     cs.place(x=100,y=250)
     cs.pack()
     text= Label(root, text=str(a.correct()), font=("Times New Roman",20, "bold"), bg= "grey",  fg="black")
     text.pack()
     spell.config(text=right)
     

header= Label(root, text="Spelling Checker", font=("Times New Roman", 25, "bold"), bg= "grey" ,fg="white")
header.pack(pady= (50, 0))

enter_text = Entry(root, justify="center", width=30, font=("Times New Roman", 25), bg="white", border=5)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("Times New Roman", 20,"bold"), fg="White", bg= "black", command= check_spelling)
spell = Label(root, font=("Times New Roman", 20), bg="grey", fg="black")
button.pack()

root.mainloop()





















#from spellchecker import SpellChecker

#spell = SpellChecker()

#msp = spell.unknown(["cmputr", "watr", "study", "wrte"])

#for word in msp:
# print(spell.correction(word))
# print(spell.candidates(word))








#from re import T
#from textblob import TextBlob

#a = "computr"
#print("original text: " + str(a))

#b = TextBlob(a)

#print("corrected text: " + str(b.correct()))

