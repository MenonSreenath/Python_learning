print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
name = name1+name2
score1 = 0
score2 = 0

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")

L = name.count("l")
O = name.count("o")
V = name.count("v")


score1 = T+R+U+E
score2 = L+O+V+E
score3 = str(score1)+str(score2)
score = int(score3)

if ((score)<10) or ((score)>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif ((score)>40) and ((score)<50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




