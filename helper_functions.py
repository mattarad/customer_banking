def request_customer_input(account_type):
    """
    this function will get the user input for:
        account balance (float)
        account interest (float)
        maturity/length (integer)
    params: account type (string)
        the param accout_type is used in print statements
    """
    requesting_customer_input = True
    while requesting_customer_input:
        getting_account_balance = True
        getting_account_interest = True
        getting_account_maturity = True
        while getting_account_balance:
            account_balance_input = input(f"What is your {account_type} balance?\n Please enter in as a float: 000.00  ")
            match isfloat(account_balance_input):
                case True:
                    balance = float(account_balance_input)
                    getting_account_balance = False
                case _:
                    continue
        while getting_account_interest:
            account_interest_input = input(f"What is the interest you will be earning on {account_type}?\n Please enter as a float: 00.00  ")
            match isfloat(account_interest_input):
                case True:
                    interest = float(account_interest_input)
                    getting_account_interest = False
                case _:
                    continue
            
        while getting_account_maturity:            
            account_maturity_input = input(f"What is the length (in months) for the {account_type}?\n please enter a integer: 00  ")
            match account_maturity_input.isdigit():
                case True:
                    maturity = int(account_maturity_input)
                    getting_account_maturity = False
                case _:
                    continue
        requesting_customer_input = False
    return balance, interest, maturity


# see README.md to see website where isfloat() was taken from
# this function takes in a number as a string and tries to convert it to a float using a try/except to catch an error
# if it can then it will return true, else if there is an error it will return false
def isfloat(num):
    """function takes in a variable and trys to convert to a float using a try/except to handle any errors
        if the parameter can be turned into a float, it will return true
        if a ValueError is thrown then it will return false
    """
    try:
        float(num)
        return True
    except ValueError:
        return False