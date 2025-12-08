from datetime import date
from sqlalchemy import Column, BigInteger, Date, Boolean, Integer, JSON, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    start_date = Column(Date, nullable=True)
    active = Column(Boolean, default=False)
    best_streak = Column(Integer, default=0)
    hold_count_today = Column(Integer, default=0)
    last_hold_date = Column(Date, nullable=True)
    last_hold_time = Column(DateTime, nullable=True)
    achievements = Column(JSON, default=list)  # список полученных достижений
    mood_history = Column(JSON, default=list)  # [(date, mood_1_10), ...]
    # остальные поля можно добавить позже
