from aiogram import Router

router = Router()

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# ТОЛЬКО ТО, ЧТО У ТЕБЯ ЕСТЬ НА САМОМ ДЕЛЕ
from .start import router as start_router      # ▶ Начать, /start
from .hold import router as hold_router        # ✊ Держусь
from .progress import router as progress_router # 📊 Прогресс
from .heavy import router as heavy_router       # 😔 Тяжело
from .tu_tut import router as tu_tut_router     # 👋 Ты тут?
from .thanks import router as thanks_router     # ❤️ Спасибо
from .stop import router as stop_router         # ⏸ Помолчи
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

router.include_router(start_router)
router.include_router(hold_router)
router.include_router(progress_router)
router.include_router(heavy_router)
router.include_router(tu_tut_router)
router.include_router(thanks_router)
router.include_router(stop_router)
