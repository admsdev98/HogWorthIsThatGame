import os
import httpx
from dotenv import load_dotenv

load_dotenv()

RAWG_API_KEY = os.getenv('RAWG_API_KEY')
RAWG_API_URL = os.getenv('RAWG_API_URL')


async def get_info_from_rawg(title: str):
    search_url = f"{RAWG_API_URL}/games"
    search_params = {
        "key": RAWG_API_KEY,
        "search": title,
        "page_size": 1
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(search_url, params=search_params)
        data = response.json()

    return data['results'][0] if data['results'] else None
