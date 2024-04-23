import redis

try:
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('messages')

    print("Subscriber connected to Redis and subscribed to 'messages' channel.")

    for message in pubsub.listen():
        if message['type'] == 'message':
            print("Received message:", message['data'].decode('utf-8'))

except Exception as e:
    print("An error occurred:", e)
