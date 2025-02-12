from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chats, messages
import socketio
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chats.router, prefix="/chats", tags=["chats"])
app.include_router(messages.router, prefix="/messages", tags=["messages"])

sio = socketio.AsyncServer(cors_allowed_origins="*")
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

if __name__ == "__main__":
    uvicorn.run(sio_app, host="0.0.0.0", port=8000)