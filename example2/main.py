# создание документа в существующей БД и коллекции
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
user = os.getenv("MONGO_USER")
pwd = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")

uri = f"mongodb+srv://{user}:{pwd}@{cluster}?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.testdata
coll = db.users
coll.insert_one({"_id": 3, "username": "Nightmare"})

for doc in coll.find():
    print(doc)
