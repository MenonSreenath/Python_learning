def play():

    import os
    import random as r
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] # 11 - ACE, 10 - King,queen,jocker and normal 10 card

    def deal_card(b):
        """Returns a random card from the deck"""
        new_card = r.choice(cards)
        b.append(new_card)

    def calculate(a):
        """Calculates the total fo the list of the cards"""
        total = 0
        for i in a:
            total += i
        if (total==21 and (len(a))==2):
            return 0 # blackjack - (a hand with only 2 cards: ace + 10)
        for i in a:
            if (total>21 and i==11):
                a.remove(11)
                a.append(1)
        return total

    def compare(a,b):
        if (a==b):
            print("Its a Draw!! \n")
        elif (b==0):
            print("You Lose!!! COmputer got a blackjack \n")
        elif (a==0):
            print("You Win!!! You got a blackjack \n")
        elif (a>21):
            print("You Lose!!! Score exceeds 21. \n")
        elif (b>21):
            print("You Win!!! COmputer score exceeds 21 \n")
        elif (a>b):
            print("You Win!!!")
        else:
            print("Computer Wins!!!")




    def check():
        if (new_card_option=='y'): 
            deal_card(user_cards) 
            user_score = calculate(user_cards)
            computer_score = calculate(computer_cards)
            compare(user_score,computer_score)


    choice = input("Do you wanna play a game of Blackjack!? y/n \n").lower()
    if (choice=='y'):
        os.system("cls")
        user_cards = r.sample(cards,2)
        user_score = calculate(user_cards)
        computer_cards = r.sample(cards,2)
        computer_score = calculate(computer_cards)
        if (user_score==0):
            print("You Lose!!! Computer got a blackjack \n")
            exit()
        elif (computer_score==0):
            print("You Win!!! You got a blackjack \n")
            exit()
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        game_ends = False
        while(game_ends==False):
            new_card_option = input("Type 'y' to get another card,type 'n' to pass: \n")
            game_ends = check()
            if (new_card_option=='n'):
                if (computer_score < 17):
                    deal_card(computer_cards)
                    game_ends=check()
                else:
                    print(computer_cards)
            print(user_cards)
            new = input("Want to start new game?? \n")
            if (new=='y'):
                os.system("cls")
                play()
            else:
                exit()

play()