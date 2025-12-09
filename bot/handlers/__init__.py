# bot/handlers/__init__.py
"""
Подключение всех обработчиков
"""

from aiogram import Router

router = Router()

# Все рабочие handlers
from .start import router as start_router
from .hold import router as hold_router
from .progress import router as progress_router
from .heavy import router as heavy_router
from .practice import router as practice_router
from .info import router as info_router
from .rage import router as rage_router
from .stop import router as stop_router
from .thanks import router as thanks_router
from .tu_tut import router as tu_tut_router

# Подключаем все роутеры
router.include_router(start_router)
router.include_router(hold_router)
router.include_router(progress_router)
router.include_router(heavy_router)
router.include_router(practice_router)
router.include_router(info_router)
router.include_router(rage_router)
router.include_router(stop_router)
router.include_router(thanks_router)
router.include_router(tu_tut_router)
