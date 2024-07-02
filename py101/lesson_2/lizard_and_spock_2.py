import os
import random
os.system('clear')

def prompt(message):
    """
    Printing with a special format
    """
    print(f"- {message}")

class GameSeries:
    # Set how many points should be achieved in the game
    points_in_game = int()

    # RPS or RPSLS
    type_of_game = str()

    # Express what wins vs what
    game_rules = {}

    # Valid full length words that are able to be played
    valid_game_plays = []

    # Valid single characters representing valid_game_plays can be input
    valid_single_char_choice = []

    # all_valid_choice_inputs = valid_game_plays + valid_single_char_choice
    all_valid_choice_inputs = []

    # to be deleted: valid_full_length_choice = list()
    game_number_counter = 1

    score = {"computer": 0, "user": 0}

    # Initiating a GameSeries
    def __init__(self, _points_in_game, _type_of_game):
        # Setting how many points are needed to win
        self.points_in_game = int(_points_in_game)

        # Configuring the game rules depending on the type of game
        if _type_of_game == "RPS":
            self.type_of_game = "RPS"
            self.game_rules = {"winning_against":
                                    {"scissors": ["paper"],
                                    "paper": ["rock"],
                                    "rock": ["scissors"]},
                                }
        elif _type_of_game == "RPSLS":
            self.type_of_game = "RPSLS"
            self.game_rules = {"winning_against":
                                    {"lizard": ["spock", "paper"],
                                    "spock": ["scissors", "rock"],
                                    "scissors": ["paper", "lizard"],
                                    "paper": ["rock", "spock"],
                                    "rock": ["lizard", "scissors"]},
                                }
        else:
            print("Error: No game rule set")
        # Collecting valid game choices based on type of game
        self.valid_game_plays = list(self.game_rules["winning_against"].keys())

        # Since user also can input first character in the play string,
        # that also has to be considered a valid input (even if it is an
        # invalid game choice before conversion to the game choice)
        # Important dependency: this also double counts the letter if two game
        # plays have the same initial character. This will later be used to
        # identify when a follow-up clarification is needed.
        self.valid_single_char_choice = \
            [list_unit[0] for list_unit in self.valid_game_plays]

        self.all_valid_choice_inputs = self.valid_game_plays +\
            self.valid_single_char_choice

    # Sending a welcome message to user depending on type_of_game
    def welcome_prompt(self):
        os.system("clear")
        if self.type_of_game == "RPS":
            prompt("""\nWelcome to, rock, paper, scissors!\n
                    Scissors cuts paper.\n
                    Paper covers rock.\n
                    Rock crushes scissors.\n
                    """)
        if self.type_of_game == "RPSLS":
            prompt("""\nWelcome to, rock, paper, scissors, lizard, spock!\n
                    Scissors cuts paper.\n
                    Paper covers rock.\n
                    Rock crushes lizard.\n
                    Lizard poisons Spock.\n
                    Spock smashes scissors.\n
                    Scissors decapitates lizard.\n
                    Lizard eats paper.\n
                    Paper disproves Spock.\n
                    Spock vaporizes rock.\n
                    Rock crushes scissors.\n
                    """)

    # Checking if the game has reached the points in game to end the game
    def check_if_player_won_series(self):
        return self.points_in_game in \
                (self.score["computer"], self.score["user"])
    def check_correct_user_choice(self, user_choice):
        return user_choice in self.all_valid_choice_inputs

    def define_full_length_choice(self, input_char):
        # If the user input character ony has ONE
        # corresponding full length string
        if self.valid_single_char_choice.count(input_char) == 1:
            # Find the choice starting with user input character
            for choice in self.valid_game_plays:
                if choice[0] == input_char:
                    return choice

        # If the user input character ony has MORE THAN ONE
        # corresponding full length string
        else:
            # Defining what choices are available starting with input_char
            alt_full_length_choices = [string for string in\
                                    self.valid_game_plays if\
                                    string.startswith(input_char)]

            # Prompt user to enter available choices
            prompt(f'There are {len(alt_full_length_choices)} choices'
                   f' starting with {input_char}. \n'
                   'Please choose one of the following by typing the number:')
            available_indexes_for_choice = []

            for number, choice in enumerate(alt_full_length_choices):
                prompt(f'Enter {number + 1} for {choice}.')
                available_indexes_for_choice.append(str(number + 1))

            user_choice = usr_input_str_query(available_indexes_for_choice)
            return alt_full_length_choices[int(user_choice) - 1]

    def determine_winner_or_tie(self, computer_choice, user_choice):

        for _item in self.game_rules["winning_against"][user_choice]:
            if _item == computer_choice:
                return "user"

        for _item in self.game_rules["winning_against"][computer_choice]:
            if _item == user_choice:
                return "computer"

        return "tie"

    def add_point_to_scoreboard(self, point_receiver):
        if point_receiver == "computer":
            self.score["computer"] += 1
        if point_receiver == "user":
            self.score["user"] += 1

    def play_round(self):
        # Player makes choice
        user_choice = input()

        # Choice is checked for correct input
        while self.check_correct_user_choice(user_choice) is False:
            self.prompt_round("incorrect_input_prompt")
            user_choice = input()

        # Single character choice is mapped to the
        # standard choice format (full string)
        if len(user_choice) == 1:
            user_choice = self.define_full_length_choice(user_choice)

        # Computer is choosing a random key in the game rules list
        computer_choice = random.choice(self.valid_game_plays)

        result = self.determine_winner_or_tie(computer_choice, user_choice)

        os.system("clear")

        prompt(f'You chose {user_choice}, computer chose {computer_choice}')

        if result == "computer":
            prompt('Computer wins!')
            self.add_point_to_scoreboard("computer")
        if result == "user":
            prompt('You win!')
            self.add_point_to_scoreboard("user")
        if result == "tie":
            prompt("It's a tie!")

        self.game_number_counter += 1

    def get_game_count(self):
        # How many rounds have been played in this series
        return self.game_number_counter

    def print_scoreboard(self):
        prompt(f'Computer: {self.score["computer"]} - '
               f'You: {self.score["user"]}')

    # Prompting for a new round of game
    def prompt_round(self, prompt_type):

        # Asking for user's choice
        if prompt_type == "initial_prompt":
            #os.system('clear')
            print(f'\n~~~~~~~~~ Round {self.game_number_counter}  |  Computer:'
                f' {self.score["computer"]} - You: {self.score["user"]} '
                '~~~~~~~~~\n'
                f'First to {self.points_in_game} wins!')
            prompt(f'Choose one: {" | ".join(self.valid_game_plays)}.\n You '
                   'can also write the first letter of your choice, for '
                   'example r for rock.')

        # If user's choice is incorrect,
        # student is informed to enter a new choice
        if prompt_type == "incorrect_input_prompt":
            prompt('Incorrect input. Choose one: '
                   f'{" | ".join(self.valid_game_plays)}.\n'
                   'You can also write the first letter of your choice, '
                   'for example r for rock.')

