from db_connection import db
from pymongo.errors import DuplicateKeyError


students = db["students"]
rooms=db["rooms"]
allocations = db["allocations"]
payments = db["payments"]
complaints = db["complaints"]

students.create_index("student_id", unique=True)

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

    try:
        students.insert_one(student)
        print("Student added successfully!")
    except DuplicateKeyError:
        print("Student ID already exists!")


# ➤ View Students
def view_students():
    print("\n--- Student List ---")

    data = students.find()

    found = False
    for s in data:
        found = True
        print(f"ID: {s['student_id']}, Name: {s['name']}, Age: {s['age']}, Phone: {s['phone']}")

    if not found:
        print("No students found.")


# ➤ Delete Student
def delete_student():
    sid = input("Enter Student ID to delete: ")

    student = students.find_one({"student_id": sid})
    if not student:
        print("❌ Student not found!")
        return

    # Find all allocations of this student
    student_allocs = allocations.find({"student_id": sid})

    for alloc in student_allocs:
        rid = alloc["room_id"]

        rooms.update_one(
            {"room_id": rid},
            {"$inc": {"occupied": -1}}
        )

    students.delete_one({"student_id": sid})
    allocations.delete_many({"student_id": sid})
    payments.delete_many({"student_id": sid})
    complaints.delete_many({"student_id": sid})

    print("Student deleted successfully!")


# ➤ Search Student
def search_student():
    sid = input("Enter Student ID to search: ")

    s = students.find_one({"student_id": sid})

    if s:
        print("\n--- Student Found ---")
        print(f"ID: {s['student_id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Gender: {s['gender']}")
        print(f"Phone: {s['phone']}")
    else:
        print("Student not found!")


# ➤ Update Student
def update_student():
    sid = input("Enter Student ID to update: ")

    s = students.find_one({"student_id": sid})

    if not s:
        print("Student not found!")
        return

    print("Leave blank to keep old value")

    name = input(f"Enter new name ({s['name']}): ")
    age = input(f"Enter new age ({s['age']}): ")
    gender = input(f"Enter new gender ({s['gender']}): ")
    phone = input(f"Enter new phone ({s['phone']}): ")

    updated_data = {
        "name": name if name else s["name"],
        "age": int(age) if age else s["age"],
        "gender": gender if gender else s["gender"],
        "phone": phone if phone else s["phone"]
    }

    students.update_one(
        {"student_id": sid},
        {"$set": updated_data}
    )

    print("Student updated successfully!")


# ➤ Test Menu (for this file only)
def test_students():
    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    test_students()