class BankAccount:
    def __init__(self,account_balance=100):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance+= int(amount)
        return True
    def withdraw(self, amount):
        if self.account_balance >= int(amount):
            amount = float(amount)
            self.account_balance-= (amount)
            return True
        else:
            return False
    def display_balance(self):
         print(f"Current Balance: ${float(self.account_balance)}0")