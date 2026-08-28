from backend.database import SessionLocal, Workout
from sqlalchemy import select
from fastapi import APIRouter
from pydantic import BaseModel


workout_router = APIRouter()

class WorkoutSchema(BaseModel):
    id: int
    weight: float
    reps: int
    exercise: str

    class Config:
        from_attributes = True


@workout_router.get("/api/get_workouts", response_model=list[WorkoutSchema]) 
def get_workouts():

    with SessionLocal() as session:
        statement = select(Workout)
        result = session.scalars(statement).all()
    return (result)