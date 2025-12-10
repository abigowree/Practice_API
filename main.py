from fastapi import FastAPI
from db.database import engine,Base
#step1 routers --> foods router import
from routers.foods import food_router
from schemas.foods import Foods
from routers.restaurant import res_router
from routers.users import user_router

Base.metadata.create_all(bind=engine)

app =FastAPI()


#get
@app.get("/")
def get_all_products():
    return {"message":""}
#step 2 
app.include_router(food_router)
#step 3
app.include_router(res_router)
#user table
app.include_router(user_router)