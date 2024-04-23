import requests
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_movie_list():
    clear_screen()
    response = requests.get('http://localhost:8004/movies')
    movies = response.json()
    print("Movie List:")
    for movie in movies:
        print(f"ID: {movie['id']}, Title: {movie['title']}")

def get_showtimes():
    clear_screen()
    response = requests.get('http://localhost:8002/showtimes')
    showtimes = response.json()
    print("Showtimes:")
    for showtime in showtimes:
        print(f"ID: {showtime['id']}, Movie ID: {showtime['movie_id']}, Time: {showtime['time']}")

def get_bookings_info():
    clear_screen()
    response = requests.get('http://localhost:8003/bookings')
    bookings = response.json()
    print("Bookings Info:")
    for booking in bookings:
        print(f"ID: {booking['id']}, User ID: {booking['user_id']}, Showtime ID: {booking['showtime_id']}, Tickets: {booking['tickets']}")

def get_user_list():
    clear_screen()
    response = requests.get('http://localhost:8001/users')
    users = response.json()
    print("User List:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}")

def book_show(user_id, showtime_id, tickets):
    data = {
        "user_id": user_id,
        "showtime_id": showtime_id,
        "tickets": tickets
    }
    response = requests.post('http://localhost:8003/bookings', json=data)
    if response.status_code == 201:
        print("Booking successful!")
    else:
        print("Booking failed.")

while True:
    print("\nMenu:")
    print("1. Get Movie List")
    print("2. Get Show Times")
    print("3. Get Bookings Info")
    print("4. Get User List")
    print("5. Book a Show")
    print("6. Clear Screen")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        get_movie_list()
    elif choice == '2':
        get_showtimes()
    elif choice == '3':
        get_bookings_info()
    elif choice == '4':
        get_user_list()
    elif choice == '5':
        user_id = int(input("Enter User ID: "))
        showtime_id = int(input("Enter Showtime ID: "))
        tickets = int(input("Enter Number of Tickets: "))
        book_show(user_id, showtime_id, tickets)
    elif choice == '6':
        clear_screen()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
