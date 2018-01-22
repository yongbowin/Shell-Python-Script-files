from pymongo import MongoClient

client = MongoClient("mongodb://192.168.100.237:27017/")
database = client["ReplaceKS"]
collection = database["Test"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}

cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc["score"])
finally:
    cursor.close()
