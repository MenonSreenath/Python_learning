#Write your code below this line ๐

def prime_checker(number):
    prime = False
    for n in range(2,number):
        if number%n == 0:
            prime = True
            break
    if prime == False:
        print("It's a prime number.")
    else :
        print("It's not a prime number.")


#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
