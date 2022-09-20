print("Welcome to AvA Calculator")

num1 = int(input("enter first number "))
num2 = int(input ("enter second Number "))
op = input ("Enter an opreator ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print (num1-num2)
elif op == ["x", "*"]:
    print (num1 * num2)
elif op == "/":
    print (num1/num2)
else:
    print ("invalid operator")