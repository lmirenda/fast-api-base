from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("/")
async def main_route():
    return {"message": "Hey, It is me Goku"}


@router.get("/{item_id}")
async def read_item(item_id: str):
    return {"message": f"Hey, the item_id was {item_id}"}
