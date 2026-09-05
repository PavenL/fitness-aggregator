from backend.database import SessionLocal, Workout
from sqlalchemy import select
from fastapi import APIRouter
from pydantic import BaseModel


workout_router = APIRouter()

#Create pydantic schema for data leaving API
class WorkoutSchema(BaseModel):
    id: int
    weight: float
    reps: int
    exercise: str

    class Config:
        from_attributes = True

#Pydantic model for data entering API
class WorkoutCreate(BaseModel):
    weight: float
    reps: int
    exercise: str

#set workout route
@workout_router.get("/api/get_workouts", response_model=list[WorkoutSchema]) 
def get_workouts():

    with SessionLocal() as session:
        #get workout and convert result to scalar
        statement = select(Workout)
        result = session.scalars(statement).all()
    return (result)

#Insert new record
@workout_router.post("/api/insert_workouts") 
def insert_workouts(workout: WorkoutCreate):

    with SessionLocal() as session:
        #Convert Pydantic model -> dictionary -> SQLAlchemy ORM
        workout_orm = Workout(**workout.model_dump())
        #Add new item into DB
        session.add(workout_orm)
        session.commit()
        session.refresh(workout_orm)
        return (workout_orm)