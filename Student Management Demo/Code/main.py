# Create a Python program for a student management system 
# where the admin can add, delete, update, and display student
# information using a menu-driven interface. 
# The system should store student data in a .txt file 
# and use functions to implement each feature.

# Here’s an example of how your menu-driven 
# student management system will look in text when run:

# Welcome to the Student Management System
# 1. Add Student
# 2. Delete Student
# 3. Update Student
# 4. Display Students
# 5. Exit
# Please choose an option (1-5): 

from student import add_student, delete_student, update_student, display_students

def menu():
    while True: 
        print("Welcome to the Student Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Display Students")
        print("5. Exit")
        option = input("Please choose an option (1-5): ")
        
        if option not in ['1', '2', '3', '4', '5']:
            print("Invalid option. Please try again.")
            continue
        
        if option == '1':
            add_student()
        elif option == '2':
            delete_student()
        elif option == '3':
            update_student()
        elif option == '4':
            display_students()
        elif option == '5':
            print("Exiting the system. Goodbye!")
            break
        
        
menu()     

