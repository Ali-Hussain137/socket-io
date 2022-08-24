import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/':'./public/'
})


@sio.event
async def connect(sid, environ):
    print(sid, 'connected')
    
    
@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')
    
@sio.event
async def sum(sid, data):
    result = data['number'][0] + data['number'][1]
    await sio.emit('sum_result', {'result':result}, to=sid)