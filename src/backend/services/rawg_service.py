import os
import httpx
from dotenv import load_dotenv
from backend.models.rawg import RawgData

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

def map_rawg_info(rawg_info):
    if not rawg_info:
        return None

    name = rawg_info.get("name")
    score = rawg_info.get("rating")  # RAWG: puntuación media

    top_media_scores = [
        {"source": rating.get("title"), "score": rating.get("percent")}
        for rating in rawg_info.get("ratings", [])[:3]
    ]

    return RawgData(
        name=name,
        score=score,
        top_media_scores=top_media_scores
    )
