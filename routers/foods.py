from fastapi import APIRouter,Depends
from schemas.foods import Foods
from db.database import Base,engine
from dependencies import connect_db
from sqlalchemy.orm import session
from models.foods import Food_information


food_router =APIRouter(
    prefix="/food",
    tags=["Food"]
)

@food_router.get("/")
def get_all_products(dbs:session=Depends(connect_db)):
    all_product=dbs.query(Food_information).all()
    return all_product

    


@food_router.get("/{id}")
def all_products_by_id(id:int):
    return {"message":"update all succesfully"}


@food_router.post("/")
def create_products(new_food:Foods, dbs:session=Depends(connect_db)):
    new_entry=Food_information(
        food_name=new_food.food_name,
        price=new_food.price,
        qty=new_food.qty,
        availability=new_food.availability

    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)

    


@food_router.put("/{id}")
def update_products(id:int,changed:Foods,dbs:session=Depends(connect_db)):
    changes=dbs.query(Food_information).filter(Food_information.id==id).first()
    if not changes:
        return {"message":"invalid id"}
    changes.food_name=changed.food_name
    changes.price=changed.price,
    changes.qty=changed.qty,
    changes.availability=changed.availability
    dbs.add(changes)
    dbs.commit()
    dbs.refresh(changes)
    

@food_router.delete("/{id}")
def delete_products(id:int,dbs:session=Depends(connect_db)):
    deleted=dbs.query(Food_information).filter(Food_information.id==id).first()
    if not deleted:
        return {"message":"invalid id"}
    dbs.delete(deleted)
    dbs.commit()
   
    return {"message":"id deleted succesfully"}

