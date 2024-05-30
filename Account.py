""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods
        params:
        balance (float): initial balance to the account
        interest (float): the interest gained on the account
    """
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    # simply returns balance
    def get_balance(self):
        """returns the account balance"""
        return self.balance

    # simply returns interest
    def get_interest(self):
        """returns the account interest"""
        return self.interest