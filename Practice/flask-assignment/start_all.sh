#!/bin/bash

# Start user service on port 8001
echo "Starting User Service on port 8001"
python user.py &

# Start showtimes service on port 8002
echo "Starting Showtimes Service on port 8002"
python showtimes.py &

# Start bookings service on port 8003
echo "Starting Bookings Service on port 8003"
python bookings.py &

# Start movies service on port 8004
echo "Starting Movies Service on port 8004"
python movies.py &

echo "All services started successfully"
