# bank_management.py

from Banker import Banker
from Customer import Customer

def display_menu():
    print("\nBank Management System")
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")

def main():
    banker = Banker()
    customer = Customer()

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            banker.execute_operations()
        elif choice == '2':
            customer.execute_operations()
        elif choice == '3':
            print("Exiting the Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-3).")

if __name__ == "__main__":
    main()
