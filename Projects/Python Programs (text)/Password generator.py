import random
import string
print("Welcome to AvA Password Generator")
chars = list(string.ascii_letters + string.digits + "!@#$%^&()")

number = input("Input amount of password ")
number = int(number)
length = input ("input password length ")
length = int(length)

print("here are your password ")

for pwd in range (number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)