from datetime import datetime
import pytz

MOSCOW = pytz.timezone("Europe/Moscow")

def now():
    return datetime.now(MOSCOW)

def today():
    return now().date()
