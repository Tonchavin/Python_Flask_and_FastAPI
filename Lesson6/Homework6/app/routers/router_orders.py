from fastapi import APIRouter

from Lesson6.Homework6.models import Order, OrderIn
from Lesson6.Homework6.database import db, orders

router = APIRouter()


@router.post("/order", response_model=Order)
async def create_order(order_in: OrderIn):
    query = orders.insert().values(**order_in.dict())
    last_record_id = await db.execute(query)
    return {**order_in.dict(), "id": last_record_id}


@router.get("/orders", response_model=list[Order])
async def read_orders():
    query = orders.select()
    return await db.fetch_all(query)


@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await db.fetch_one(query)


@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, order_in: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**order_in.dict())
    await db.execute(query)
    return {**order_in.dict(), "id": order_id}


@router.delete("/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {"message": "Order successfully deleted"}
