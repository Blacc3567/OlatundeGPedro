import random
from ssl import Options 

user_wins = 0 
Computer_wins = 0 

print ("Welcome to AvA Rock Paper Scissors Game")
while True:
   player = input ("(rock/paper/scissors): ").lower
   if player != "rock".lower:
      break
   if player != "paper".lower:
       break
   if player != "scissors".lower:
       break
    
option =  ["rock", "paper", "scissors"]
computer_pick = option[random.randint(0,2)]
print (computer_pick)

   
     
while True:
      print("")

      if player == computer_pick:
        print ("Tie!")
     
      elif player == "r": 
       if computer_pick == "s":
          print ("you won")
          user_wins = 1
      else:
       ("you lose")
       Computer_wins = 1
                
       if player == "paper":
        if computer_pick == "rock":
          print ("you won")
          user_wins = 1
    
       else:
        ("you lose")
        Computer_wins = 1
        if player == "scissors":
         if computer_pick == "paper":
          print ("you won")
          user_wins = 1
          
        else: 
           print ("you lost ")
           Computer_wins = 1   
      break
    
while True:         
  play_again = input ("Do you want to play again (yes/no) ")
  if play_again == "yes":
          player()
  if player == "no":
   print ("you won", user_wins, " times")
   print ( "The computer wins", Computer_wins," times")
   print ("goodbye")   
   


   
    