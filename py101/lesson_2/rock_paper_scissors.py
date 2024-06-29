# Rock paper scissors

"""
In this assignment, we'll build a Rock Paper Scissors game. 
Rock Paper Scissors is a simple game played between two opponents. 
Both opponents choose an item from rock, paper, or scissors. 
The winner is decided according to the following rules:

If player a chooses rock and player b chooses scissors, player a wins.
If player a chooses paper and player b chooses rock, player a wins.
If player a chooses scissors and player b chooses paper, player a wins.
If both players choose the same item, neither player wins. It's a tie.
Our version of the game lets the user play against the computer. 

The game flow should go like this:

The user makes a choice.
The computer makes a choice.
The winner is displayed.
"""
import os
import random
os.system('clear')

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    """
    Printing with a special format
    """
    print(f"- {message}")

def determine_winner(user_choice, computer_choice):
    """
    Letting the user know who won the game, the user or the computer.
    """
    if ((user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")):
        return "You win!"
    if ((user_choice == "rock" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "rock")):
        return "Computer wins!"
    return "It's a tie!"

def q_play_again():
    """
    Checking if the user wants to play again
    """
    prompt("Do you want to play again? type y for yes and n for no")
    y_or_n = input()
    if y_or_n[0].lower() == 'y':
        main()
    if y_or_n[0].lower() != 'n':
        q_play_again()

def main():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    user_choice = input()

    while user_choice.lower() not in VALID_CHOICES:
        prompt('Not a valid choice, you have to write rock,'
               ' paper or scissors')
        user_choice = input()

    user_choice = user_choice.lower()
    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    prompt(determine_winner(user_choice, computer_choice))

    q_play_again()

main()
