# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance, savings_interest, savings_maturity = request_customer_input("Savings Account")


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Congratulations! You have earned {interest_earned:,.2f} during the time period!")
    print(f"and your updated savings balance is: {updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance, cd_interest, cd_maturity = request_customer_input("CD Account")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Congratulations! You have earned {interest_earned:,.2f} during the time period!")
    print(f"and your updated savings balance is: {updated_cd_balance:,.2f}")

def request_customer_input(account_type):
    """
    this function will get the user input for:
        account balance (float)
        account interest (float)
        maturity/length (integer)
    params: account type (string)
        **strictly for display purposes
    """
    requesting_customer_input = True
    while requesting_customer_input:
        getting_account_balance = True
        getting_account_interest = True
        getting_account_maturity = True
        while getting_account_balance:
            account_balance_input = input(f"What is your {account_type} balance?\n Please enter in as a float: 000.00  ")
            getting_account_balance = False if isfloat(account_balance_input) else True
            balance = float(account_balance_input)
        while getting_account_interest:
            account_interest_input = input(f"What is the interest you will be earning on {account_type}?\n Please enter as a float: 00.00  ")
            getting_account_interest = False if isfloat(account_interest_input) else True
            interest = float(account_interest_input)
        while getting_account_maturity:            
            account_maturity_input = input(f"What is the length (in months) for the {account_type}?\n please enter a integer: 00  ")
            getting_account_maturity = False if account_maturity_input.isdigit() else True
            maturity = int(account_maturity_input)
        requesting_customer_input = False
    return balance, interest, maturity

# function is taken from:
# https://www.programiz.com/python-programming/examples/check-string-number#:~:text=In%20the%20function%20isfloat(),is%20raised%20and%20returns%20False%20.
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

if __name__ == "__main__":
    # Call the main function.
    main()
