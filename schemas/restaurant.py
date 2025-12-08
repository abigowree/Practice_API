
from pydantic import BaseModel

class Restaurant(BaseModel):
    res_name: str
    status_check: bool
    rating: int
    address: str