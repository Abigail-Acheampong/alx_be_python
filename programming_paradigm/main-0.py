import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance with an initial balance of 100
    account = BankAccount(100)

    # Ensure at least one command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional parameter from the argument
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform operations based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use: deposit:<amount>, withdraw:<amount>, or display.")

if __name__ == "__main__":
    main()
