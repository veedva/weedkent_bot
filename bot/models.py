# bot/models.py
from sqlalchemy import Column, Integer, Boolean, Date, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

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
    
    # Наши поля (совместимость с JSON)
    used_tips = Column(JSONB, default=list)
    used_triggers = Column(JSONB, default=list)
    used_distortions = Column(JSONB, default=list)
    used_facts = Column(JSONB, default=list)
    used_rage = Column(JSONB, default=list)
    used_anhedonia = Column(JSONB, default=list)
    achievements_received = Column(JSONB, default=list)
    
    # Поля от Грока (оставляем для совместимости)
    achievements = Column(JSONB, default=list)
    mood_history = Column(JSONB, default=list)
