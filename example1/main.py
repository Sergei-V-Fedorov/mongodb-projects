# создание документа в новой БД и коллекции
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
user = os.getenv("MONGO_USER")
pwd = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")

uri = f"mongodb+srv://{user}:{pwd}@{cluster}?retryWrites=true&w=majority"
client = MongoClient(uri)

# Если осуществить вставку документа в несуществующую БД и/или коллекцию,
# то они будут созданы
db = client.new_db
coll = db.users

# если повторно вставить документ с тем же id, то выпадет ошибка
# pymongo.errors.DuplicateKeyError: E11000 duplicate key error collection
# coll.insert_one({"_id": 3, "username": "Morgan"})

# Вывод всего содержимого коллекции
for doc in coll.find():
    print(doc)
