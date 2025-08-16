class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0 # Default attribute value

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount    

    def display_balance():
        print(f"Current Balance: ${amount}")