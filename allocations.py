from db_connection import db

students = db["students"]
rooms = db["rooms"]
allocations = db["allocations"]

def allocate_room():
    sid = input("Enter Student ID: ")
    rid = input("Enter Room ID: ")

    student = students.find_one({"student_id": sid})
    room = rooms.find_one({"room_id": rid})

    if not student:
        print("❌ Student not found!")
        return

    if not room:
        print("❌ Room not found!")
        return

    if room["occupied"] >= room["capacity"]:
        print("❌ Room is full!")
        return

    allocations.insert_one({
        "student_id": sid,
        "room_id": rid
    })

    rooms.update_one(
        {"room_id": rid},
        {"$inc": {"occupied": 1}}
    )

    print("✅ Room allocated!")


def view_allocations():
    print("\n--- Allocations ---")
    for a in allocations.find():
        print(f"Student: {a['student_id']} → Room: {a['room_id']}")


# ✅ Test Menu
def test_allocations():
    while True:
        print("\n--- Allocation Menu ---")
        print("1. Allocate Room")
        print("2. View Allocations")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            allocate_room()
        elif choice == "2":
            view_allocations()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    test_allocations()