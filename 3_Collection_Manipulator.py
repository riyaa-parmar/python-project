students = {}

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = tuple(input("Enter Date of Birth (YYYY-MM-DD): ").split("-"))

    subjects = set(input("Enter subjects (comma separated): ").split(","))

    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": subjects
    }

    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records available.\n")
        return

    for sid, info in students.items():
        print(f"\nStudent ID: {sid}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Grade: {info['grade']}")
        print(f"Date of Birth (Immutable Tuple): {info['dob']}")
        print(f"Subjects: {', '.join(info['subjects'])}")

def update_student():
    sid = int(input("Enter Student ID to update: "))
    if sid in students:
        students[sid]["grade"] = input("Enter new grade: ")
        print("Student information updated.\n")
    else:
        print("Student not found.\n")

def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    if sid in students:
        del students[sid]
        print("Student record deleted.\n")
    else:
        print("Student not found.\n")

def display_subjects():
    all_subjects = set()
    for info in students.values():
        all_subjects.update(info["subjects"])
    print("Subjects Offered:", ", ".join(all_subjects), "\n")

def menu():
    print("Welcome to the Student Data Organizer!")
    while True:
        print("""
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            print("Thank you for using the Student Data Organizer. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

menu()