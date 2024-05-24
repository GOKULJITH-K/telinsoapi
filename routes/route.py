from fastapi import APIRouter
from models.todos import Todo
from models.todos import CropData
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

@router.post("/predictCrop")
def predict_crop(data: CropData):
    crop_prediction, success_percentage, suggested_crop = predict_crop_success(
        data.N, data.P, data.K, data.ph, data.humidity, data.ec, data.temperature
    )
    return {
        'crop_prediction': crop_prediction,
        'success_percentage': success_percentage,
        'suggested_crop': suggested_crop
    }
    @app.get("/predictCrop")
def predict_crop_get(N: float, P: float, K: float, ph: float, humidity: float, ec: float, temperature: float):
    crop_prediction, success_percentage, suggested_crop = predict_crop_success(
        N, P, K, ph, humidity, ec, temperature
    )
    return {
        'crop_prediction': crop_prediction,
        'success_percentage': success_percentage,
        'suggested_crop': suggested_crop
    }
