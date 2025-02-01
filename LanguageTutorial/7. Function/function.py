def open_account():
    print("new account generated")

def deposit(balance, money):
    print("deposit is finished. Left is {0}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance > money:
        print("withdraw is finished. Left is {0}".format(balance - money))
        return balance - money
    else:
        print("withdraw is not finished. Left is {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

open_account()

balance = 0
print(balance)
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 300)
print("commission is {0} won, left is {1} won".format(commission, balance))