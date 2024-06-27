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


def prompt(message):
    """
    Printing with a special format
    """
    print(f"-{message}")

def validate_pos_float(item):
    """
    Validate if input is a positive float
    """
    while invalid_number_float(item): # checking if input is float
        prompt('Input should be a number')
        item = input()
    item = float(item)
    while item < 0:
        prompt('Number should be positive')
        item = input()
        validate_pos_float(item)
    return item

def validate_pos_int(item):
    """
    Validate if the input is a positive integer
    """
    while invalid_number_int(item):
        prompt('Input should be a number')
        item = input()
    while float(item) % 1 != 0:
        prompt('Number should be an integer')
        item = input()
        validate_pos_float(item)
    item = int(item)
    while item < 0:
        prompt('Number should be positive')
        item = input()
        validate_pos_float(item)

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

def monthly_payment(loan_amount_, annual_rate_,loan_duration_):
    """
    Calculate monthly payment based on loan amount, 
    annual interest rate and loan duration
    """
    monthly_rate_ = (annual_rate_ / 12 ) / 100
    monthly_payment_ = loan_amount_ * (monthly_rate_ / (1 -
                        (1 + monthly_rate_) ** (-loan_duration_)))
    return round(monthly_payment_, 2)

prompt("What's the loan amount? (in $)") # Asking user for loan amount
loan_amount = validate_pos_float(input())

prompt("What's the Annual Percentage Rate? (in %)") # Asking user for loan amount
annual_rate = validate_pos_float(input())

prompt("What's the loan duration? (in months)") # Asking user for loan amount
loan_duration = validate_pos_int(input())

print(f'The monthly payment is ${monthly_payment(loan_amount, annual_rate, loan_duration)}')
