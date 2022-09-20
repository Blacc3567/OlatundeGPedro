from json import load
from telnetlib import ENCRYPT
from tokenize import Name
from unicodedata import name
from cryptography.fernet import Fernet



def wronginfo():
       print ("you have inputed a wrong info")
       print("")
       print("bye")

def view ():
     Name =  input ("account name ")
     pwd =  input ("enter password ")  
     with open ( Name + ".txt", "r") as f:
        for line in f.readlines() :
            data =line.rstrip()
            user , password = data.split(",")
            print ("User: ", user,",", "Password: ", password)
def add ():
    Name = input ("account name ")
    pwd = input ("enter password ")
    with open (Name + ".txt", "a") as f:
        f.write (Name+ "," + pwd + "\n")
        begin()
def opp():
 while True:
  mode = input ("would you like to add a new password or view existing one's (view/ add)  press q to quit ")

  if mode == "q":
    break

  if mode == "view":
    view()
  elif mode == "add":
    add()
  else: 
    print ("invalid mode")
  if mode not in ["view", "add", "q"]:
       wronginfo()

def begin ():
     pwd = input (" what is the Master Password " )
     while pwd == True:
      opp()

begin()
opp()
view()
add()
wronginfo()    


