# Customer Banking App

**this is a customer banking system that allows users to calculate and track interest earned on savings and CD accounts.**

**_By running this app, users are able to enter their savings and CD account info, view interest earned, and view updated balances after specified number of months._**

### this project should not require any additional installs

#### project was built using python 11, but should run with most versions of python

**to start, simply run the following command in the correct directory**

```shell
python customer_banking.py
```

### How it works:

1. when the app starts, it will trigger the main function in customer_banking.py
2. it will then call request_customer_input()
   - this function starts a while loop with nested while loops for each input needed.
   - inputs needed are: 1. (float) balance 2. (float) interest rate 3. (int) length of time (in months)
     **_while loops were used to gather correct data types and to ensure the user input could be cast as correct data types (floats and integers)_**
3. Once the correct input is gathered, request_customer_input() returns the correct values as correct data types
4. the returned values are stored in variables and used as arguments when calling create_savings_account()
5. App will then calculate and print the interest earned and the users new balance
6. App will repeat for a CD account, reusing the request_customer_input(), and returning values to be used in create_cd_account()
