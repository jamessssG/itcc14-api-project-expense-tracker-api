from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)

# our DB
db = client["expense_tracker"]

# our collection
transactions_collection = db["transactions"]
