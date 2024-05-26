from ...database.mongodb import *


def create_user(
    name,
    phone: int,
    address,
    # home,
    # work,
    # college,
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
        None
    """

    user = {
        "name": name,
        "phone": phone,
        "address": address,
        # "home": home,
        # "work": work,
        # "college": college,
        "dob": dob,
        "occupation": occupation,
        "health_condition": health_condition,
        "dislikings": dislikings,
        "restriction": restriction,
    }

    user_collection.insert_one(user)


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
    user = user_collection.find_one({"wa_id": wa_id})
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
    user_collection.delete_one({"wa_id": wa_id})
    return "Your account data has been deleted"
