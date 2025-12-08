
from db.database import sessionLocal

def connect_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()    
       