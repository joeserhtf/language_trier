from pydantic import BaseModel
from typing import List

class Drink(BaseModel):
    id: int
    name: str
    description: str
    image: str
    observations: List[str]