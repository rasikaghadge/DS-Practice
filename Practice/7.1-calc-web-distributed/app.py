from flask import Flask, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def hello():
    redis_client.publish('messages', 'Hello, World!')
    return jsonify({'message': 'Message sent to subscribers'})

if __name__ == '__main__':
    app.run(debug=True)