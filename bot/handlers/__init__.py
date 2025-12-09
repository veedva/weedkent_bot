from aiogram import Router

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# ВСЕ ХЕНДЛЕРЫ — ВСЁ РАБОТАЕТ
from .start import router as start_router
from .hold import router as hold_router
from .progress import router as progress_router
from .heavy import router as heavy_router   # ← ЭТОТ ТЫ ЗАБЫЛ ДОБАВИТЬ!!!
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

router = Router()
router.include_router(start_router)
router.include_router(hold_router)
router.include_router(progress_router)
router.include_router(heavy_router)   # ← ЭТА СТРОКА ВКЛЮЧАЕТ 😔 Тяжело и всё остальное
