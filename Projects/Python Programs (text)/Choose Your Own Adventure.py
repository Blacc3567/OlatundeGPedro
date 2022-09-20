





def start ():
 print ("Your on a bike going through a dirt road")
 play = input ("You have reached a dead end. type l to go left  or r to go right ")
 if play.lower() == "l":
       left()
 if play.lower() == "r":
       right()
 if play not in ["l", "r"]:
        wrongvalue2()

def end ():
   print ("Too Bad")
   print ("Bye")
   quit()

def left():
 print ("you have passed the dead end and continuing on your journey ") 
 print ("...........................................................")
 play = input ("you have come across a river, type s to swim or w to walk around it ")
 if play == "s":
       swim()
 if play == "w":
       walkacross()
 if play not in ["s", "w"]:
      wrongvalue2()
def wrongvalue2 ():
      print ("you inputed the wrong value ")
      quit()

def swim ():
 play = input ("You are swimming across the river and you have come across a crocrodile. type a to attack: " )
 if play == "a":
       attack()
 if play not in ["a"]:
      wrongvalue2()

def walkacross ():
 print ("you cant walk on water genius, what are you jesus ?")
 quit()

def attack ():
 print ("You have killed the crocrodile and crossed the river")
 play = input ("you are on a dirt road, but you have met an ogre. type a to attack or r to run: ")
 if play == "a": 
    ogreattack()
 if play == "r":
        run ()
 if play not in ["a" , "r"]:
      wrongvalue2()

def ogreattack ():
 play = input ("the ogre has blocked your attack with his sheild and has fired his bazooka weapon. type d to dodge or j to jump: ")
 if play == "d":
      dodge()
 if play == "j":
      jump()
 if play not in ["d", "j"]:
      wrongvalue2()

def dodge ():
 play = input ("you have dodged the ogre's attack. now type a to attack: ")
 if play == "a":
      Ogrefinishingattack()
 if play not in ["a"]:
      wrongvalue2()

def Ogrefinishingattack():
 play = input ("you have killed the ogre, type v to cross the finishing line: ")
 if play == "v":
      victory()
 if play not in ["v"]:
      wrongvalue2()

def victory ():
      print ("")
      print ("You have won The AvA Monster game ")  
      print ("")
      print ("congratulations")
      quit()

def jump ():
      print ("you have been hit by the ogre's attack")
      print ("game over")
      quit ()
def run ():
      print ("you ran away and the ogre got to yo and killed you.")
      print  ("Bye")
      quit ()

def right ():
   play = input ("you have gone right but have come across a ledge. type j to jump ")
   if play == "j":
          jump1()
   if play not in ["j"]:
          wrongvalue2()
def jump1 ():
   play = input ("you have come across another ledge. type j to jump ")
   if play == "j":
          jump2()
   if play not in ["j"]:
      wrongvalue2()
def jump2 ():
   play = input ("you have come across another ledge. type j to jump ")
   if play == "j":
          jump3()
   if play not in ["j"]:
      wrongvalue2()
def jump3 ():
      print ("you have passed all the ledges and are continuing on the journey")
      print ("")
      print (".................................................................")
      play = input ("you are on a dirt road, but you have met an ogre. type a to attack or r to run: ")
      if play == "a": 
       ogreattack()
      if play == "r":
        run ()
      if play not in ["a" , "r"]:
       wrongvalue2()
def wrongvalue():
   print ("You have inputed the wrong value")
   begin()

def begin ():
 print ("Welcome to AvA Monster Gamer")
 play = input ("Do you want to play this game yes/no: ")
 if play.lower() == "yes":
     start()
 elif play.lower() == "no":
     end()
 elif play not in ["yes", "no"]:
     wrongvalue()


begin()
start()
left()
swim()
walkacross
wrongvalue()
wrongvalue2
attack()
ogreattack()
dodge()
jump()
run
right()
end()














