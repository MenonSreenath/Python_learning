print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input(""" Make a Choice now!!!
 Left - Where nothing is right !
 or
 Right - Where Nothing is left!\n""")
choice = choice.lower()

if (choice == "left"):

   print("""Atleast the treasure is left even thought nothing else is left
   
   Run the wild beasts are coming for you!!!! Get out as soon as possible!!
   
   Swim accross or catch that boat coming over there and save yourself \n""")
   
   choice1 = input("Choose if you wanna go by swim or boat \n")
   choice1= choice1.lower()
   
   if (choice1 == "boat"):
    print("Nice choice. Go ahead on the island and open any one door")
    
    choice2 = input("Which door would you wanna open Red Blue or Green \n")
    
    choice2 = choice2.lower()
    
    if (choice2 == "red"):
          print("Your Dead!!!! Burned to ashes by fire. GAME OVER")
    elif (choice2 == "yellow"):
      print("Yellow Yellow Dirty fellow, Your Dead - Eaten by maggots, GAME OVER!!!!")
    elif (choice2 == "blue"):
      print("""Treasure found!!!! You win!
       However nothing is right here, Your treasure has no value!! HAHAHAHAHAHA GAME OVER!!!!!!!!!""")

   elif(choice1 == "swim"):
      print("GAME OVER!!! Killed by the captain of the boat in a fit of anger")
      
elif(choice == "right"):
    print("""Nothing is left. Not even your life.
  Your dead - GAME OVER """)

