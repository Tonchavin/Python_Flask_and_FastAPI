import uvicorn
from fastapi import FastAPI, APIRouter

from Lesson6.Homework6.app.routers.router_users import router as router_users
from Lesson6.Homework6.app.routers.router_items import router as router_items
from Lesson6.Homework6.app.routers.router_orders import router as router_orders

app = FastAPI()

app.include_router(router_users, prefix="/users", tags=['users'])
app.include_router(router_items, prefix="/items", tags=['items'])
app.include_router(router_orders, prefix="/orders", tags=['orders'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='info', reload=True)
