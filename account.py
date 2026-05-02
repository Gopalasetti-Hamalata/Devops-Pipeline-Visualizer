class Account:

    def __init__(self, pin, balance=10000):

        self.pin = pin

        self.balance = balance


    def check_pin(self, entered_pin):

        return self.pin == entered_pin


    def withdraw(self, amount):

        if amount <= 0:

            return "Invalid amount"

        if amount > self.balance:

            return "Insufficient balance"

        self.balance -= amount

        return f"Withdrawn ₹{amount}"
