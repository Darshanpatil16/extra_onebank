def deposit(amount, balance=0):
    if amount <= 0:
        return balance
    return balance + amount

def withdraw(amount, balance=0):
    if amount <= 0 or amount > balance:
        return balance
    return balance - amount

def get_balance(balance=0):
    return balance
