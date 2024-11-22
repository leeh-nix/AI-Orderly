import dotenv
import os
import json
import google.generativeai as genai

from logger import logger


dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

system_instruction = """
You are a friendly and knowledgeable restaurant bot that interacts using whatsapp as interface, designed to help users explore the menu, answer questions, and make suggestions.

You are given a menu with various categories such as starters, mains, and desserts. When a user asks about the menu, respond with a list of items from the relevant category along with descriptions and prices.

Do not memorize the menu directly in your instructions. Instead, use the dynamic menu data provided to generate your responses. You are responsible for:

- Providing details of menu items when users ask (name, description, price) in bulleted points using whatsapp formatting.
- Offering suggestions based on user preferences (e.g., if they want something vegetarian, spicy, etc.).
- Encouraging the user to explore the menu further (e.g., asking, "Would you like to know more about our desserts?").

Always maintain a friendly, welcoming tone and provide helpful responses.
"""

model_pro = genai.GenerativeModel(
    # model_name="gemini-pro",
    model_name="gemini-1.5-flash-latest",
    system_instruction=system_instruction,
    safety_settings=None,
)


query_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    system_instruction="""
You are a query generator for a menu.json file stored on backend for a restaurant, your task is to find the intent of user in the given user message and generate a query that will be used by our backend program to select the correct parts of our menu

Do not conatain any header or footer text, only the query should be there without the delimitor backticks

Use the following structure of menu.json (python dictionary) for queries:
menu = {
    "starters": [...],
    "mains": [...],
    "desserts": [...]
}

Examples: 
user: `What do you guys server in the beginning?`
you: `menu["starters"]`

user: `What about main course and sweets?`
you: `menu["starters"] + menu["desserts"]`
""",
    safety_settings=None,
)


def generate_query(text):
    response = query_model.generate_content(contents=text)
    result = response.text
    print(f"Gemini Query: \n{result}")
    return result



def generate_response(text) -> str:
    """
    Generates a response based on the given text.

    Args:
        text (str): The input text to generate a response from.

    Returns:
        str: The generated response.

    """

    # menu_data = ""

    # if "starter" in text.lower():
    #     menu_data = "Here are some of our starters:\n"
    #     for item in menu["starters"]:
    #         menu_data += f"{item['name']}: {item['description']} - {item['price']}\n"
    # elif "main" in text.lower():
    #     menu_data = "Here are some of our mains:\n"
    #     for item in menu["mains"]:
    #         menu_data += f"{item['name']}: {item['description']} - {item['price']}\n"
    # elif "dessert" in text.lower():
    #     menu_data = "Here are some of our desserts:\n"
    #     for item in menu["desserts"]:
    #         menu_data += f"{item['name']}: {item['description']} - {item['price']}\n"
    # else:
    #     menu_data = "I'm sorry, I didn't understand your request. Could you please rephrase or ask something else?"
    # # Add menu details to the user query
    # response_text = f"User asked: {text}\n\n{menu_data}"

    response = model_pro.generate_content(contents=text)
    result = response.text
    logger(f"Gemini: \n{result}")
    return result
