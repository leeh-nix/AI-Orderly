import dotenv
import os
import google.generativeai as genai


dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# curl -H 'Content-Type: application/json' -d '{ "prompt": { "text": "Write a story about a magic backpack"} }' \
# "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=YOUR_API_KEY"


genai.configure(api_key=GEMINI_API_KEY)

# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    system_instruction="You are a bot for a food delivery organization. Your task is to take food items as input and serve the user with the items and at last give the total amount to be paid",
    # generation_config=generation_config,
)

chat = model.start_chat(history=[])


def send_message_to_chatbot(message):
    response = chat.send_message(message)
    return response.text


response = send_message_to_chatbot("Hello, I'd like to order a pizza")
print(response)


# # model_pro = genai.GenerativeModel(
# #     # model_name="gemini-pro",
# #     model_name="gemini-1.5-flash-latest",
# #     # safety_settings=None,
# # )
# # def generate_response(text) -> str:
# #     """
# #     Generates a response based on the given text.

# #     Args:
# #         text (str): The input text to generate a response from.

# #     Returns:
# #         str: The generated response.

# #     """
# #     print(text)
# #     response = model_pro.generate_content(
# #         contents=text,
# #     )
# #     result = response.text
# #     return result
