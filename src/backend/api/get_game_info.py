from fastapi import APIRouter
from backend.models.game import Game
from backend.services.hltb_service import get_info_from_hltb
from backend.services.rawg_service import get_info_from_rawg

router = APIRouter()

@router.post("/get-game-info")
async def get_game_info(game: Game):
    # First, we fetch information from a reliable platform
    rawg_game_info = await get_info_from_rawg(game.title)

    # After retrieving the game info from RAWG, we use its slug to fetch additional details without errors
    hltb_game_info = await get_info_from_hltb(rawg_game_info['name'])


    # ign_game_info = await get_info_from_ign(game.title)
    # scoring = calculate_final_game_scoring()

    return {
        "hltb": hltb_game_info,
        "rawg": rawg_game_info,
        # "ign": ign_game_info,
        # "score": scoring
    }