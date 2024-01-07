# bank_management.py

from Banker import Banker
from Customer import Customer

def display_menu():
    print("\nBank Management System")
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")

def main():
    # calling  both function at a time of options
    banker = Banker()
    customer = Customer()


# Displaying selection type.....
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
# when user press 1 and 2 executing the opration....
        if choice == '1':
            banker.execute_operations()

        elif choice == '2':
            customer.execute_operations()
        # when User  Press 3 the Management system will be closed.....
        elif choice == '3':
            print("Exiting the Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-3).")

        # automatically called the function

if __name__ == "__main__":
    main()
