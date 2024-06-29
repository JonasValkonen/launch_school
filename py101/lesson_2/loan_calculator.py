# Loan calculator

"""
This loan calculator determines the monthly 
payment of a loan.

Input:
the loan amount
the Annual Percentage Rate (APR)
the loan duration

Output:
monthly payment
"""
# Ask for loan amount, APR and duration
# Check input for inconsistencies
# Calculate the monthly interest rate
# Print monthly interest rate

import os
import json
os.system('clear')
with open('loan_calculator_messages.json', 'r') as json_translation_table:
    MESSAGES = json.load(json_translation_table)

def select_language():
    prompt('Please select your language. Type the number 1 for english. '
           '输入“2”以选择中文. Skriv “3” för att välja svenska.')
    language_input = input()
    while language_input != '1' and language_input != '2' and language_input != '3':
        prompt('Wrong input. Type the number 1 for english. '
           '输入“2”以选择中文. Skriv “3” för att välja svenska.')
        language_input = input()
    if language_input == '1':
        return 'en'
    if language_input == '2':
        return 'zh'
    return 'se'
    
def prompt(message):
    """
    Printing with a special format
    """
    print(f"- {message}")

def validate_pos_float(item):
    """
    Validate if input is a positive float
    """
    if item == 'nan':
        prompt(MESSAGES[language]["no_nan"])
        item = validate_pos_float(input())
    if item == 'inf':
        prompt(MESSAGES[language]["no_inf"])
        item = validate_pos_float(input())
    if invalid_number_float(item): # checking if input is float
        prompt(MESSAGES[language]["input_number"])
        item = validate_pos_float(input())
    item = float(item)
    if item <= 0:
        prompt(MESSAGES[language]["positive_number"])
        item = validate_pos_float(input())
    return item

def validate_pos_int(item):
    """
    Validate if the input is a positive integer
    """
    if item == 'nan':
        prompt(MESSAGES[language]["no_nan"])
        item = validate_pos_float(input())
    if item == 'inf':
        prompt(MESSAGES[language]["no_inf"])
        item = validate_pos_float(input())
    if invalid_number_int(item):
        prompt(MESSAGES[language]["input_number"])
        item = validate_pos_int(input())
    if float(item) % 1 != 0:
        prompt(MESSAGES[language]["integer_number"])
        item = validate_pos_int(input())
    item = int(item)
    if item <= 0:
        prompt('Number should be positive')
        item = validate_pos_int(input())

    return item

def invalid_number_float(number_str):
    """
    Check if input can be a float
    """
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def invalid_number_int(number_str):
    """
    Check if input can be an integer
    """
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def monthly_payment(_loan_amount, _annual_rate,_loan_duration):
    """
    Calculate monthly payment based on loan amount, 
    annual interest rate and loan duration
    """
    monthly_rate = (_annual_rate / 12 ) / 100
    _monthly_payment = _loan_amount * (monthly_rate / (1 -
                        (1 + monthly_rate)**(-_loan_duration)))
    return round(_monthly_payment, 2)

def main():
    """
    Main segment that initiates the execution of the program
    """
    language = select_language()

    prompt(MESSAGES[language]["loan_amount"])
    loan_amount = validate_pos_float(input())

    prompt(MESSAGES[language]["annual_percentage_rate"])
    annual_rate = validate_pos_float(input())

    prompt(MESSAGES[language]["loan_duration"])
    loan_duration = validate_pos_int(input())

    _monthly_payment = monthly_payment(loan_amount, annual_rate, loan_duration)

    print(MESSAGES[language]["monthly_payment"].replace(
    r"{monthly_payment}", str(_monthly_payment)).replace(
    r"{loan_amount}", str(loan_amount)).replace(
    r"{loan_duration}", str(loan_duration)).replace(
    r"{annual_rate}", str(annual_rate)))

    print(MESSAGES[language]["calculate_again"])
    if input().lower() == 'y':
        main()

main()
