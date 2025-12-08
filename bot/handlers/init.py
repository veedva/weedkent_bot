from aiogram import Router

# Импортируем все роутеры
from .start import router as start_router
from .hold import router as hold_router
from .progress import router as progress_router
# сюда потом добавим rage, achievements и т.д.

# Главный роутер — он и есть "router" в main.py
router = Router()
router.include_router(start_router)
router.include_router(hold_router)
router.include_router(progress_router)

# Эта строка — ключ к жизни
__all__ = ["router"]
