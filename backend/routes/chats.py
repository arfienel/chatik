from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Chat

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_chats(db: Session = Depends(get_db)):
    return db.query(Chat).all()

@router.post("/")
def create_chat(name: str, db: Session = Depends(get_db)):
    new_chat = Chat(name=name)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat