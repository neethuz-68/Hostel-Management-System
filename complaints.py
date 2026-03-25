from db_connection import db

complaints = db["complaints"]
students = db["students"]

def add_complaint():
    sid = input("Enter Student ID: ")

    if not students.find_one({"student_id": sid}):
        print("❌ Student not found!")
        return

    text = input("Enter Complaint: ")

    complaints.insert_one({
        "student_id": sid,
        "complaint": text,
        "status": "open"
    })

    print("✅ Complaint added!")


def view_complaints():
    print("\n--- Complaints ---")
    for c in complaints.find():
        print(f"Student: {c['student_id']}, Complaint: {c['complaint']}, Status: {c['status']}")


def update_status():
    sid = input("Enter Student ID: ")
    status = input("Enter new status (resolved/open): ")

    result = complaints.update_one(
        {"student_id": sid},
        {"$set": {"status": status}}
    )

    if result.modified_count > 0:
        print("✅ Status updated!")
    else:
        print("❌ Complaint not found!")


# ✅ Test Menu
def test_complaints():
    while True:
        print("\n--- Complaints Menu ---")
        print("1. Add Complaint")
        print("2. View Complaints")
        print("3. Update Status")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            update_status()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    test_complaints()