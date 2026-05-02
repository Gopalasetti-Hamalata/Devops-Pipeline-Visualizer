from account import Account
 
def test_withdraw():
    acc = Account(1234, 1000)
    assert acc.withdraw(500) == "Withdrawn ₹500"
