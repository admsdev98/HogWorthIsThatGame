from fastapi import APIRouter
from backend.models.game import Game
from backend.scoring import calculate_final_game_scoring
from backend.services.rawg_service import get_info_from_rawg
from backend.services.hltb_service import get_info_from_hltb
from backend.services.steam_service import get_all_steam_games, get_info_from_steam

router = APIRouter()

@router.post("/get-game-info")
async def get_game_info(game: Game):
    # First, we fetch information from a reliable platform
    rawg_game_info = await get_info_from_rawg(game.title)

    # After retrieving the game info from RAWG, we use its slug to fetch additional details without errors
    hltb_game_info = await get_info_from_hltb(rawg_game_info['name'])
    steam_game_info = await get_info_from_steam(rawg_game_info['name'])

    scoring = calculate_final_game_scoring(rawg_game_info, hltb_game_info, steam_game_info)

    return {
        "hltb": hltb_game_info,
        "rawg": rawg_game_info,
        "score": scoring
    }

@router.post("/get-all-steam-games")
async def get_game_info():
    await get_all_steam_games()