import os

def add(a,b):
    c=a+b
    return c

def sub(a,b):
    d=a-b
    return d

def mul(a,b):
    e=a*b
    return e

def div(a,b):
    f=a/b
    return f

def mod(a,b):
    g=a%b
    return g


def calculation():
    operations = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":div,
        "%":mod,
    }
    a = float(input("Enter the first number \n"))
    for i in operations:
        print(i)
    condition = True
    while(condition==True):
        c = input("Enter the operation to perform \n")
        b = float(input("Enter the next number \n"))
        function = operations[c]
        t=function(a,b)
        print(f"{a}{c}{b}={t}")
        option = input("Type 'y' to continue same calculation and 'n' to start new calculation, if you want to stop input 'stop' \n").lower()
        if (option=="y"):
            condition = True
        elif(option=="n"):
            os.system("cls")
            calculation()
        elif(option=="stop"):
            break

calculation()

