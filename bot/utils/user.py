from bot.models import User
from bot.database import AsyncSessionLocal
from bot.utils.time import today
from sqlalchemy import select

async def get_user(user_id: int) -> User:
    async with AsyncSessionLocal() as session:
        user = await session.get(User, user_id)
        if not user:
            user = User(id=user_id)
            session.add(user)
            await session.commit()
        return user

async def save_user(user: User):
    """Сохраняет объект User в базе"""
    async with AsyncSessionLocal() as session:
        session.add(user)
        await session.commit()

# Заглушка — потом сделаем настоящие рассылки
async def schedule_jobs(user_id: int, bot):
    print(f"Рассылки включены для пользователя {user_id}")

def calculate_streak(start_date):
    if not start_date:
        return 0
    return max((today() - start_date).days, 0)

def streak_text(days: int) -> str:
    if days == 0:
        return "0 дней"
    if 11 <= days % 100 <= 19:
        return f"{days} дней"
    if days % 10 == 1:
        return f"{days} день"
    if days % 10 in (2, 3, 4):
        return f"{days} дня"
    return f"{days} дней"
