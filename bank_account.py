class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_account_balance(self):
        print(self.balance)
        return self
    def yield_interest(self):
        interest = self.balance * (self.int_rate/100)
        self.balance += interest
        return self

jake = BankAccount(2.0, 200)
hannah = BankAccount(3.0, 250)

jake.make_deposit(200).make_deposit(150).make_deposit(250).make_withdrawal(200).yield_interest().display_account_balance()

hannah.make_deposit(350).make_deposit(300).make_withdrawal(150).make_withdrawal(200).make_withdrawal(100).make_withdrawal(150).yield_interest().display_account_balance()