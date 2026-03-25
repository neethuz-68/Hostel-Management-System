from db_connection import db

payments = db["payments"]
students = db["students"]

def make_payment():
    sid = input("Enter Student ID: ")

    if not students.find_one({"student_id": sid}):
        print("❌ Student not found!")
        return

    amount = float(input("Enter Amount: "))
    status = input("Enter Status (paid/pending): ")

    payments.insert_one({
        "student_id": sid,
        "amount": amount,
        "status": status.lower()
    })

    print("✅ Payment recorded!")


def view_payments():
    print("\n--- Payments ---")
    for p in payments.find():
        print(f"Student: {p['student_id']}, Amount: {p['amount']}, Status: {p['status']}")


def show_pending():
    print("\n--- Pending Payments ---")
    for p in payments.find({"status": "pending"}):
        print(f"Student: {p['student_id']}, Amount: {p['amount']}")


# ✅ Test Menu
def test_payments():
    while True:
        print("\n--- Payments Menu ---")
        print("1. Make Payment")
        print("2. View Payments")
        print("3. Show Pending")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            make_payment()
        elif choice == "2":
            view_payments()
        elif choice == "3":
            show_pending()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    test_payments()