from students import *
from rooms import *
from allocations import *
from payments import *
from complaints import *

def main():
    while True:
        print("\n========== HOSTEL MANAGEMENT SYSTEM ==========")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Room Allocation")
        print("4. Payments")
        print("5. Complaints")
        print("6. Exit")

        choice = input("Enter choice: ")

        # ---------------- STUDENT MENU ----------------
        if choice == "1":
            while True:
                print("\n--- Student Menu ---")
                print("1. Add Student")
                print("2. View Students")
                print("3. Delete Student")
                print("4. Search Student")
                print("5. Update Student")
                print("6. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    add_student()
                elif ch == "2":
                    view_students()
                elif ch == "3":
                    delete_student()
                elif ch == "4":
                    search_student()
                elif ch == "5":
                    update_student()
                elif ch == "6":
                    break
                else:
                    print("Invalid choice!")

        # ---------------- ROOM MENU ----------------
        elif choice == "2":
            while True:
                print("\n--- Room Menu ---")
                print("1. Add Room")
                print("2. View Rooms")
                print("3. Show Available Rooms")
                print("4. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    add_room()
                elif ch == "2":
                    view_rooms()
                elif ch == "3":
                    show_available_rooms()
                elif ch == "4":
                    break
                else:
                    print("Invalid choice!")

        # ---------------- ALLOCATION MENU ----------------
        elif choice == "3":
            while True:
                print("\n--- Allocation Menu ---")
                print("1. Allocate Room")
                print("2. View Allocations")
                print("3. Deallocate Room")
                print("4. View Rooms.")
                print("5. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    allocate_room()
                elif ch == "2":
                    view_allocations()
                elif ch == "3":
                    deallocate_room()
                elif ch == "4":
                    view_rooms()
                elif ch=='5':
                    break
                else:
                    print("Invalid choice!")

        # ---------------- PAYMENTS MENU ----------------
        elif choice == "4":
            while True:
                print("\n--- Payments Menu ---")
                print("1. Make Payment")
                print("2. View Payments")
                print("3. Show Pending Payments")
                print("4.Back.")
                

                ch = input("Enter choice: ")

                if ch == "1":
                    make_payment()
                elif ch == "2":
                    view_payments()
                elif ch == "3":
                    show_pending()
                elif ch == "4":
                    break
                else:
                    print("Invalid choice!")

        # ---------------- COMPLAINTS MENU ----------------
        elif choice == "5":
            while True:
                print("\n--- Complaints Menu ---")
                print("1. Add Complaint")
                print("2. View Complaints")
                print("3. Update Complaint Status")
                print("4. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    add_complaint()
                elif ch == "2":
                    view_complaints()
                elif ch == "3":
                    update_status()
                elif ch == "4":
                    print("Exiting.")
                    break
                else:
                    print("Invalid choice!")

        # ---------------- EXIT ----------------
        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")

# Run the system
if __name__ == "__main__":
    main() 