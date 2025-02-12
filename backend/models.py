from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    messages = relationship("Message", back_populates="chat")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    text = Column(String)
    chat_id = Column(Integer, ForeignKey("chats.id"))

    chat = relationship("Chat", back_populates="messages")