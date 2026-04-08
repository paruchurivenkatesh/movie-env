from pydantic import BaseModel
from typing import List, Optional

class Action(BaseModel):
    action_type: str  # "recommend" or "ask"
    content: str

class Observation(BaseModel):
    user_profile: str
    history: List[str]
    last_feedback: Optional[str]

class Reward(BaseModel):
    score: float