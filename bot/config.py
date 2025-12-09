# config.py
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # Используем тот же ключ
KATHARSIS_WEBAPP_URL = "https://veedva.github.io/weedkent_bot/"

# ОТДЕЛЬНЫЙ файл для тестов!
DATA_FILE = os.getenv("DATA_FILE", "user_data_test.json")
LOCK_FILE = DATA_FILE + ".lock"
