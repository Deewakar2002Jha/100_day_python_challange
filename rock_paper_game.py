#importing the pyhton libray
import random

#defining the function
def get_choices():
    #defining the variable
    #player_choice = "rock"
    player_choice = input("enter the choice(rock , paper ,scissors: )")
    #computer_choice ="paper"
    options = ["rock","paper","scissors"]
    
    computer_choice = random.choice(options)
    #get a value back from the varible
    choices = {"player":player_choice,"computer":computer_choice}
    
    return choices

#passing the argument in the function
def check_win(player,computer):
    #to check what a player check
    print("You chose:-  "+player+   "   computer choose:-  "   +  computer )
    if player == computer :
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors ! You win!"
    elif player == "paper" and computer == "rock":
        return "Paper covered rock ! You Win"
    elif player == "scissors" and computer == "paper":
        return "Scissors cut paper ! You Win!"
    elif player == "scissors" and computer == "rock":
        return "Rock break the scissors! You Loose!"
    elif player == "rock" and computer == "paper":
        return "Paper covered paper! You Loose!"
    elif player == "scissors" and computer == "paper":
        return "Scissors cut paper! You loose"
    else:
        return "choose from the options"
    

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
#check_win("rock","paper")

#know using if and else statement to check the condtion
a = 3
b = 4
if a > b :
    print("yes")




