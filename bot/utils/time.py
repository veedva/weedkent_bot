# bot/utils/time.py
"""
Утилиты для работы со временем
"""

import pytz
from datetime import datetime, date

MOSCOW_TZ = pytz.timezone('Europe/Moscow')

def get_current_time() -> datetime:
    """Текущее время в московском часовом поясе"""
    return datetime.now(MOSCOW_TZ)

def get_current_date() -> date:
    """Текущая дата в московском часовом поясе"""
    return get_current_time().date()

def format_days(days: int) -> str:
    """Форматирование дней с правильным склонением"""
    if days == 0:
        return "0 дней"
    
    if 11 <= days % 100 <= 19:
        return f"{days} дней"
    
    last_digit = days % 10
    if last_digit == 1:
        return f"{days} день"
    elif last_digit in [2, 3, 4]:
        return f"{days} дня"
    
    return f"{days} дней"

def get_days_since_start(start_date_str: str) -> int:
    """Возвращает количество ПОЛНЫХ дней трезвости"""
    if not start_date_str:
        return 0
    
    try:
        start = date.fromisoformat(start_date_str)
        current = get_current_date()
        days = (current - start).days
        return max(days, 0)
    except Exception:
        return 0
