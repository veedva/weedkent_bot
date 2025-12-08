from datetime import timedelta
from bot.database import AsyncSessionLocal
from bot.models import User
from bot.utils.time import today, now

async def get_user(user_id: int):
    async with AsyncSessionLocal() as session:
        user = await session.get(User, user_id)
        if not user:
            user = User(id=user_id)
            session.add(user)
            await session.commit()
        return user

async def save_user(user_id: int, updates: dict):
    async with AsyncSessionLocal() as session:
        user = await session.get(User, user_id)
        if not user:
            user = User(id=user_id, **updates)
            session.add(user)
        else:
            for key, value in updates.items():
                setattr(user, key, value)
        await session.commit()

def calculate_streak(start_date):
    if not start_date:
        return 0
    delta = today() - start_date
    return max(delta.days, 0)

def streak_text(days: int) -> str:
    if 11 <= days % 100 <= 19:
        return f"{days} дней"
    if days % 10 == 1:
        return f"{days} день"
    if days % 10 in (2, 3, 4):
        return f"{days} дня"
    return f"{days} дней"
