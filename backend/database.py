import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Column, Integer, Float, String
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
#Create ORM Model Workout
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    exercise = Column(String)
    weight = Column(Float)
    reps = Column(Integer)

##Create column
# Base.metadata.create_all(engine)

# with SessionLocal() as session:
#     #Create object of workout
#     workout1 = Workout(exercise = "evening workout2", weight = 50,reps = 20)
#     workout2 = Workout(exercise = "night workout", weight = 50,reps = 20)
#     #Insert object and commit
#     session.add_all([workout1, workout2])
#     session.commit()