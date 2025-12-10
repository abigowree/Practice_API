from sqlalchemy import Column, Integer,String,Boolean,ForeignKey
from db.database import Base,relationship


class order_information(Base):
    __tablename__="orders"


    order_id=Column(Integer,primarykey=True)
    user_id=Column(Integer,primarykey=True("user_id"))
    rest_id=Column(Integer,ForeignKey("rest.id"))
    total_amount=Column(Integer)
        