#import os
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

#from dotenv import load_dotenv

#load_dotenv()

#from dotenv import load_dotenv

#POSTGRES_USER = os.getenv("POSTGRES_USER")
#POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
#POSTGRES_HOST = os.getenv("POSTGRES_HOST")

DATABASE_URL = "postgresql://postgres:postgres@10.0.1.4:5432/postgres"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
