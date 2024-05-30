import math
from database.mongodb import users_collection, restaurant_collection


def create_users(
    name,
    phone: int,
    address,
    dob,
    occupation,
    health_condition,
    dislikings,
    restriction,
):
    """
    Creates a new user in the database with the given information.

    Args:
        name (str): The name of the user.
        phone (str): The phone number of the user.
        address (str): The address of the user (home, work, college).
        dob (str): The date of birth of the user.
        occupation (str): The occupation of the user.
        health_condition (str): The health condition of the user.
        dislikings (str): The things the user dislikes.
        restriction (str): The restrictions the user has.

    Returns:
        String
    """

    if existing_user(phone):
        return "User already exists"
    user = {
        "name": name,
        "phone": phone,
        "address": address,
        "dob": dob,
        "occupation": occupation,
        "health_condition": health_condition,
        "dislikings": dislikings,
        "restriction": restriction,
    }

    users_collection.insert_one(user)
    return "User created"


def create_restaurant(
    resto_name,
    branches: list,
    gloc,
    address,
    menu: list,
    dish_name: list,
    dish_pic: list,
    portion_sizing: list,
    price_portion: list,
    rating,
    contact_person_name,
    contact_person_cell,
    resto_rating: float,
):
    """
    Creates a new restaurant in the database with the given information.

    Args:
        resto_name (str): The name of the restaurant.
        branches (list): A list of branches of the restaurant.
        gloc (str): The geolocation of the restaurant.
        address (str): The address of the restaurant.
        menu (list): A list of menu items available at the restaurant.
        dish_name (list): A list of names of dishes available at the restaurant.
        dish_pic (list): A list of URLs of pictures of dishes available at the restaurant.
        portion_sizing (list): A list of portion sizes available for each dish.
        price_portion (list): A list of prices for each portion size of each dish.
        rating (float): The rating of the restaurant.
        contact_person_name (str): The name of the contact person at the restaurant.
        contact_person_cell (str): The cell number of the contact person at the restaurant.
        resto_rating (float): The rating of the restaurant by users.

    Returns:
        None
    """

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


def existing_user(wa_id):
    """
    Check if a user with the given WhatsApp ID exists in the database.

    Parameters:
        wa_id (int): The WhatsApp ID of the user.

    Returns:
        bool: True if a user with the given WhatsApp ID exists, False otherwise.
    """
    user = users_collection.find_one({"wa_id": wa_id})
    if user:
        return True
    else:
        return False


def delete_user(wa_id):
    """
    Deletes a user from the user_collection in the database based on the provided WhatsApp ID.

    Parameters:
        wa_id (int): The WhatsApp ID of the user to be deleted.

    Returns:
        None
    """
    users_collection.delete_one({"wa_id": wa_id})
    return "Your account data has been deleted"


def fetch_restaurants_details():
    """
    Fetches the details of all restaurants from the restaurant_collection in the database.

    Returns:
        List of dictionaries containing the details of each restaurant.
    """
    restaurants = []
    for restaurant in restaurant_collection.find():
        restaurants.append(restaurant)
    return restaurants


def calculate_nearest_restaurant(user_latitude, user_longitude):
    """
    Calculates the nearest restaurant from the given latitude and longitude of the user.

    Parameters:
        user_latitude (float): The latitude of the user.
        user_longitude (float): The longitude of the user.

    Returns:
        Dictionary containing the details of the nearest restaurant.
    """
    restaurants = fetch_restaurants_details()
    nearest_restaurant = None
    minimum_distance = float("inf")
    for restaurant in restaurants:
        restaurant_gloc = restaurant["gloc"]
        restaurant_latitude = float(restaurant_gloc[0])
        restaurant_longitude = float(restaurant_gloc[1])
        distance = calculate_distance(
            user_latitude, user_longitude, restaurant_latitude, restaurant_longitude
        )
        if distance < minimum_distance:
            minimum_distance = distance
            nearest_restaurant = restaurant
    return nearest_restaurant


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two points on the Earth's surface using the Haversine formula.

    Parameters:
        lat1 (float): The latitude of the first point.
        lon1 (float): The longitude of the first point.
        lat2 (float): The latitude of the second point.
        lon2 (float): The longitude of the second point.

    Returns:
        The distance between the two points in kilometers.
    """
    earth_radius = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
        math.radians(lat1)
    ) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = earth_radius * c

    return distance


x = {
    "resto_name": "Taco Time",
    "branches": ["Southside", "Northside"],
    "gloc": "37.7749295,-122.4194155",
    "address": "123 Southside St, Bay City, CA 98765",
    "menu": ["Mexican"],
    "dish_name": ["Beef Tacos", "Chicken Quesadilla"],
    "dish_pic": ["url_to_beef_tacos_pic", "url_to_chicken_quesadilla_pic"],
    "portion_sizing": ["Single", "Double"],
    "price_portion": [[5, 9], [7, 13]],
    "rating": 4.2,
    "contact_person_name": "Michael Brown",
    "contact_person_cell": "456-789-0123",
    "resto_rating": 4.3,
}


def serve_pics(nearest_restaurant):
    dish_name = nearest_restaurant["dish_name"]
    dish_pic = nearest_restaurant["dish_pic"]
    
    return dish_name, dish_pic

