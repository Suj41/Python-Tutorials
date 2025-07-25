from admin import *
from customer import *
from staff import *
import os

def main_menu():
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("3. Staff Menu")
        print("4. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            admin_menu()
        elif choice == '2':
            login_customer()
        elif choice == '3':
            login_staff()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
main_menu()