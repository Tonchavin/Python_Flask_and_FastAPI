from fastapi import APIRouter

from Lesson6.Homework6.models import Item, ItemIn
from Lesson6.Homework6.database import db, items

router = APIRouter()


@router.post("/item", response_model=Item)
async def create_item(item_in: ItemIn):
    query = items.insert().values(**item_in.dict())
    last_record_id = await db.execute(query)
    return {**item_in.dict(), "id": last_record_id}


@router.get("/items", response_model=list[Item])
async def read_items():
    query = items.select()
    return await db.fetch_all(query)


@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await db.fetch_one(query)


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item_in: ItemIn):
    query = items.update().where(items.c.id == item_id).values(**item_in.dict())
    await db.execute(query)
    return {**item_in.dict(), "id": item_id}


@router.delete("/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await db.execute(query)
    return {"message": "Item successfully deleted"}
