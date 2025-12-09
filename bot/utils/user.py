# bot/utils/user.py
"""
Утилиты для работы с пользователями (JSON-версия для совместимости)
"""

import json
import os
import asyncio
from filelock import FileLock
from typing import Dict, Any, Optional

from bot.config import DATA_FILE, LOCK_FILE

_user_data_cache = None

def load_data() -> Dict[str, Any]:
    """Загрузить данные из файла"""
    global _user_data_cache
    
    if _user_data_cache is not None:
        return _user_data_cache
    
    with FileLock(LOCK_FILE):
        if not os.path.exists(DATA_FILE):
            _user_data_cache = {}
            return {}
        
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                _user_data_cache = json.load(f)
                return _user_data_cache
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")
            _user_data_cache = {}
            return {}

async def save_data():
    """Сохранить данные в файл"""
    global _user_data_cache
    if _user_data_cache is None:
        return
    
    with FileLock(LOCK_FILE):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(_user_data_cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка сохранения данных: {e}")

def get_user(user_id: int) -> Dict[str, Any]:
    """Получить данные пользователя, создать если нет"""
    data = load_data()
    uid = str(user_id)
    
    if uid not in data:
        data[uid] = {
            "start_date": None,
            "active": False,
            "best_streak": 0,
            "hold_count_today": 0,
            "last_hold_date": None,
            "last_hold_time": None,
            "used_tips": [],
            "used_triggers": [],
            "used_distortions": [],
            "used_facts": [],
            "used_rage": [],
            "used_anhedonia": [],
            "achievements_received": []
        }
        _user_data_cache.update(data)
        asyncio.create_task(save_data())
    
    return data[uid]

async def save_user(user_id: int, updates: Optional[Dict[str, Any]] = None):
    """Сохранить изменения пользователя"""
    data = load_data()
    uid = str(user_id)
    
    if uid not in data:
        data[uid] = {}
    
    if updates:
        data[uid].update(updates)
    
    _user_data_cache.update(data)
    await save_data()

def get_active_users() -> list:
    """Получить список активных пользователей"""
    data = load_data()
    return [int(uid) for uid, user in data.items() if user.get("active", False)]

def get_all_active_users():
    """Получить список всех активных пользователей (алиас для get_active_users)"""
    return get_active_users()

def schedule_jobs(chat_id, job_queue):
    """Запланировать ежедневные задания (заглушка)"""
    # Пока просто заглушка, позже реализуем
    print(f"DEBUG: schedule_jobs called for {chat_id}")
    return

def remove_user_jobs(chat_id, job_queue):
    """Удалить все задания пользователя (заглушка)"""
    print(f"DEBUG: remove_user_jobs called for {chat_id}")
    return

def calculate_streak(user_data: dict) -> int:
    """Рассчитать текущую серию (заглушка)"""
    # Пока просто возвращаем лучшую серию
    return user_data.get("best_streak", 0)

# ========== НОВЫЕ ФУНКЦИИ ==========

def get_user_days(user_id: int) -> int:
    """Получить количество дней трезвости пользователя"""
    user = get_user(user_id)
    start_date = user.get("start_date")
    
    if not start_date:
        return 0
    
    from datetime import date
    try:
        start = date.fromisoformat(start_date)
        today = date.today()
        return max((today - start).days, 0)
    except Exception:
        return 0

async def reset_user_progress(user_id: int):
    """Сбросить прогресс пользователя (при срыве)"""
    user = get_user(user_id)
    
    # Сохраняем лучший результат
    current_days = get_user_days(user_id)
    best_streak = user.get("best_streak", 0)
    
    if current_days > best_streak:
        await save_user(user_id, {"best_streak": current_days})
    
    # Сбрасываем всё
    from bot.utils.time import get_current_date
    new_start_date = get_current_date().isoformat()
    
    await save_user(user_id, {
        "start_date": new_start_date,
        "hold_count_today": 0,
        "last_hold_date": None,
        "last_hold_time": None,
        "used_tips": [],
        "used_triggers": [],
        "used_distortions": [],
        "used_facts": [],
        "used_rage": [],
        "used_anhedonia": [],
        "achievements_received": []
    })
    
    return current_days  # Возвращаем сколько дней было до сброса
