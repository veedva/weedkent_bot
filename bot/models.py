from sqlalchemy import Column, Integer, Boolean, Date, DateTime, JSON, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    active = Column(Boolean, default=False)
    start_date = Column(Date, nullable=True)
    best_streak = Column(Integer, default=0)
    hold_count_today = Column(Integer, default=0)
    last_hold_date = Column(Date, nullable=True)
    last_hold_time = Column(DateTime, nullable=True)
    achievements = Column(JSON, default=list)
    mood_history = Column(JSON, default=list)  # [(date, mood_1_10)]
