# Customer.py

class Customer:


    def __init__(self):

        # Initialize Customer default balance  and creating transaction detail file ......
        self.account_balance = 0.0
        self.log_file = 'transaction_log.txt'

        self.operations = {
            '1': self.withdraw_amount,
            '2': self.deposit_amount,
            '3': self.view_balance
        }



    def withdraw_amount(self):
        print("\nCustomer: Withdrawing amount.")
        withdrawal_amount = float(input("Enter the amount to withdraw: "))

        if withdrawal_amount <= self.account_balance:
            self.account_balance -= withdrawal_amount
            print(f"Withdrew 💰{withdrawal_amount}. Remaining balance: 💰{self.account_balance}")
            self.log_transaction(f"Withdrew 💰{withdrawal_amount}")
        else:
            print("Insufficient funds. Withdrawal canceled.")




    def deposit_amount(self):
        print("\nCustomer: Depositing amount.")
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.account_balance += deposit_amount

        print(f"Deposited 💰{deposit_amount}. New balance: 💰{self.account_balance}")
        self.log_transaction(f"Deposited 💰{deposit_amount}")




    def view_balance(self):
        print("\nCustomer: Viewing balance.")
        print(f"Current Balance: 💰{self.account_balance}")



    def execute_operations(self):
        while True:
            print("\nCustomer Operations Menu")
            print("1. Withdraw Amount")
            print("2. Deposit Amount")
            print("3. View Balance")
            print("4. Go back to main menu")

            choice = input("Enter your choice (1-4): ")

            if choice == '4':
                print("Returning to the main menu.")
                break

            operation = self.operations.get(choice)
            if operation:
                operation()
            else:
                print("Invalid choice. Please enter a valid option (1-4).")



    def log_transaction(self, message):
        """Log transaction details to a file."""
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')
