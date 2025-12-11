
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker,declarative_base
# from core.config import username

# print(username)

# username="postgres"
# password="Abi%402007-5"
# hostname="localhost"
# port="5432"
# db_name="sample_db"

# DB_URL=f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}"



# engine=create_engine(DB_URL)

# sessionLocal= sessionmaker (bind=engine,autoflush=False)

# Base=declarative_base() 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

username="postgres"
password="Abi%402007-5"
hostname="localhost"
port="5432"
db_name="editdb"

DB_URL=f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}"
 


engine=create_engine(DB_URL)

sessionLocal= sessionmaker (bind=engine,autoflush=False)

Base=declarative_base() 