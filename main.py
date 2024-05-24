from fastapi import FastAPI
from routes.route import router
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# v8RcNc2VQL1D5p4m
app = FastAPI()


app.include_router(router)


 

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




# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://admin:v8RcNc2VQL1D5p4m@cluster0.0bx7pop.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
