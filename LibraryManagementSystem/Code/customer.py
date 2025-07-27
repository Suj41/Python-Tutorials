# Customer Functionalities
# Customers can log in and borrow books. Their capabilities include:
# •	Log in using a function that reads users.txt and validates the role as "customer".
# •	View all available books from the books.txt file, showing title, author, and quantity.
# •	Borrow books by selecting from the available list. The program should confirm availability, reduce stock, and log the transaction in borrow.txt.
# •	View their borrow history by filtering the borrow.txt file to show only records related to their username.
import os
# paths for files
user_path = 'e:\\Documents\\Git Hub\\Python-Tutorials\\LibraryManagementSystem\\Files\\users.txt'
book_path = 'e:\\Documents\\Git Hub\\Python-Tutorials\\LibraryManagementSystem\\Files\\books.txt'
borrow_path = 'e:\\Documents\\Git Hub\\Python-Tutorials\\LibraryManagementSystem\\Files\\borrow.txt'

# Dictionary to store login information
# This will hold the username of the logged-in customer
login={}


def login_customer():
    print()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if the users.txt file exists and is not empty
    if not os.path.exists(user_path):
        print("No users found.")
        return
    # Read the users from the file and validate the credentials
    with open(user_path, 'r') as file:
        users = file.readlines()
    # Iterate through the users to find a match
    for user in users:
        user_details = user.strip().split(',')
        if user_details[0] == username and user_details[1] == password and user_details[2].lower() == 'customer':
            print(f"Welcome {username}!")
            login["username"] = username
            # Proceed to customer menu
            customer_menu()
            return True
    
    print("Invalid username or password.")
    return False

def view_books():
    print()
    # check if the books file exists and is not empty
    if not os.path.exists(book_path):
        print("No books available.")
        return
    
    with open(book_path, 'r') as file:
        books = file.readlines()
        
    # check if the books list is empty
    if not books:
        print("No books available.")
        return
    print("Available Books:")
    
    # Iterate through the books and print their details
    for book in books:
        title, author, quantity, id_ = book.strip().split(',')
        print(f"Title: {title}, Author: {author}, Quantity: {quantity}, ID: {id_}")

def borrow_book():
    
    book_name = input("Enter the name of the book you want to borrow: ").title().strip()
    if not book_name:
        print("Book name is required.")
        return
    if not os.path.exists(book_path):
        print("Books file not found.")
        return

    with open(book_path, 'r') as file:
        books = file.readlines()

    book_found = False
    updated_books = []
    for book in books:
        title, author, quantity_str, book_id = book.strip().split(',')
        if book_name.lower() == title.strip().lower():
            book_found = True
            quantity = int(quantity_str)
            if quantity <= 0:
                print(f"Insufficient stock of '{title}'.")
                return

            # Check if already borrowed
            borrow_present = False
            if os.path.exists(borrow_path):
                with open(borrow_path, 'r') as borrow_file:
                    for record in borrow_file:
                        uname, bname, _, _ = record.strip().split(',')
                        if uname == login['username'] and bname.strip().lower() == title.strip().lower():
                            borrow_present = True
                            break

            if borrow_present:
                print(f"{login['username']} has already borrowed '{title}'.")
                return

            # Log the borrow
            with open(borrow_path, 'a') as borrow_file:
                borrow_file.write(f"{login['username']},{title},{book_id},1\n")
            print(f"{login['username']} borrowed 1 copy of '{title}'.")

            # Update book quantity
            updated_books.append(f"{title},{author},{quantity - 1},{book_id}\n")
        else:
            updated_books.append(book)

    if not book_found:
        print("Book not found.")
        return

    # Write updated books
    with open(book_path, 'w') as file:
        file.writelines(updated_books)
     
              
def view_borrow_history():
    print()
    # Check if the borrow file exists and is not empty
    if not os.path.exists(borrow_path):
        print("No borrow history found.")
        return
    
    with open(borrow_path, 'r') as file:
        borrows = file.readlines()
    
    
    for borrow in borrows:
        user, title, book_id, qty = borrow.strip().split(',')
        print("Your Borrow History:")
        if user == login["username"]:
            print(f"Book Title: {title}, Book ID: {book_id}, Quantity: {qty}")
    
    
    
   
        

def customer_menu():
    print()
    while True:
        print("Customer Menu:")
        print("1. View Available Books")
        print("2. Borrow Book")
        print("3. View Borrow History")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            view_borrow_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            
