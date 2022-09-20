from ast import While


print ("Welcome to the Question Game ")
play = input ("Do you want Play this game: ")

while True:
 if play.lower() == "yes":
    print ("lets Play")
    Pointscore = 0 
    Question1 = input ("What does CPU Mean: ")
    if Question1.lower() == "central processing unit":
        print ("Correct Answer")
        Pointscore += 1
    else:
        print ("Wrong Answer")
        Pointscore
    Question2 = input ("What does GPU Mean: ")
    if Question2.lower() == "graphics processing unit":
        print ("Correct Answer")
        Pointscore += 1
    else:
        print ("Wrong Answer")
        Pointscore
    Question3 = input ("what does RAM Mean: ")
    if Question3.lower() == "random acess memory":
        print ("Correct Answer")
        Pointscore += 1
    else:
        print ("Wrong Answer")
        Pointscore
    Question4 = input ("What does PSU Mean: ")
    if Question4.lower() == "power supply":
        print ("Correct Answer")
        Pointscore += 1
    else:
        print ("Wrong Answer")
        Pointscore
    
    Total = print ("You got " + str(Pointscore) + " Questions Correct")
    break
 elif play.lower() == "no":
    print ("")
    print ("Too bad")
    print (" ")
    print ("bye") 
    break
 elif play not in ["yes", "no"]:
    print ("you have inputed the wrong value ") 
    break
    