from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import dotenv
import os

dotenv.load_dotenv()
URI = os.getenv("URI")
# Create a new client and connect to the server
client = MongoClient(URI, server_api=ServerApi("1"))
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.get_database("food_nests")
users_collection = db.wa_users  # collection: whatsapp users
restaurant_collection = db.resto  # collection: restaurants

# add a fn to calculate the number of entries so that whenever
# someone adds to this it returns a number of how many got added or in negative if deleted
