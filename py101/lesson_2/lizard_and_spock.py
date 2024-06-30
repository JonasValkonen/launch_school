

import os
import random
os.system('clear')

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WIN_LOOSE_PAIRS ={"winning_against":
                    {"lizard": ["spock", "paper"],
                    "spock": ["scissors", "rock"],
                    "scissors": ["paper", "lizard"],
                    "paper": ["rock", "spock"],
                    "rock": ["lizard", "scissors"]},
                "loosing_against":
                    {"lizard": ["rock", "scissors"],
                     "spock": ["lizard", "paper"],
                     "scissors": ["rock", "spock"],
                     "paper": ["scissors", "lizard"],
                     "rock": ["paper", "spock"]
                    }
                }

GAMES_IN_MATCH = 5

# Global counters for wins
COMPUTER_WINS = 0
USER_WINS = 0

def prompt(message):
    """
    Printing with a special format
    """
    print(f"- {message}")

def determine_winner(user_choice, computer_choice):
    """
    Letting the user know who won the game, the user or the computer.
    """
    tie_flag = 1

    for _item in WIN_LOOSE_PAIRS["winning_against"][user_choice]:
        if _item == computer_choice:
            tie_flag = 0
            prompt('You win!')
            match_series_status("user")

    for _item in WIN_LOOSE_PAIRS["loosing_against"][user_choice]:
        if _item == computer_choice:
            tie_flag = 0
            prompt('Computer wins!')
            match_series_status("computer")

    if tie_flag == 1:
        prompt("It's a tie!")

def q_play_again():
    """
    Checking if the user wants to play again
    """
    prompt("Do you want to play again? type y for yes and n for no")
    y_or_n = input()

    if y_or_n[0].lower() == 'y':
        global COMPUTER_WINS, USER_WINS
        COMPUTER_WINS = 0
        USER_WINS = 0
        os.system('clear')
        main()

    if y_or_n[0].lower() != 'n':
        q_play_again()

def check_valid_choice(user_choice):
    _user_choice = user_choice.lower()
    valid_initials_choices = map_choice_initial_w_choices()

    if (user_choice.lower() not in VALID_CHOICES) and (user_choice.lower()
                                    not in valid_initials_choices):
        prompt(f'Not a valid choice, you have to write '
            f'{", ".join(VALID_CHOICES)} or the first letter of your choice')
        _user_choice = input()
        return check_valid_choice(_user_choice)

    return _user_choice

def map_choice_initial_w_choices():
    choice_initial_map = {}
    for valid_choice in VALID_CHOICES:
        choice_initial = valid_choice[0]
        if choice_initial not in choice_initial_map:
            choice_initial_map[choice_initial] = [valid_choice]
        else:
            choice_initial_map[choice_initial].append(valid_choice)
    return choice_initial_map

def list_possible_choice_index(choice_inits_w_choices, user_choice):

    possible_choice_index = []

    for index, _ in enumerate(choice_inits_w_choices[user_choice[0]]):
        possible_choice_index.append(index + 1)

    return str(possible_choice_index)

def print_possible_choices_for_initial(choice_inits_w_choices, user_choice):
    for index, choice in enumerate(choice_inits_w_choices[user_choice[0]]):
        prompt(f'{index+1}: {choice}')


def define_user_choice(user_choice):
    #If choice is expressed as the full exact name
    if user_choice in VALID_CHOICES:
        return user_choice
    #If choice is not expressed as the full exact name
    choice_inits_w_choices = map_choice_initial_w_choices()

    # If choice initial only has one corresponding choice
    if len(choice_inits_w_choices[user_choice[0]]) == 1:
        return str(choice_inits_w_choices[user_choice][0])

    # If choice initial has more than one corresponding choice
    if (user_choice[0] in choice_inits_w_choices) and \
        len(choice_inits_w_choices[user_choice[0]]) > 1:
        prompt('There is more than one choice starting with that letter. '
        'Please insert the corresponding number to choose:')
        print_possible_choices_for_initial(choice_inits_w_choices, user_choice)

        possible_choice_initials = list_possible_choice_index( \
            choice_inits_w_choices, user_choice)

        _choice = 0
        while True:
            _choice = input()
            if _choice in possible_choice_initials:
                prompt(choice_inits_w_choices\
                    [user_choice[0]][int(_choice) - 1])
                return choice_inits_w_choices\
                    [user_choice[0]][int(_choice) - 1]
            prompt('Choice is not correct, please choose between:')
            for index, choice in \
                enumerate(choice_inits_w_choices[user_choice[0]]):
                prompt(f'{index+1}: {choice}')

def match_series_status(winner):
    if winner == "user":
        global USER_WINS
        USER_WINS += 1
        if USER_WINS == GAMES_IN_MATCH:
            prompt(f"You have {GAMES_IN_MATCH} wins and win the series!")
    elif winner == "computer":
        global COMPUTER_WINS
        COMPUTER_WINS += 1
        if COMPUTER_WINS == GAMES_IN_MATCH:
            prompt(f"Computer has {GAMES_IN_MATCH} wins and win the series!")
    if GAMES_IN_MATCH not in (COMPUTER_WINS,USER_WINS):
        prompt(f'Computer: {COMPUTER_WINS} - You: {USER_WINS}')

def main():
    
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}. You can also write '
           'the first letter of your choice, for example r for rock.')
    user_choice = input().lower()
    user_choice = check_valid_choice(user_choice)
    user_choice = str(define_user_choice(user_choice))

    user_choice = user_choice.lower()
    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    determine_winner(user_choice, computer_choice)
    print("\n--------------Next Round---------------\n")
    if GAMES_IN_MATCH in (COMPUTER_WINS,USER_WINS):
        q_play_again()
    elif (COMPUTER_WINS < GAMES_IN_MATCH) and (USER_WINS < GAMES_IN_MATCH):
        main()

main()
