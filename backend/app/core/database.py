from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()

#Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/erp-db")

#create database engine
engine = create_engine(DATABASE_URL)

#create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class for models
Base = declarative_base()

#Dependency to get Database sesion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()