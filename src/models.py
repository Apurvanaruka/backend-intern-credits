from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

    credits = relationship("Credit", back_populates="user", uselist=False)

class Credit(Base):
    __tablename__ = "credits"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    credits = Column(Integer, default=0, nullable=False)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="credits")