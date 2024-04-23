# showtimes_service.py

from flask import Flask, jsonify
import json
app = Flask(__name__)

# Read showtimes data from showtimes.json file
with open('showtimes.json', 'r') as file:
    showtimes = json.load(file)


@app.route('/showtimes')
def get_showtimes():
    return jsonify(showtimes)

if __name__ == '__main__':
    app.run(debug=True, port=8002)
