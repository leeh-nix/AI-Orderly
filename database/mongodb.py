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
user_collection = db.wa_user  # collection: whatsapp
restaurant_collection = db.resto  # collection: restaurant

# ● Name
# ● Phone
# ● Address + G Loc
# -home(Tags): Work - Hostel - College
# ● DOB
# ● Occupation
# ● Health Condition
# ● Dislikings
# ● any days with restriction (eg-tuesdays and no non veg) or no veg


def create_user(
    name,
    phone,
    address,
    home,
    work,
    college,
    dob,
    occupation,
    health_condition,
    dislikings,
    restriction,
):
    user = {
        "name": name,
        "phone": phone,
        "address": address,
        "home": home,
        "work": work,
        "college": college,
        "dob": dob,
        "occupation": occupation,
        "health_condition": health_condition,
        "dislikings": dislikings,
        "restriction": restriction,
    }

    user_collection.insert_one(user)


# {
#   Name
# ● Branches
# ● GLoc+
# Address(es)
# ● Menu
# -Dish Name
# - Dish Pic
# Portion Sizing
# -Price / Portion
# -Rating (Dish)
# ● Contact person
# name
# ● Contact Person
# cell
# ● Resto Rating
# }


def create_restaurant(
    resto_name,
    branches,
    gloc,
    address,
    menu,
    dish_name,
    dish_pic,
    portion_sizing,
    price_portion,
    rating,
    contact_person_name,
    contact_person_cell,
    resto_rating,
):
    restaurant = {
        "resto_name": resto_name,
        "branches": branches,
        "gloc": gloc,
        "address": address,
        "menu": menu,
        "dish_name": dish_name,
        "dish_pic": dish_pic,
        "portion_sizing": portion_sizing,
        "price_portion": price_portion,
        "rating": rating,
        "contact_person_name": contact_person_name,
        "contact_person_cell": contact_person_cell,
        "resto_rating": resto_rating,
    }

    restaurant_collection.insert_one(restaurant)
