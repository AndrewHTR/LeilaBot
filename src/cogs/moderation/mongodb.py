import pymongo
from pymongo import MongoClient
import modules.utils

try:
    cluster = MongoClient(modules.utils.get_uri())
    db = cluster["LeilaBot"]
    collection = db["UserData"]
    post = {"_id": 2, "score": 1}
    collection.insert_one(post)
except:
    print("sexo")


