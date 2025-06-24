from howlongtobeatpy import HowLongToBeat
from backend.models.hltb import HltbData

async def get_info_from_hltb(title: str):
    results_list = await HowLongToBeat().async_search(title)

    if not results_list:
        return None

    hltb_filtered_result = max(results_list, key=lambda element: element.similarity)

    return map_hltb_info(hltb_filtered_result)

def map_hltb_info(hltb_info):
    return HltbData(
        game_name=hltb_info.game_name,
        main_story=hltb_info.main_story,
        main_extra=hltb_info.main_extra,
        completionist=hltb_info.completionist,
    )