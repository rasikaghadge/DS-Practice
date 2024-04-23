# user_service.py
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Read user data from users.json file
with open('user.json', 'r') as file:
    users = json.load(file)

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
