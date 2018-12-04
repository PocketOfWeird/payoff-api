import os
from pymongo import MongoClient


def load_db():
    mongo_client = MongoClient(os.getenv("MONGO_URI"))
    db = mongo_client[os.getenv("MONGO_DB")]
