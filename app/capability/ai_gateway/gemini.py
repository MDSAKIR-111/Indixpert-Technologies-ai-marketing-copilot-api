from google import genai

from app.core.config.settings import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


async def generate_content(prompt: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text