class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

jake = User("Jake", "jake@123.com")
guido = User("Guido", "guido@123.com")
hannah = User("Hannah", "hannah@123.com")

jake.make_deposit(300)
jake.make_deposit(250)
jake.make_deposit(150)
jake.make_withdrawal(150)
jake.display_user_balance()

guido.make_deposit(150)
guido.make_deposit(250)
guido.make_withdrawal(100)
guido.make_withdrawal(150)
guido.display_user_balance()

hannah.make_deposit(500)
hannah.make_withdrawal(170)
hannah.make_withdrawal(50)
hannah.make_withdrawal(100)
hannah.display_user_balance()

jake.transfer_money(hannah, 150)
jake.display_user_balance()
hannah.display_user_balance()