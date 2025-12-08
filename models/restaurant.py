from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class restaurant_info(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True)
    res_name = Column(String)
    status_check = Column(Boolean)
    rating=Column(Integer)
    address=Column(String)
