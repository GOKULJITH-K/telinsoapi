from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from scheme.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/telinso")
async def get_todo():
    todo = list_serial(collection_name.find())
    return todo


@router.post("/telinso")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))