import pymongo
from pymongo import MongoClient
import modules.utils

try:
    cluster = MongoClient(modules.utils.get_uri())
    db = cluster["LeilaBot"]
    collection = db["UserData"]
except:
    print("sexo")


