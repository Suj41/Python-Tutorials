# Staff Functionalities
# The Staff members handle book management and customer services. Staff should be able to:
# •	Add new books to a books.txt file with details like title, author, quantity, and unique book ID.
# •	Ensure no duplicate book titles or IDs are added by checking the file beforehand.
# •	Register new customers by storing their usernames and passwords in the same users.txt file with a role of "customer".
# •	Allow customers to borrow books by checking if the requested book is available, updating the quantity, and recording the borrow in a borrow.txt file.
# •	View borrow history of customers by reading from borrow.txt, which logs which user borrowed which book and when.
import os
login={}

userpath= 'e:\\Documents\\Git Hub\\Python-Tutorials\\LibraryManagementSystem\\Files\\users.txt'
book_path = 'e:\\Documents\\Git Hub\\Python-Tutorials\\LibraryManagementSystem\\Files\\books.txt'
borrow_path = 'e:\\Documents\\Git Hub\\Python-Tutorials\\LibraryManagementSystem\\Files\\borrow.txt'

def add_new_book():
    title = input("Enter book title: ").title().strip()
    author = input("Enter book author: ")
    quantity = input("Enter quantity: ")
    book_id = input("Enter unique book ID: ")
    
    if not title or not author or not quantity or not book_id:
        print("All fields are required. Please fill in all details.")
        return
    
    if author.isdigit():
        print("Author should only contain alphabetic characters.")
        return
    if not book_id.isdigit():
        print("Book ID should be numeric.")
        return
    
    if  len(book_id) != 4:
        print("Book ID should be in 4 digits.")
        return
    
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity. Please enter a quantity in postive number.")
        return
    
    # Check if the books.txt file exists, if not create it
    if os.path.exists(book_path):
        with open(book_path) as file:
            books = file.readlines()
        # Check for duplicate titles or IDs
        for book in books:
            if book.split(',')[0] == title or book.split(',')[3] == book_id:
                print("Book title or ID already exists. Please choose a different one.")
                return
    
    with open(book_path, 'a') as file:
        file.write(f"{title},{author},{quantity},{book_id}\n")
    
    print(f"Book '{title}' added successfully.")

def view_books():
    if not os.path.exists(book_path):
        print("No books available.")
        return
    
    with open(book_path, 'r') as file:
        books = file.readlines()
    
    if not books:
        print("No books available.")
        return
    
    print("Available Books:")
    for book in books:
        title, author, quantity, book_id = book.strip().split(',')
        print(f"Title: {title}, Author: {author}, Quantity: {quantity}, ID: {book_id}")

def view_customers():
    if not os.path.exists(userpath):
        print("No customers found.")
        return
    
    with open(userpath, 'r') as file:
        users = file.readlines()
    
    if not users:
        print("No customers found.")
        return
    
    print("List of Customers:")
    for user in users:
        username, password, role, address, phone, email = user.strip().split(',')
        if role == 'Customer':
            print(f"Username: {username}, Address: {address}, Phone: {phone}, Email: {email}")

