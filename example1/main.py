# создание документа в новой БД и коллекции

from pymongo import MongoClient

uri = "mongodb+srv://sfedorovmhi:BRL7gP4Dodz4qc3l@testcluster.ykbmvay.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Если осуществить вставку документа в несуществующую БД и/или коллекцию,
# то они будут созданы
db = client.new_db
new_collection = db.users

# если повторно вставить документ с тем же id, то выпадет ошибка
# pymongo.errors.DuplicateKeyError: E11000 duplicate key error collection
new_collection.insert_one({"_id": 2, "username": "Kate"})
