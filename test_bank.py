from bank import deposit, withdraw, get_balance

def test_deposit_with_default_balance():
    balance = deposit(500)
    assert balance == 500

def test_deposit_with_existing_balance():
    balance = deposit(300, 1000)
    assert balance == 1300

def test_invalid_deposit():
    balance = deposit(-200, 1000)
    assert balance == 1000

def test_withdraw_with_default_balance():
    balance = withdraw(100)
    assert balance == 0

def test_withdraw_valid():
    balance = withdraw(400, 1000)
    assert balance == 600

def test_withdraw_more_than_balance():
    balance = withdraw(2000, 1000)
    assert balance == 1000
