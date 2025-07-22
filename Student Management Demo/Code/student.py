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

import os

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    # checking if the ID is numeric or not
    if not id.isdigit():
        print("Invalid ID. Please enter a numeric value.")
        return
    # checking if the file exists and if the ID already exists in the file
    if os.path.exists("E:\\Documents\\Python\\SMS\\File\\students.txt"):
        with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(id + ","):
                    print("Student ID already exists. Please use a different ID.")
                    return
    # if the file does not exist, it will be created
    with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "a") as file:
        file.write(f"{id},{name},{age},{grade}\n")
    print("Student added successfully!")

def delete_student():
    # checking if the file exists before trying to delete a student
    if os.path.exists("E:\\Documents\\Python\\SMS\\File\\students.txt"):
        id = input("Enter student id to delete: ")
        
        # checking if the ID is numeric or not
        if not id.isdigit():
            print("Invalid ID. Please enter a numeric value.")
            return
        
        
        
        # reading the file and checking if the ID exists
        with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "r") as file:
            lines = file.readlines()
            
        # checking if the ID exists in the file
        if id + "," not in " ".join(lines):
            print("Student ID not found.")
            return
        
        # checking if the ID exists in the file
        with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "w") as file:
            for line in lines:
                if not line.startswith(id + ","):
                    file.write(line)
        print("Student deleted successfully!")
    else:
        print("No student records found. Please add students first.")

def update_student():
    # checking if the file exists before trying to update a student
    if os.path.exists("E:\\Documents\\Python\\SMS\\File\\students.txt"):
        id = input("Enter student id to update: ")
        # checking if the ID is numeric or not
        if not id.isdigit():
            print("Invalid ID. Please enter a numeric value.")
            return
        # reading the file and checking if the ID exists
        with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "r") as file:
            lines = file.readlines()
        # checking if the ID exists in the file
        if id + "," not in " ".join(lines):
            print("Student ID not found.")
            return
        # updating the student information 
        with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "w") as file:
            for line in lines:
                if line.startswith(id + ","):
                    new_name = input("Enter new student name: ")
                    new_age = input("Enter new student age: ")
                    new_grade = input("Enter new student grade: ")
                    file.write(f"{id},{new_name},{new_age},{new_grade}\n")
                else:
                    file.write(line)
        print("Student updated successfully!")
    else:
        print("No student records found. Please add students first.")

def display_students():
    # checking if the file exists before trying to display students
    if os.path.exists("E:\\Documents\\Python\\SMS\\File\\students.txt"):
        # reading the file and displaying the student information
        with open("E:\\Documents\\Python\\SMS\\File\\students.txt", "r") as file:
            lines = file.readlines()
            # checking if the file is empty
            if not lines:
                print("No students found.")
                return
            print("Student Information:")
            for line in lines:
                id, name, age, grade = line.strip().split(",")
                print(f"Id: {id}, Name: {name}, Age: {age}, Grade: {grade}")
    else:
        print("No student records found. Please add students first.")            
