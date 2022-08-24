import random
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})

client_count = 0
a_count = 0
b_count = 0


def task(sid):
    sio.sleep(5)
    result = sio.call('mult', {'numbers': [3, 4]}, to=sid)
    print(result)


@sio.event
def connect(sid, environ):
    print(sid, 'connected')
    sio.start_background_task(task, sid)

    global client_count
    client_count += 1
    sio.emit('client_count', client_count)
    global a_count
    global b_count
    if random.random() > 0.5:
        sio.enter_room(sid, 'a')
        a_count += 1
        sio.emit('room_count', a_count, to='a')
    else:
        sio.enter_room(sid, 'b')
        b_count += 1
        sio.emit('room_count', b_count, to='b')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')
    global client_count
    global a_count
    global b_count

    client_count -= 1
    sio.emit('client_count', client_count)
    if 'a' in sio.rooms(sid):
        a_count -= 1
        sio.emit('room_count', a_count, to='a')
    else:
        b_count -= 1
        sio.emit('room_count', b_count, to='b')


@sio.event
def sum(sid, data):
    result = data['number'][0] + data['number'][1]
    return result
    # sio.emit('sum_result', {'result':result}, to=sid)
