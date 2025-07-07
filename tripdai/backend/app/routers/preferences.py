from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def set_preferences():
    return {"msg": "preferences set"}

@router.get("/{user_id}")
async def get_preferences(user_id: int):
    return {"user_id": user_id}
