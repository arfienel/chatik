from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_message(chat_id: int, user: str, text: str, db: Session = Depends(get_db)):
    message = Message(chat_id=chat_id, user=user, text=text)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message