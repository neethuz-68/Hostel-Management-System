from db_connection import db

# Access collection
students = db["students"]

# ➤ Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    phone = input("Enter Phone: ")

    student = {
        "student_id": sid,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    students.insert_one(student)
    print("✅ Student added successfully!")

# ➤ View Students
def view_students():
    print("\n--- Student List ---")
    for s in students.find():
        print(f"ID: {s['student_id']}, Name: {s['name']}, Age: {s['age']}, Phone: {s['phone']}")

# ➤ Simple Test Runner
def test_students():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

# Run this file directly for testing
if __name__ == "__main__":
    test_students()