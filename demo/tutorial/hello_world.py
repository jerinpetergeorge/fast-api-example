import logging
from fastapi import APIRouter

router = APIRouter()

empty_logger = logging.getLogger("myapp")


@router.get("/")
async def read_root():
    empty_logger.info("This is `read_root()` function")
    return {"msg": "Hello World"}
