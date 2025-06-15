import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RAWG_API_KEY')
BASE_URL = 'https://api.rawg.io/api'

async def get_info_from_rawg(title: str):
    search_url = f"{BASE_URL}/games"
    search_params = {
        "key": API_KEY,
        "search": title,
        "page_size": 1
    }

    response = requests.get(search_url, params=search_params)
    data = response.json()
    return data['results'][0]