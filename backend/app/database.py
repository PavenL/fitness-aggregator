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
class workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    excercise = Column(String)
    weight = Column(Float)
    reps = Column(Integer)

    def __init__ (self, id, excercise,weight,reps):
        self.id = id
        self.excercise = excercise
        self.weight = weight
        self.reps = reps

# Base.metadata.create_all(engine)

with SessionLocal() as session:
    workout1 = workout(1,"afternoon workout",50,20)

    session.add(workout1)
    session.commit()
    session.close()