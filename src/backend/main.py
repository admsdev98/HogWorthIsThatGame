from fastapi import FastAPI
from howlongtobeatpy import HowLongToBeat

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Proyecto base funcionando"}

@app.get("/get-game")
async def get_hltb_game_info(title: str):
    results_list = await HowLongToBeat().async_search(title)
    if results_list is not None and len(results_list) > 0:
        best_element = max(results_list, key=lambda element: element.similarity)
        
        return {
            "game_name": best_element.game_name,
            "main_story": best_element.main_story,
            "main_extra": best_element.main_extra,
            "completionist": best_element.completionist,
        }

