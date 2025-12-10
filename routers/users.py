from fastapi import APIRouter,Depends
from models.users import UserTable
from schemas.users import CustomerTable
from db.database import create_engine
from sqlalchemy.orm import session
from dependencies import connect_db

user_router=APIRouter(
    prefix="/user_detail",
    tags=["User_info"]

)
#get
@user_router.get("/")
def show_all_user(dbs:session=Depends(connect_db)):
    all_user=dbs.query(UserTable).all()
    return all_user
#post 
@user_router.post("/")
def create_user_detail(add_detail:CustomerTable,dbs:session=Depends(connect_db)):
    new_entry=UserTable(
        user_name=add_detail.user_name,
        email=add_detail.email,
        city=add_detail.city

    )

    dbs.add(new_entry)
    dbs.commit()
    dbs.refresh(new_entry)

#get by id
@user_router.get("/{user_id}")
def show_user_only(user_id:int,dbs:session=Depends(connect_db)):
    all_user=dbs.query(UserTable).filter(UserTable.user_id == user_id).first()
    return all_user

#put 
@user_router.put("/{user_id}")
def update_user_detail(user_id:int, changed:CustomerTable,dbs:session=Depends(connect_db)):
    alter_user=dbs.query(UserTable).filter(UserTable.user_id==user_id).first()
    if not alter_user:
        return{"message":"user not found"}
    alter_user.user_name=changed.user_name,
    alter_user.email=changed.email,
    alter_user.city=changed.city
   
    dbs.commit()
    dbs.refresh(alter_user)

#delete
@user_router.delete("/{user_id}")
def delete_user(user_id:int,dbs:session=Depends(connect_db)):
    deleted=dbs.query(UserTable).filter(UserTable.user_id==user_id).first()
    if not deleted:
        return {"message":"user not found"}
    dbs.delete(deleted)
    dbs.commit()
   
    return {"message":"id deleted succesfully"}
                    


    


    
   
    