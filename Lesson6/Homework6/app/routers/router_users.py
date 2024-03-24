from fastapi import APIRouter
from passlib.hash import pbkdf2_sha256
from Lesson6.Homework6.models import User, UserIn
from Lesson6.Homework6.database import db, users


router = APIRouter()


@router.post("/user", response_model=User)
async def create_user(user_in: UserIn):
    user_to_db = user_in.dict().copy()
    user_to_db.setdefault('password_hash', pbkdf2_sha256.hash(user_to_db.pop('password')))
    query = users.insert().values(**user_to_db)
    last_record_id = await db.execute(query)
    return {**user_to_db, "id": last_record_id}


@router.get("/users", response_model=list[User])
async def read_users():
    query = users.select()
    return await db.fetch_all(query)


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_in: UserIn):
    user_to_db = user_in.dict().copy()
    user_to_db.setdefault('password_hash', pbkdf2_sha256.hash(user_to_db.pop('password')))
    query = users.update().where(users.c.id == user_id).values(**user_to_db)
    await db.execute(query)
    return {**user_to_db, "id": user_id}


@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {"message": "User successfully deleted"}
