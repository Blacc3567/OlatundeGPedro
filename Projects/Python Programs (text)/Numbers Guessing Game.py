from cProfile import run
import random


print ("Welcome to AvA Number Game")
random_number = random.randint(0,10)
Guess = 0
User_input = input ("Make a Number Guess  ")
Guess = 1 
print (random_number)
if random_number == User_input:
    print ("Correct")   
else:
      print ("Wrong Number")

User_input = input ("Make a Number Guess  ")
Guess = 1 
print (random_number)
if random_number == User_input:
    print ("Correct")   
else:
      print ("Wrong Number")

User_input = input ("Make a Number Guess  ")
Guess = 1 
print (random_number)
if random_number == User_input:
    print ("Correct")   
else:
      print ("Wrong Number")


print ("You Got the Number on " + str (Guess) + " Guesses")  



