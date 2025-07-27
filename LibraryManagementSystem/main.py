# sys package is used to manipulate the Python runtime environment
# os package is used to interact with the operating system
import sys
import os
#  this line ensures that the parent directory is included in the system path
# so that we can import modules from the LibraryManagementSystem package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LibraryManagementSystem.Code.admin import *
from LibraryManagementSystem.Code.customer import *
from LibraryManagementSystem.Code.staff import *


# This is the main entry point for the Library Management System application.
# It provides a menu for users to choose between admin, customer, and staff functionalities.
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