from db_connection import db

rooms = db["rooms"]

def add_room():
    rid = input("Enter Room ID: ")

    if rooms.find_one({"room_id": rid}):
        print("❌ Room already exists!")
        return

    capacity = int(input("Enter Capacity: "))

    rooms.insert_one({
        "room_id": rid,
        "capacity": capacity,
        "occupied": 0
    })

    print("✅ Room added successfully!")


def view_rooms():
    print("\n--- Rooms ---")
    for r in rooms.find():
        print(f"Room: {r['room_id']}, Capacity: {r['capacity']}, Occupied: {r['occupied']}")


def show_available_rooms():
    print("\n--- Available Rooms ---")
    for r in rooms.find():
        if r["occupied"] < r["capacity"]:
            print(f"Room: {r['room_id']}")


# ✅ Test Menu
def test_rooms():
    while True:
        print("\n--- Rooms Menu ---")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Show Available Rooms")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_room()
        elif choice == "2":
            view_rooms()
        elif choice == "3":
            show_available_rooms()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    test_rooms()