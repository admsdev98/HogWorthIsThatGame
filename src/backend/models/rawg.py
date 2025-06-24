from pydantic import BaseModel
from typing import List, Optional

class RawgData(BaseModel):
    name: str
    score: int
    top_media_scores: Optional[List[dict]] = None 


    
