import time
print("Welcome to AvA Timer")

Start = input("Do you want to start your race ")
if Start == "yes".lower():
    def count_down(T):
        while T:
            min, sec = divmod(T, 60)
            timer = "{:02d}:{:02d}".format(min, sec)
            print(timer, end="\r")
            time.sleep(1)
            T -= 1


    t = input("Enter the time in seconds: ")

    count_down(int(t))
    print('Timer Completed')
    print('Go for your run')
else:
    print ('You have inputed a wrong value')
    quit()
