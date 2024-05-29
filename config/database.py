from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongo:UNE8bmYvV38FARx5@cluster0.l2ubs1d.mongodb.net")

db = client["login-tut"]

collection_name = db["tests"]
collection_name2 = db["prediction"]
