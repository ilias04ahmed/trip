from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register():
    return {"msg": "register"}

@router.post("/login")
async def login():
    return {"msg": "login"}
