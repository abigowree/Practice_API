
from pydantic import BaseModel

class Foods(BaseModel):
    food_name: str
    price: int
    qty: int
    availability: bool
