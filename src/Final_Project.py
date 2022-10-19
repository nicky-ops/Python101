# Rock Paper Sciccors Game

import random



def game ():
    
    while True:

        default = random.choice(["Rock", "Paper", "Scissors"])
        default = default.lower()
        choice = input("Enter Your Choice: rock, paper or scissors: ")
        choice = choice.lower()
        print(f"The Computer chose:  {default}")
        if choice == "quit":
            break
        if choice == default:
            print("You tied")
            continue
        elif choice == "paper" and default == "rock":
            print("You Win!")
            break
        elif choice == "rock" and default == "scissors":
            print("You Win!")
            break
        elif choice == "scissors" and default == "paper":
            print("You won")
            break
        else:
            print("You Lose. Try again!")
        
        

game()