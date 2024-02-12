# создание документа в существующей БД и коллекции

from pymongo import MongoClient

uri = "mongodb+srv://sfedorovmhi:BRL7gP4Dodz4qc3l@testcluster.ykbmvay.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client.testdata
new_collection = db.users
new_collection.insert_one({"_id": 2, "username": "Kate"})
