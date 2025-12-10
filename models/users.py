from sqlalchemy import Column, Integer, String
from db.database import Base

class UserTable(Base): 
    __tablename__= "user_table"

    user_id=Column(Integer,primary_key=True,index=  True)
    user_name=Column(String)
    email=Column(String)
    city=Column(String)