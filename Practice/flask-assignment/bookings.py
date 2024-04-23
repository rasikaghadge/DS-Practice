# bookings_service.py

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('bookings.json', 'r') as file:
    bookings = json.load(file)

def save_bookings_data():
    with open('bookings.json', 'w') as file:
        json.dump(bookings, file, indent=4)

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings)

@app.route('/bookings', methods=['POST'])
def book_show():
    data = request.json
    booking_id = len(bookings) + 1 
    new_booking = {
        "id": booking_id,
        "user_id": data.get("user_id"),
        "showtime_id": data.get("showtime_id"),
        "tickets": data.get("tickets")
    }
    bookings.append(new_booking)
    save_bookings_data()  # Save updated bookings data to the file
    return jsonify({"message": "Booking successful", "booking_id": booking_id}), 201

if __name__ == '__main__':
    app.run(port=8003, debug=True)
