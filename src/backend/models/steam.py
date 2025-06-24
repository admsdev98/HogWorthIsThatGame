from pydantic import BaseModel
from typing import List, Optional

class MediaScore(BaseModel):
    source: str
    score: int
    label: str

class SteamData(BaseModel):
    name: str
    score: int
    top_media_scores: List[MediaScore]
    top_reviews: Optional[List[dict]] = None 


    
