class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

jake = User("Jake", "jake@123.com")
guido = User("Guido", "guido@123.com")
hannah = User("Hannah", "hannah@123.com")

jake.make_deposit(300).make_deposit(250).make_deposit(150).make_withdrawal(150).display_user_balance()

guido.make_deposit(150).make_deposit(250).make_withdrawal(100).make_withdrawal(150).display_user_balance()

hannah.make_deposit(500).make_withdrawal(170).make_withdrawal(50).make_withdrawal(100).display_user_balance()

jake.transfer_money(hannah, 150).display_user_balance()

hannah.display_user_balance()