class BankAccount:
    def __init__(self,account_balance=0):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance+= int(amount)
    def withdraw(self, amount):
        if self.account_balance >= int(amount) and self.account_balance > 0:
            self.account_balance-= int(amount)
        else:
            print("Insufficient funds")
    def display_balance(self):
         print(f"Hi, Your Current Balance is: {self.account_balance}")