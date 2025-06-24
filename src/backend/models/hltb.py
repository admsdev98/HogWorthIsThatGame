from pydantic import BaseModel
from typing import List, Optional

class HltbData(BaseModel):
    game_name: str
    main_story: str
    main_extra: str
    completionist: str


    
