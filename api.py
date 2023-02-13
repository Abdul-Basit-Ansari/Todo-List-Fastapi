from fastapi import APIRouter
from apis import todos


api_router = APIRouter()
api_router.include_router(todos.router, prefix="/todos", tags=["todos"])