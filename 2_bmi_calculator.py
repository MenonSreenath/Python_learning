# Program for checking our BMI value
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# formula for BMI= weight(kg)/(height)^2(m)
# bmi value indication are below: 
#0-18 : underweight
#19-24 : healthy
#25-29 : overweight
#30-39 : obese
#40-above : extremely overweight

h = float(height)
w = int(weight)

noin_round_bmi = w / (h ** 2)

bmi = round(weight/(height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


