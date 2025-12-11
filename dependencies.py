from db.database import sessionLocal

def connect_to_db():
    db = sessionLocal()
    try:
        print("Connected to DB")
        yield db
    finally:

        db.close()