def usr_input_str_query(query_options):
    """
    This compares the input to expected input. It is case insensitive,
    so you can write either 'Y' or 'y'. This function assumes that 
    system input query_options is correct so no checking needed.

    Returning a validated user choice.
    """

    # Ask user for input
    user_input_str = input()

    query_options = [str.lower() for str in query_options]
    user_input_str = user_input_str.lower()
    # Checking if user input is in list of query options
    if user_input_str in query_options:
        return user_input_str
    prompt(f'We expect you to enter any of the following inputs: '
            f'{" | ".join(query_options)}')
    return usr_input_str_query(query_options)

def ask_play_again():
    """
    Checking if the user wants to play again
    """
    prompt("Do you want to play again? type y for yes or n for no (y/n)")

    yes_or_no = usr_input_str_query(["y", "n", "yes", "no"])

    if yes_or_no in ('y', "Y"):
        main()


def main():
    # Allow user to choose game mode RPS or RPSLS
    prompt('Welcome to this game!\n'
            'You can either play:\n'
            '1) Rock, Paper, Scissors or\n'
            '2) Rock, Paper, Scissors, Lizard, Spock\n'
            'Please choose 1 or 2')

    _type_of_game = usr_input_str_query(['1', '2'])
    if _type_of_game == '1':
        type_of_game = "RPS"
    elif _type_of_game == '2':
        type_of_game = "RPSLS"

    # Allow user to choose how many points there should be to win a game
    os.system('clear')
    prompt('Great choice!\n\n')

    prompt('This game can be played as a single round or as a series where the'
        ' first to win a specified number of rounds is the winner.\n\n'
        'How many points should be needed to win? (1 to 5 points)')
    number_of_points = usr_input_str_query(['1', '2', '3', '4', '5'])

    game = GameSeries(number_of_points, type_of_game)
    game.welcome_prompt()

    # If one player has wond the serier,
    # there is no need to continue the series

    while not game.check_if_player_won_series():
        game.prompt_round("initial_prompt")
        # Play a round
        game.play_round()
    prompt("PLAY AGAIN? :)")
    ask_play_again()

main()
