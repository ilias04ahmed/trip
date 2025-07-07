from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_destinations():
    return {"destinations": []}

@router.get("/{dest_id}/activities")
async def get_activities(dest_id: int):
    return {"destination_id": dest_id, "activities": []}
