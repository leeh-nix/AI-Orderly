import os
import dotenv
import google.generativeai as genai


dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model_pro = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
)


def generate_response(text: str) -> str:
    """
    Generates a response based on the given text.

    Args:
        text (str): The input text to generate a response from.

    Returns:
        str: The generated response.

    """
    response = model_pro.generate_content(
        contents=text,
    )
    return response.text
