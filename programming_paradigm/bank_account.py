class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount 
        else:
            print("Amount should be positive")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdraw amount must be positive.")
    def display_balance(self):
        print("Display the current balance")
        print(f"Your current balance is {self.account_balance:.2f}")