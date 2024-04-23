# movies_service.py

from flask import Flask, jsonify
import json

app = Flask(__name__)

# Sample movie data for demonstration
with open('movies.json', 'r') as file:
    movies = json.load(file)

@app.route('/movies')
def get_movies():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True, port=8004)
