from fastapi import APIRouter
from models.todos import Todo
from models.todos import CropData
from config.database import collection_name
from scheme.schemas import list_serial
from config.database import collection_name2
from scheme.schemas import list_serial2
from bson import ObjectId
from sklearn.ensemble import RandomForestClassifier
import pandas as pd




dataset = pd.read_csv('crop_data.csv')


X = dataset[['N', 'P', 'K', 'ph', 'humidity', 'ec', 'temperature']]
y = dataset['Crop'] 
print(dataset.columns) 

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
 

rf_classifier.fit(X, y)


def predict_crop_success(N, P, K, ph, humidity, ec, temperature):
    input_data = [[N, P, K, ph, humidity, ec, temperature]]
    crop_prediction = rf_classifier.predict(input_data)[0]
    crop_probabilities = rf_classifier.predict_proba(input_data)[0]
    max_probability_index = crop_probabilities.argmax()
    max_probability = crop_probabilities[max_probability_index]
    suggested_crop = rf_classifier.classes_[max_probability_index]
    return crop_prediction, max_probability * 100, suggested_crop

router = APIRouter()

@router.get("/telinso")
async def get_todo():
    todo = list_serial(collection_name.find())
    return todo


@router.post("/telinso")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))


@router.get("/predictCrop")
async def get_predict():
    predict = list_serial2(collection_name2.find())
    return predict
@router.post("/predictCrop")
async def predict_crop(data: CropData):
    crop_prediction, success_percentage, suggested_crop = predict_crop_success(
        data.N, data.P, data.K, data.ph, data.humidity, data.ec, data.temperature
    )
    
    existing_crop_data = collection_name2.find_one({"username": data.username})
    cropdata = {
        "crop_prediction": crop_prediction,
        "success_percentage": success_percentage,
        "suggested_crop": suggested_crop,
        "username":data.username,
        "__v": 0,
    } 
    if existing_crop_data:
        id_db = {"_id": existing_crop_data["_id"]}
        collection_name2.update_one(id_db, {"$set": cropdata})
    else:
        collection_name2.insert_one(cropdata)
    
