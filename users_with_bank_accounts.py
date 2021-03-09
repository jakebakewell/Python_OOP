class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        self.balance -= amount
        return self
    def account_balance(self):
        print(self.balance)
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {'savings': BankAccount(0.02, 0)}
    def make_deposit(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self
    def make_withdrawal(self, account_name, amount):
        self.accounts[account_name].withdrawal(amount)
        return self
    def display_user_balance(self, account_name):
        print(self.name, account_name)
        self.accounts[account_name].account_balance()
        return self
    def transfer_money(self, other_user, account_name, amount):
        self.accounts[account_name].balance -= amount
        other_user.accounts[account_name].balance += amount
        return self
    def create_account(self, account_type, int_rate, balance):
        self.accounts[account_type] = BankAccount(int_rate, balance)

jake = User("Jake", "jake@123.com")
hannah = User("Hannah", "hannah@123.com")
jake.create_account('checking', 0, 200)
hannah.create_account('checking plus', 0, 100)
jake.make_deposit('checking', 200).make_deposit('savings', 300).make_withdrawal('checking', 100).make_withdrawal('savings', 150).display_user_balance('checking').display_user_balance('savings')
hannah.make_deposit('checking plus', 500).make_deposit('savings', 400).make_withdrawal('checking plus', 250).make_withdrawal('savings', 250).display_user_balance('checking plus').display_user_balance('savings')