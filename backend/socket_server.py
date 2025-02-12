import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",
)

socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def root():
    return {"message": "Socket.IO server is running"}

@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connected")
    await sio.emit("message", {"user": "server", "text": "Привет!"}, to=sid)

@sio.event
async def message(sid, data):
    print(f"Message from {sid}: {data}")
    await sio.emit("message", data)

@sio.event
async def disconnect(sid):
    print(f"Client {sid} disconnected")

if __name__ == "__main__":
    uvicorn.run(socket_app, host="0.0.0.0", port=8001)