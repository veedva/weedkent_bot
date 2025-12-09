# bot/config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# URL для WebApp
KATHARSIS_WEBAPP_URL = "https://veedva.github.io/weedkent_bot/"

# Файл с данными (для совместимости со старым ботом)
DATA_FILE = os.getenv("DATA_FILE", "user_data_test.json")
LOCK_FILE = DATA_FILE + ".lock"

# Настройки базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Настройки Redis
REDIS_URL = os.getenv("REDIS_URL")

# Таймзона
MOSCOW_TZ = "Europe/Moscow"
