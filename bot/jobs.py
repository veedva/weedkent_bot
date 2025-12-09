from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import time
import pytz
from bot.utils.user import get_all_active_users
from bot.texts import MORNING_MESSAGES, EVENING_MESSAGES, NIGHT_MESSAGES
import random

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

async def morning_job(bot):
    users = await get_all_active_users()
    msg = random.choice(MORNING_MESSAGES)
    for user_id in users:
        try:
            await bot.send_message(user_id, msg)
        except:
            pass

async def evening_job(bot):
    users = await get_all_active_users()
    msg = random.choice(EVENING_MESSAGES)
    for user_id in users:
        try:
            await bot.send_message(user_id, msg)
        except:
            pass

async def night_job(bot):
    users = await get_all_active_users()
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
