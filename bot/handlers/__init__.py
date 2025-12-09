from aiogram import Router

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# ВСЁ, ЧТО У ТЕБЯ ЕСТЬ — ВКЛЮЧЕНО
from .start import router as start_router
from .hold import router as hold_router
from .progress import router as progress_router
from .heavy import router as heavy_router          # ← 😔 Тяжело
from .rage import router as rage_router            # ← 🤬 ЗЛЮСЬ (если есть)
from .info import router as info_router            # ← 🧠 Информация (если есть)
from .practice import router as practice_router    # ← 💪 Практика (если есть)
from .days import router as days_router            # ← 📅 Дни (если есть)
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

router = Router()
router.include_router(start_router)
router.include_router(hold_router)
router.include_router(progress_router)
router.include_router(heavy_router)
router.include_router(rage_router)        # ← если файла нет — просто закомментируй эту строку
router.include_router(info_router)        # ← если файла нет — закомментируй
router.include_router(practice_router)    # ← если файла нет — закомментируй
router.include_router(days_router)        # ← если файла нет — закомментируй
