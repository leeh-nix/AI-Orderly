import dotenv
import os
import google.generativeai as genai


dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model_pro = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=None,
)


def generate_response(text) -> str:
    """
    Generates a response based on the given text.

    Args:
        text (str): The input text to generate a response from.

    Returns:
        str: The generated response.

    """
    print(text)
    response = model_pro.generate_content(
        contents=text,
    )
    result = response.text
    return result