def register_new_customer():
    username = input("Enter username: ")
    password = input("Enter password: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    
    if not username or not password or not address or not phone or not email:
        print("All fields are required.")
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
        file.write(f"{username},{password},Customer,{address},{phone},{email}\n")
    
    print(f"Customer {username} registered successfully.")

def borrow_book():
    customer_username = input('Enter the username: ')
    if not customer_username:
        print("Username is required.")
        return

    # Check if user exists and is a customer
    customer_found = False
    with open(userpath, 'r') as file:
        users = file.readlines()
    for user in users:
        details = user.strip().split(',')
        if details[0] == customer_username and details[2].lower() == 'customer':
            customer_found = True
            break
    if not customer_found:
        print("User not found or is not a customer.")
        return

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
        if book_name == title.strip().lower():
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
                        if uname == customer_username and bname.strip().lower() == title.strip().lower():
                            borrow_present = True
                            break

            if borrow_present:
                print(f"{customer_username} has already borrowed '{title}'.")
                return

            # Log the borrow
            with open(borrow_path, 'a') as borrow_file:
                borrow_file.write(f"{customer_username},{title},{book_id},1\n")
            print(f"{customer_username} borrowed 1 copy of '{title}'.")

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
    if not os.path.exists(borrow_path):
        print("No borrow history found.")
        return
    
    with open(borrow_path, 'r') as file:
        borrows = file.readlines()
    
    if not borrows:
        print("No borrow history found.")
        return
    
    print("Borrow History:")
    for borrow in borrows:
        username, title, book_id, quantity = borrow.strip().split(',')
        print(f"User: {username}, Book Title: {title}, Book ID: {book_id}, Quantity: {quantity}")

def staff_menu():
    while True:
        print("Staff Menu:")
        print("1. Add New Book")
        print("2. Register New Customer")
        print("3. View Books")
        print("4. View Customers")
        print("5. Borrowed Book")
        print("6. View Borrow History")
        print("7. Book Submit")
        print("8. Exit")
        
        choice= input("Enter your choice: ")
        if choice == '1':
            add_new_book()
        elif choice == '2':
            register_new_customer()
        elif choice == '3':
            view_books()
        elif choice == '4':
            view_customers()
        elif choice == '5':
            borrow_book()
        elif choice == '6':
            view_borrow_history()
        elif choice == '7':
            book_submit()
        elif choice == '8':
            print("Exiting Staff Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        if choice not in ['1', '2', '3', '4', '5','6','7','8']:
            print("Invalid choice. Please try again.")    

def book_submit():
    print()
    customer_username = input('Enter the username: ').strip()
    if not customer_username:
        print("Username is required.")
        return

    # Check user
    customer_found = False
    with open(userpath, 'r') as file:
        users = file.readlines()
    for user in users:
        details = user.strip().split(',')
        if details[0] == customer_username and details[2].lower() == 'customer':
            customer_found = True
            break
    if not customer_found:
        print("User not found or is not a customer.")
        return

    book_name = input("Enter the name of the book you want to submit: ").strip().lower()
    if not book_name:
        print("Book name is required.")
        return

    if not os.path.exists(borrow_path):
        print("No borrow records found.")
        return

    if not os.path.exists(book_path):
        print("Book records not found.")
        return

    # Read borrow records
    with open(borrow_path, 'r') as file:
        borrow_records = file.readlines()

    borrow_present = False
    updated_borrow_records = []
    book_id_to_return = ""
    for record in borrow_records:
        uname, bname, book_id, qty = record.strip().split(',')
        if uname == customer_username and bname.strip().lower() == book_name:
            borrow_present = True
            book_id_to_return = book_id
            # Not appending to updated list => effectively removing the borrow entry
        else:
            updated_borrow_records.append(record)

    if not borrow_present:
        print(f"{customer_username} has not borrowed '{book_name}'.")
        return

    # Update book quantity in books.txt
    with open(book_path, 'r') as file:
        book_lines = file.readlines()

    book_found = False
    updated_book_lines = []
    for line in book_lines:
        title, author, quantity_str, book_id = line.strip().split(',')
        if title.strip().lower() == book_name:
            book_found = True
            quantity = int(quantity_str)
            quantity += 1
            updated_book_lines.append(f"{title},{author},{quantity},{book_id}\n")
        else:
            updated_book_lines.append(line)

    if not book_found:
        print("Book not found in stock records.")
        return

    # Write updated book stock
    with open(book_path, 'w') as file:
        file.writelines(updated_book_lines)

    # Write updated borrow records
    with open(borrow_path, 'w') as file:
        file.writelines(updated_borrow_records)

    print(f"{customer_username} successfully submitted '{book_name.title()}'.")
 
def login_staff():
    print()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not os.path.exists(userpath):
        print("No users found.")
        return
    
    with open(userpath, 'r') as file:
        users = file.readlines()
    
    for user in users:
        user_details = user.strip().split(',')
        if user_details[0] == username and user_details[1] == password and user_details[2].lower() == 'staff':
            print(f"Welcome {username}!")
            login["username"] = username
            # Proceed to customer menu
            staff_menu()
            return True
    
    print("Invalid username or password.")
    return
    


    