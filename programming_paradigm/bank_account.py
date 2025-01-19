class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount 
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Amount should be positive")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                print(f"Withdrew: ${amount:.2f}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdraw amount must be positive.")
            return False
        
    def display_balance(self):
        print("Display the current balance")
        print(f"Your current balance is {self.account_balance:.2f}")