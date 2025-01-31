import openai
from backend.config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_ai_opinion(asset_name, price):
    prompt = f"Is {asset_name} at ${price} overvalued or undervalued? Explain."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
