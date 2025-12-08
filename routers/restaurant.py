
from fastapi import APIRouter,Depends
from schemas.restaurant import Restaurant
from db.database import Base,engine
from dependencies import connect_db
from sqlalchemy.orm import session
from models.restaurant import restaurant_info


res_router =APIRouter(
    prefix="/restaurant",
    tags=["Restaurant"]
)

@res_router.get("/")
def get_all_products(dbs:session=Depends(connect_db)):
    all_product=dbs.query(restaurant_info).all()
    return all_product

    


@res_router.get("/{id}")
def all_products_by_id(id:int):
    return {"message":"update all succesfully"}


@res_router.post("/")
def create_products(new_res:Restaurant, dbs:session=Depends(connect_db)):
    new_entry=restaurant_info(
        res_name=new_res.res_name,
        status_check=new_res.status_check,
        rating=new_res.rating,
        address=new_res.address

    )
    dbs.add(new_entry)
    dbs.commmit()
    dbs.refresh(new_entry)

    


@res_router.put("/{id}")
def update_products(id:int,changed:Restaurant,dbs:session=Depends(connect_db)):
    changes=dbs.query(restaurant_info).filter(restaurant_info.id==id).first()
    if not changes:
        return {"message":"invalid id"}
    changes.res_name=changed.res_name
    changes.status_check=changed.status_check ,
    changes.rating=changed.rating,
    changes.address=changed.address
    dbs.add(changes)
    dbs.commit()
    dbs.refresh(changes)
    

@res_router.delete("/{id}")
def delete_products(id:int,dbs:session=Depends(connect_db)):
    deleted=dbs.query(restaurant_info).filter(restaurant_info.id==id).first()
    if not deleted:
        return {"message":"invalid id"}
    dbs.delete(deleted)
    dbs.commit()
   
    return {"message":"id deleted succesfully"}