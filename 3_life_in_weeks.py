age = input("What is your current age? \n")

#Write your code below this line 👇

years_left = 90- int(age) #pending years

days = 365*years_left # no.of days = 22,995
weeks = 52*years_left # no.of weeks = 3,276
months = 12*years_left # no.of months = 756

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


