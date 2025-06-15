from howlongtobeatpy import HowLongToBeat

async def get_info_from_hltb(title: str):
    results_list = await HowLongToBeat().async_search(title)

    if not results_list:
        return None

    best_element = max(results_list, key=lambda element: element.similarity)

    return {
        "game_name": best_element.game_name,
        "main_story": best_element.main_story,
        "main_extra": best_element.main_extra,
        "completionist": best_element.completionist,
    }