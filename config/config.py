
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://provat1716:2URrDZOdFdyTNjso@provat.dudow6n.mongodb.net/?retryWrites=true&w=majority&appName=provat"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.blogging
blogging_collection=db["blogs"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)