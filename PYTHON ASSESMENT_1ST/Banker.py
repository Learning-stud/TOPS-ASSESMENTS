
class Banker:
    def __init__(self):
        self.customer_data = {}  # Dictionary to store customer information
        self.log_file = 'transaction_log.txt'


            # types of opration  for customer
        self.customer_operations = {
            '1': self.add_customer,
            '2': self.view_customer,
            '3': self.search_customer,
            '4': self.view_all_customers,
            '5': self.total_amount_in_bank
        }

    # Customer Role And Its Related Logic
    def add_customer(self):
        print("\nBanker: Adding a new customer.")
        account_number = input("Enter customer account number: ")
        customer_name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))

        self.customer_data[account_number] = {
            'customer_name': customer_name,
            'balance': initial_balance
        }

            # Adding customer name and its account number
        self.log_transaction(f"Added customer {customer_name} with account number {account_number}")

        #Printing .....
        print(f"Customer {customer_name} added successfully.")


        # Function to View Customer ....
    def view_customer(self):
        print("\nBanker: Viewing a customer.")

        # First Account Number
        account_number = input("Enter customer account number: ")

        # if exists it will print exists else it will not be executad
        if account_number in self.customer_data:
            print(f"Customer Name: {self.customer_data[account_number]['customer_name']}")
            print(f"Balance: 💰{self.customer_data[account_number]['balance']}")
        else:
            print("Customer not found.")


        # For searching  Customer And HOw many customer Has Added
    def search_customer(self):
        print("\nBanker: Searching for a customer.")
        customer_name = input("Enter customer name: ")


        found_customers = []  # To store The user Search
        for account_number, customer_info in self.customer_data.items():  # for Account Number In Customer Info/ Datra Search acciount Related Name using items Function
            if customer_info['customer_name'].lower() == customer_name.lower():  # if Customer _info And Customer_Name  Are Equal
                found_customers.append(account_number)  # then Displaying

        # Function When Customer FOund !
        if found_customers:
            print("Found customers with the given name:")
            for account_number in found_customers:  #  In Customer_Name Is found Related TO account NUmber
                print(f"Account Number: {account_number}") # then Display Account Number
                print(f"Balance: 💰{self.customer_data[account_number]['balance']}") # And Their Account Balance
        else:
            print("No customers found with the given name.") # else No Account Found Related tpo that .. Account Number


    #  Function for Viewing Customer Details
    def view_all_customers(self):
        print("\nBanker: Viewing all customers.")
        if self.customer_data:
            print("All Customers:")


            #FOr account number and customer information In customer Data

            for account_number, customer_info in self.customer_data.items():
                print(f"Account Number: {account_number}")
                print(f"Customer Name: {customer_info['customer_name']}")
                print(f"Balance: 💰{customer_info['balance']}")
                print("--------------")
        else:
            print("No customers in the bank.")



    # Calculating Total Amount in bank
    # When total Transaction is credited by customer the banker can view the total balance.....

    def total_amount_in_bank(self):
        print("\nBanker: Calculating total amount in the bank.")
        #Sum function to calculate the balance
        total_amount = sum(customer_info['balance'] for customer_info in self.customer_data.values())
        print(f"Total Amount in the Bank: 💰{total_amount}")




        # while user is executing the opration
    def execute_operations(self):
        while True:
            # Oprations To Execute..
            print("\nBanker Operations Menu")
            print("1. Add Customer")
            print("2. View Customer")
            print("3. Search Customer")
            print("4. View All Customers")
            print("5. Total Amount in Bank")
            print("6. Go back to main menu")

            choice = input("Enter your choice (1-6): ")

            # If user press 6 the program will be break and start from starting
            if choice == '6':
                print("Returning to the main menu.")
                break
# And after that the user will go to Customer   options

            operation = self.customer_operations.get(choice)
            if operation:
                operation()
            else:
                print("Invalid choice. Please enter a valid option (1-6).")



    # Final opration to save all detail in another file by using File handling method
    def log_transaction(self, message):
        """Log transaction details to a file."""
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')
