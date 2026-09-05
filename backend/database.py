import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

##Test DB connection
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT 1"))
#     print("Database test:", result.scalar())

#Create base class
Base = declarative_base()