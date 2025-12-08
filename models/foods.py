
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Food_information(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    qty = Column(Integer, nullable=False)
    availability = Column(Boolean, default=True)