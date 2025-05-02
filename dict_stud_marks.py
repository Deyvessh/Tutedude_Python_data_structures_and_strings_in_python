

stud_marks = {}

while True:
    print("\nOptions:\n1. Add student\n2. View student's marks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        stud_name = input("Enter the student's name: ")
        marks = input(f"{stud_name}'s marks: ")
        stud_marks[stud_name] = marks

    elif choice == '2':
        stud_name = input("Enter the student's name: ")
        if stud_name in stud_marks:
            print(f"{stud_name}'s marks: {stud_marks}")
        else:
            print('Student not found.')

    elif choice == '3':
        break

    else:
        print("Invalid choice.")



