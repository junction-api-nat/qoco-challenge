import pymongo
from pymongo import MongoClient
import os

DB_NAME = "junction-challenge"
DB_HOST = os.environ.get("SECRET")
DB_PORT = 15434
DB_USER = "tommi"
DB_PASS = os.environ.get("PASSWD")

print(DB_NAME)
print(DB_HOST)
print(DB_PORT)
print(DB_USER)
print(DB_PASS)

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

testcollection = db.collection
print(testcollection.find_one())