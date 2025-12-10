from pydantic import BaseModel

class CustomerTable(BaseModel):
    user_id:int
    user_name:str
    email:str
    city:str