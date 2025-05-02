# Python Tasks - Student Marks Management & List Manipulation

This repository contains two simple Python scripts that demonstrate fundamental programming concepts:
- Task 1: Managing a dictionary of student marks through a menu-based system.
- Task 2: Working with lists to extract and reverse elements.

---

## Task 1: Student Marks Management System

### 📋 Description

This task is a console-based application designed to add and retrieve students' marks using a dictionary in Python. It demonstrates:
- Use of a dictionary for key-value storage
- Infinite loop for menu-driven logic
- Basic conditionals (`if`, `elif`, `else`)
- User input handling

### 🧠 Key Concepts

- `Dictionary`: Used to store student names as keys and their marks as values.
- `Infinite Loop`: A `while True` loop ensures the menu keeps showing until the user exits.
- `Conditional Statements`: To handle various menu options.
- `Input/Output`: For interacting with the user.

### 💻 Code Walkthrough

```python
stud_marks = {}  # Dictionary to store student names and their corresponding marks

while True:
    print("\nOptions:\n1. Add student\n2. View student's marks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        stud_name = input("Enter the student's name: ")
        marks = input(f"{stud_name}'s marks: ")
        stud_marks[stud_name] = marks  # Add student and marks to dictionary

    elif choice == '2':
        stud_name = input("Enter the student's name: ")
        if stud_name in stud_marks:
            print(f"{stud_name}'s marks: {stud_marks[stud_name]}")
        else:
            print('Student not found.')

    elif choice == '3':
        break  # Exit the loop and program

    else:
        print("Invalid choice.")  # Handle invalid input
```

### ✅ Example Usage

```
Options:
1. Add student
2. View student's marks
3. Exit
Enter choice: 1
Enter the student's name: Alice
Alice's marks: 89

Options:
1. Add student
2. View student's marks
3. Exit
Enter choice: 2
Enter the student's name: Alice
Alice's marks: 89
```

---

## Task 2: List Slicing and Reversal

### 📋 Description

This task demonstrates how to:
- Create a list of numbers
- Slice the first five elements
- Reverse the sliced portion

### 🧠 Key Concepts

- `List Creation`: Using `range()` to generate a list from 1 to 10.
- `List Slicing`: Extracting a subset of elements.
- `List Reversal`: Using slicing syntax to reverse elements.

### 💻 Code Walkthrough

```python
original_list = list(range(1, 11))  # List from 1 to 10
print('Original list:', original_list)

first_five_elements = original_list[:5]  # Slicing first 5 elements
print('Extracted first five elements:', first_five_elements)

reverse_first_five_elements = first_five_elements[::-1]  # Reversing the sliced list
print('Reversed first five elements:', reverse_first_five_elements)
```

### ✅ Example Output

```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed first five elements: [5, 4, 3, 2, 1]
```

---

## 📚 Conclusion

These two tasks are excellent introductory examples for understanding data structures (like dictionaries and lists), input/output operations, and control structures in Python. They form the foundation for building more complex applications.

---
