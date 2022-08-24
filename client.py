import asyncio
import sys
import socketio


sio = socketio.Client()

sio.connect('http://localhost:8000')

@sio.event
def connect():
    print("Connected")
    result = sio.call("sum", {"number": [1, 2]})
    print(result)


@sio.event
def disconnect():
    print("Disconnected")


@sio.event
def connect_error(e):
    print(e)


@sio.event
def sum_result(data):
    print(data)


@sio.event
def mult(data):
    return data['numbers'][0] * data['numbers'][1]


@sio.event
def client_count(clientCount):
    print(f"There are {clientCount} client connected")


@sio.event
def room_count(count):
    print(f"There are {count} client connected in room")



