from backend.database import Base
from sqlalchemy import Column, Integer, Float, String


#Create ORM Model Workout
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    exercise = Column(String)
    weight = Column(Float)
    reps = Column(Integer)