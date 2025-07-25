# Customer Functionalities
# Customers can log in and borrow books. Their capabilities include:
# •	Log in using a function that reads users.txt and validates the role as "customer".
# •	View all available books from the books.txt file, showing title, author, and quantity.
# •	Borrow books by selecting from the available list. The program should confirm availability, reduce stock, and log the transaction in borrow.txt.
# •	View their borrow history by filtering the borrow.txt file to show only records related to their username.
import os
book_path = 'E:\\Documents\\Python\\LMS\\Files\\books.txt'
borrow_path = 'E:\\Documents\\Python\\LMS\\Files\\borrow.txt'

login={}


def login_customer():
    print()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not os.path.exists('E:\\Documents\\Python\\LMS\\Files\\users.txt'):
        print("No users found.")
        return
    
    with open('E:\\Documents\\Python\\LMS\\Files\\users.txt', 'r') as file:
        users = file.readlines()
    
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
    for book in books:
        title, author, quantity, id_ = book.strip().split(',')
        print(f"Title: {title}, Author: {author}, Quantity: {quantity}, ID: {id_}")

def borrow_book():
    print()
    book_name = input("Enter the book name to borrow: ").strip()
    if not book_name:
        print("Book name is required.")
        return

    

    if not os.path.exists(book_path):
        print("No books available.")
        return

    with open(book_path, 'r') as f:
        books = f.readlines()

    updated_books = []
    book_found = False
    selected_book = None

    # Find the book
    for book in books:
        title, author, quantity, book_id = book.strip().split(',')
        if title.lower() == book_name.lower():
            book_found = True
            selected_book = (title, author, int(quantity), book_id)
        else:
            updated_books.append(book.strip())

    if not book_found:
        print(f"Book '{book_name}' not found.")
        return

    if selected_book[2] == 0:
        print(f"'{selected_book[0]}' is currently out of stock.")
        return

    borrow_qty = input("Enter quantity to borrow: ").strip()
    if not borrow_qty.isdigit() or int(borrow_qty) <= 0:
        print("Invalid quantity.")
        return
    borrow_qty = int(borrow_qty)

    if borrow_qty > selected_book[2]:
        print(f"Only {selected_book[2]} copies available.")
        return

    new_quantity = selected_book[2] - borrow_qty
    # Add updated book info back to list
    updated_books.append(f"{selected_book[0]},{selected_book[1]},{new_quantity},{selected_book[3]}")

    # Save updated book list
    with open(book_path, 'w') as f:
        for line in updated_books:
            f.write(line + '\n')

    # Handle borrow.txt
    borrow_updated = []
    borrow_recorded = False

    if os.path.exists(borrow_path):
        with open(borrow_path, 'r') as f:
            borrow_records = f.readlines()

        for record in borrow_records:
            user, title, book_id, qty = record.strip().split(',')
            if user == login['username'] and title.lower() == book_name.lower():
                total_qty = int(qty) + borrow_qty
                borrow_updated.append(f"{user},{title},{book_id},{total_qty}")
                borrow_recorded = True
            else:
                borrow_updated.append(record.strip())

    if not borrow_recorded:
        borrow_updated.append(f"{login['username']},{selected_book[0]},{selected_book[3]},{borrow_qty}")

    with open(borrow_path, 'w') as f:
        for record in borrow_updated:
            f.write(record + '\n')

    print(f"{borrow_qty} copy of '{selected_book[0]}' borrowed successfully by {login['username']}.")

              
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
            
