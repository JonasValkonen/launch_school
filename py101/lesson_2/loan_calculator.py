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
#os.system('clear')
with open('loan_calculator_messages.json', 'r') as json_translation_table:
    MESSAGES = json.load(json_translation_table)
LANGUAGE = 'en'

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
        prompt(MESSAGES[LANGUAGE]["no_nan"])
        item = validate_pos_float(input())
    if item == 'inf':
        prompt(MESSAGES[LANGUAGE]["no_inf"])
        item = validate_pos_float(input())
    if invalid_number_float(item): # checking if input is float
        prompt(MESSAGES[LANGUAGE]["input_number"])
        item = validate_pos_float(input())
    item = float(item)
    if item <= 0:
        prompt(MESSAGES[LANGUAGE]["positive_number"])
        item = validate_pos_float(input())
    return item

def validate_pos_int(item):
    """
    Validate if the input is a positive integer
    """
    if item == 'nan':
        prompt(MESSAGES[LANGUAGE]["no_nan"])
        item = validate_pos_float(input())
    if item == 'inf':
        prompt(MESSAGES[LANGUAGE]["no_inf"])
        item = validate_pos_float(input())
    if invalid_number_int(item):
        prompt(MESSAGES[LANGUAGE]["input_number"])
        item = validate_pos_int(input())
    if float(item) % 1 != 0:
        prompt(MESSAGES[LANGUAGE]["integer_number"])
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
    print(type(_loan_duration))
    
    monthly_payment = _loan_amount * (monthly_rate / (1 -
                        (1 + monthly_rate)**(-_loan_duration)))
    return round(monthly_payment, 2)

def main():
    
    prompt(MESSAGES[LANGUAGE]["loan_amount"]) # Asking user for loan amount
    loan_amount = validate_pos_float(input())

    prompt(MESSAGES[LANGUAGE]["annual_percentage_rate"]) # Asking user for loan amount
    annual_rate = validate_pos_float(input())

    prompt(MESSAGES[LANGUAGE]["loan_duration"])
    loan_duration = validate_pos_int(input())

    _monthly_payment = monthly_payment(loan_amount, annual_rate, loan_duration)

    print(MESSAGES[LANGUAGE]["monthly_payment"].replace(
    r"{monthly_payment}", str(_monthly_payment)).replace(
    r"{loan_amount}", str(loan_amount)).replace(
    r"{loan_duration}", str(loan_duration)).replace(
    r"{annual_rate}", str(annual_rate)))

    print(MESSAGES[LANGUAGE]["calculate_again"])
    if input().lower() == 'y':
        main()

main()
