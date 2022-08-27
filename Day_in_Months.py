def is_leap(year):
    if (year%4==0):
        if (year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    leap_year = is_leap(year)
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    else:
        if (leap_year==True):
            return 29
        else:
            return 28

#days in a month = [31,28,31,30,31,30,31,31,30,31,30,31]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
