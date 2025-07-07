from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
async def generate_itinerary():
    return {"msg": "itinerary generated"}

@router.get("/{itinerary_id}")
async def get_itinerary(itinerary_id: int):
    return {"itinerary_id": itinerary_id}
