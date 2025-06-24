import os
import httpx
from dotenv import load_dotenv
from backend.db.sqlite import Database
from backend.models.steam import SteamData

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db", "hwitg.db"))

load_dotenv()

STEAM_API_GET_ALL_GAMES_URL = os.getenv('STEAM_API_GET_ALL_GAMES_URL')
STEAM_API_APP_REVIEW_URL = os.getenv('STEAM_API_APP_REVIEW_URL')


async def get_all_steam_games():
    async with httpx.AsyncClient() as client:
        response = await client.get(STEAM_API_GET_ALL_GAMES_URL)
        data = response.json()
        games = data['applist']['apps']

        db = Database(DB_PATH)
        db.insert_many("steam_games", ["appid", "name"], [(g['appid'], g['name']) for g in games])
        db.close()


async def get_info_from_steam(title: str):
    steam_game_id = get_game_id_from_steam(title)
    if steam_game_id is None:
        return None

    url = f"{STEAM_API_APP_REVIEW_URL}/{steam_game_id}"
    params = {"json": 1}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()
        return map_steam_info(data, title)


def get_game_id_from_steam(title: str):
    db = Database(DB_PATH)
    steam_game_id = db.select("steam_games", params=[{"cond": "name", "value": title}])
    db.close()

    if not steam_game_id:
        return None
    return steam_game_id[0][0]


def map_steam_info(steam_info, title=None):
    if not steam_info:
        return None

    if not steam_info.get("success"):
        return None

    query_summary = steam_info.get("query_summary", {})
    review_score = query_summary.get("review_score")
    review_score_desc = query_summary.get("review_score_desc")

    reviews = steam_info.get("reviews", [])

    return SteamData(
        name=title,
        score=review_score,
        top_media_scores=[
            {
                "source": "Steam",
                "score": review_score,
                "label": review_score_desc
            }
        ] if review_score is not None else [],
        top_reviews=reviews[:10] if reviews else []
    )


