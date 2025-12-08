from aiogram import Router
from .start import router as start_router
from .hold import router as hold_router
from .progress import router as progress_router
# сюда потом добавим остальные

router = Router()
router.include_router(start_router)
router.include_router(hold_router)
router.include_router(progress_router)
