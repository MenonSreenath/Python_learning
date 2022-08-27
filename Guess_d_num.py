import random
import replit

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]


print("Welcome to Number Guessing Game \n")
print("Im Thinking of a number between 1 and 100 \n")
difficulty = input("Choose a dificulty 'easy' or 'hard' \n").lower()

number = random.choice(numbers)
continue_play = True
while continue_play == True:
    replit.clear()
    def compare(guess) :
      if guess == number :
        return("correct")
    
      elif (guess > number):
        return("Too High \n")
    
      elif (guess < number):
        return("Too Low \n")
    
    
    
    def num_guessed (turns):
      while turns != 0:
        print(f"You have {turns} attemps to guess the number \n")
        guess = int(input("Make a Guess \n"))
        result = compare(guess)
        if result == "correct" :
          print(f"Eactly, the number i guessed is {number} \n")
          break
        else :
          print(result)
          turns -= 1
      if turns == 0 :
        print("You are out of your turns \n")
    
    
        
    if difficulty == "hard" :
      turns = 5
      num_guessed(turns)
      
    elif difficulty == "easy":
      turns = 10
      num_guessed(turns)
    else :
      print(f"invalid input")
  
    play = input("Want to play again \n")
    if play == "yes":
      continue_play = True
    else: 
      continue_play = False
      print("GAME OVER!!!!")
    




                