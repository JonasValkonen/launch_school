"""   
    Adds two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
"""
LANGUAGE = 'en'
import json
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    """
    Printing with a special format
    """
    print(f"==> {message}")

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def invalid_number(number_str):
    """
    Checking the input for type
    """
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def calc():
    """
    Calculator main loop
    """

    

    prompt(" What's the first number?")
    num1 = input()
    while invalid_number(num1):
        prompt(messages('invalid_number', LANGUAGE))
        num1 = input()

    prompt(" What's the second number?")
    num2 = input()
    while invalid_number(num2):
        prompt(messages('invalid_number', LANGUAGE))
        num2 = input()
    
    input_min_len = min(len(num1),len(num2))
    print(input_min_len)

    prompt("What operation would you like to perform?\n"
        "1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3 or 4')
        operation = input()

    match operation:
        case '1':
            output = float(num1) + float(num2)
        case '2':
            output = float(num1) - float(num2)
        case '3':
            output = float(num1) * float(num2)
        case '4':
            output = float(num1) / float(num2)


    prompt(f'The result is {output}')
    prompt("""Do you want to do another calculation? y/n""")
    reiterate = input()
    if reiterate == 'y':
        calc()

prompt(messages('welcome',LANGUAGE))
calc()
