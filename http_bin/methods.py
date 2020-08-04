from fastapi import APIRouter

router = APIRouter()


@router.get("/get/")
async def read_root():
    return {"msg": "This is HTTP GET"}
