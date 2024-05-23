import random
import dotenv
import os

import google.generativeai as genai


# dotenv.load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# curl -H 'Content-Type: application/json' -d '{ "prompt": { "text": "Write a story about a magic backpack"} }' \
# "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=YOUR_API_KEY"


genai.configure(api_key=GEMINI_API_KEY)

# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)


model_pro = genai.GenerativeModel(
    # model_name="gemini-pro",
    model_name="gemini-1.5-flash-latest",
    # safety_settings=None,
)


def sendResponse(text):
    print(text)
    response = model_pro.generate_content(
        contents=text,
    )
    result = response.text
    return result


# print(sendResponse("Write a story about a magic backpack"))

# import pprint

# for model in genai.list_models():
# pprint.pprint(model)
