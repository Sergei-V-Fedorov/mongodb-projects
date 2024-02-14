import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

uri = f"mongodb://{HOST}:{PORT}/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.4"
client = MongoClient(uri)

db = client.testdb
collection = db.users

# запись в БД
# collection.insert_one({"_id": 2, "username": "sf"})
# print("Данные записаны!")

# Чтение из БД
res = collection.find_one()
print(f"Прочитан документ: {res}")

res = collection.find()
print("\nСодержимое коллекции:")
for item in res:
    print(item)
