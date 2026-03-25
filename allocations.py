# from db_connection import db

# students = db["students"]
# rooms = db["rooms"]
# allocations = db["allocations"]

# def allocate_room():
#     sid = input("Enter Student ID: ")
#     rid = input("Enter Room ID: ")

#     student = students.find_one({"student_id": sid})
#     room = rooms.find_one({"room_id": rid})

#     if not student:
#         print("❌ Student not found!")
#         return

#     if not room:
#         print("❌ Room not found!")
#         return

#     if room["occupied"] >= room["capacity"]:
#         print("❌ Room is full!")
#         return

#     allocations.insert_one({
#         "student_id": sid,
#         "room_id": rid
#     })

#     rooms.update_one(
#         {"room_id": rid},
#         {"$inc": {"occupied": 1}}
#     )

#     print("✅ Room allocated!")


# def view_allocations():
#     print("\n--- Allocations ---")
#     for a in allocations.find():
#         print(f"Student: {a['student_id']} → Room: {a['room_id']}")


# # ✅ Test Menu
# def test_allocations():
#     while True:
#         print("\n--- Allocation Menu ---")
#         print("1. Allocate Room")
#         print("2. View Allocations")
#         print("3. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             allocate_room()
#         elif choice == "2":
#             view_allocations()
#         elif choice == "3":
#             break
#         else:
#             print("Invalid choice!")


# if __name__ == "__main__":
#     test_allocations()


from db_connection import db

students = db["students"]
rooms = db["rooms"]
allocations = db["allocations"]


# 🔹 Allocate Room
def allocate_room():
    sid = input("Enter Student ID: ").strip()
    rid = input("Enter Room ID: ").strip()

    if not sid or not rid:
        print("❌ Invalid input!")
        return

    student = students.find_one({"student_id": sid})
    room = rooms.find_one({"room_id": rid})

    if not student:
        print("❌ Student not found!")
        return

    if not room:
        print("❌ Room not found!")
        return

    # ✅ Prevent duplicate allocation
    existing = allocations.find_one({"student_id": sid})
    if existing:
        print("❌ Student already has a room!")
        return

    # ✅ Check room capacity safely
    if room.get("occupied", 0) >= room.get("capacity", 0):
        print("❌ Room is full!")
        return

    # ✅ Insert allocation
    allocations.insert_one({
        "student_id": sid,
        "room_id": rid
    })

    # ✅ Update room occupancy
    rooms.update_one(
        {"room_id": rid},
        {"$inc": {"occupied": 1}}
    )

    print(f"✅ Room {rid} allocated to {student.get('name', 'Student')}!")


# 🔹 View Allocations
def view_allocations():
    print("\n--- Allocations ---")

    found = False
    for a in allocations.find():
        student = students.find_one({"student_id": a["student_id"]})
        room = rooms.find_one({"room_id": a["room_id"]})

        student_name = student.get("name", "Unknown") if student else "Unknown"

        print(f"Student: {student_name} ({a['student_id']}) → Room: {a['room_id']}")
        found = True

    if not found:
        print("No allocations found.")


# 🔹 Deallocate Room (NEW FEATURE ⭐)
def deallocate_room():
    sid = input("Enter Student ID: ").strip()

    if not sid:
        print("❌ Invalid input!")
        return

    allocation = allocations.find_one({"student_id": sid})

    if not allocation:
        print("❌ No allocation found!")
        return

    rid = allocation["room_id"]

    # Delete allocation
    allocations.delete_one({"student_id": sid})

    # Decrease room occupancy
    rooms.update_one(
        {"room_id": rid},
        {"$inc": {"occupied": -1}}
    )

    print(f"✅ Room {rid} deallocated from Student {sid}!")


# 🔹 View Rooms Status (BONUS ⭐)
def view_rooms():
    print("\n--- Room Status ---")

    for room in rooms.find():
        print(
            f"Room: {room['room_id']} | Capacity: {room.get('capacity', 0)} | "
            f"Occupied: {room.get('occupied', 0)}"
        )


# 🔹 Test Menu
def test_allocations():
    while True:
        print("\n--- Allocation Menu ---")
        print("1. Allocate Room")
        print("2. View Allocations")
        print("3. Deallocate Room")
        print("4. View Rooms")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            allocate_room()
        elif choice == "2":
            view_allocations()
        elif choice == "3":
            deallocate_room()
        elif choice == "4":
            view_rooms()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!")


# 🔹 Run Program
if __name__ == "__main__":
    test_allocations()