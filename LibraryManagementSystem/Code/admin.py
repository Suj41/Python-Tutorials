# Admin Functionalities
# The Admin is responsible for managing users and overseeing the system. Implement the following features:
# •	Create new Staff and Admin users by adding their usernames, passwords, and roles into a users.txt file.
# •	Ensure that duplicate usernames are not allowed by checking the existing entries in the file before adding.
# •	Allow Admin to view a list of all users and their roles (read from users.txt).
# •	Implement a function to delete any staff member from the system by removing their line from the users.txt file.
# •	Add a login system for Admins that checks the username, password, and role from the users.txt.
import os
userpath= 'E:\\Documents\\Python\\LMS\\Files\\users.txt'

def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (Customer/Staff): ").title()
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    if role not in ['Customer', 'Staff']:
        print("Invalid role. Please enter 'Admin' or 'Staff'.")
        return
    
    if not username or not password or not address or not phone or not email:
        print("All fields are required. Please fill in all details.")
        return
    
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Please enter a 10-digit phone number.")
        return
    
    if '@' not in email or '.' not in email.split('@')[1]:
        print("Invalid email format. Please enter a valid email address.")
        return
    
    # Check if the users.txt file exists, if not create it
    if os.path.exists(userpath):
        with open(userpath) as file:
            users = file.readlines()
        # Check for duplicate usernames
        for user in users:
            if user.split(',')[0] == username:
                print("Username already exists. Please choose a different username.")
                return
    
    with open(userpath, 'a') as file:
        file.write(f"{username},{password},{role},{address},{phone},{email} \n")
    
    print(f"User {username} created successfully.")

def view_users():
    if not os.path.exists(userpath):
        print("No users found.")
        return
    
    with open(userpath, 'r') as file:
        users = file.readlines()
    
    if not users:
        print("No users found.")
        return
    
    print("List of Users:")
    for user in users:
        username, password, role, address, phone, email = user.strip().split(',')
        print(f"Username: {username}, Role: {role}, Address: {address}, Phone: {phone}, Email: {email}")

def delete_user():
    if not os.path.exists(userpath):
        print("No users found.")
        return
    delete_entry = input("Enter the username of the user to delete: ")
    with open(userpath, 'r') as file:
        users = file.readlines()
    with open(userpath, 'w') as file:
        found = False
        for user in users:
            if user.split(',')[0] != delete_entry:
                file.write(user)
            else:
                found = True
        if found:
            print(f"User {delete_entry} deleted successfully.")
        else:
            print(f"User {delete_entry} not found.")
    

def admin_menu():
    while True:
        print("Admin Menu:")
        print("1. Create User:")
        print("2. View Users:")
        print("3. Delete User:")
        print("4. Exit:")
        choice = input("Enter your choice: ")
        if choice == '1': 
            create_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            print("Exiting Admin Menu.")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            

        