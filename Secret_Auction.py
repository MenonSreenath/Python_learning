import os
from re import A

def add_new_entry(name,bid):
    Bids[name]=bid

def auction():
    name = input("Enter your name \n")
    bid = input("Enter your bid \n")
    add_new_entry(name,bid)
   


Bids = {}
max=0
max_mem=""
choose="yes"
auction()
while (choose=="yes"):
    choose = input("Is there another bidder?? \n").lower()
    if (choose=="yes"):
        os.system('cls')
        auction()
    else:
        for i in Bids:
            if (int(Bids[i]))>=max:
                max_mem=i
            
        print (f"{max_mem} is the highest bidder with a bid of {Bids[max_mem]} \n")