from ast import Pass
from re import A
from unicodedata import name

def grant ():
    global granted 
    granted = True 


def register (name,password):
     file = open (name+".txt", "a")
     file.write("\n"+name+","+password)
     grant()

     file.close
def login (name, password):
    #print ("logged in")
    sucess = False
    file = open (name+".txt", "r")
    for i in file: 
        a,b = [i.strip(",") for i  in open (name+".txt")]
        b = b.strip
    if (name,password == a,b):
   # if (a==name and b==password):
       sucess = True
    file.close 
    if (sucess): 
      print("login Successfull")
      grant()
    else:
       print ("Wrong Username and Password check both of them again") 
   
    
    
def acess (Option):
    global name
    if (Option=="login"):
        name = input("Enter Your Name: ")
        password = input ("Enter Your Password: ")
        login (name, password)
    else:
        print("Enter Your Name and Password to register")
        name = input("Enter Your Name: ")
        password = input ("Enter Your Password: ")
        register(name,password)
                           
    
def begin () :
    global Option
    print("Welcome to A.v.A Media")
    Option = input ("Login or Register (login,reg):  ")
    if (Option!="login" and Option!="reg" ):
          acess(Option)
          begin()
    else:
        print ("Enter login or password")   
begin()
acess(Option)


if(granted):
     print ("Welcome To AvA Media")
     print ("*### User Details ###*")
     print ("Username:  "+ name);''

