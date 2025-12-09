# bot/jobs.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz
from bot.utils.user import get_active_users, check_and_give_achievements
from bot.texts import MORNING_MESSAGES, EVENING_MESSAGES, NIGHT_MESSAGES
import random

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

async def morning_job(bot):
    users = get_active_users()
    for user_id in users:
        try:
            # 1. Отправляем утреннее сообщение
            msg = random.choice(MORNING_MESSAGES)
            await bot.send_message(user_id, msg)
            
            # 2. Проверяем и выдаём достижения
            new_achievements = await check_and_give_achievements(user_id)
            for day_num, achievement in new_achievements:
                await bot.send_message(
                    user_id,
                    f"{achievement['emoji']} **НОВОЕ ДОСТИЖЕНИЕ!** {achievement['emoji']}\n\n"
                    f"**{achievement['title']}**\n"
                    f"{achievement['description']}\n\n"
                    f"{achievement['message']}\n\n"
                    f"🎯 День: {day_num}",
                    parse_mode="Markdown"
                )
        except:
            pass

async def evening_job(bot):
    users = get_active_users()
    msg = random.choice(EVENING_MESSAGES)
    for user_id in users:
        try:
            await bot.send_message(user_id, msg)
        except:
            pass

async def night_job(bot):
    users = get_active_users()
    msg = random.choice(NIGHT_MESSAGES)
    for user_id in users:
        try:
            await bot.send_message(user_id, msg)
        except:
            pass

async def start_scheduler(bot):
    scheduler.add_job(morning_job, "cron", hour=9, minute=0, args=[bot])
    scheduler.add_job(evening_job, "cron", hour=18, minute=0, args=[bot])
    scheduler.add_job(night_job, "cron", hour=23, minute=0, args=[bot])
    scheduler.start()
    print("Рассылки запущены: 9:00 / 18:00 / 23:00 МСК")
