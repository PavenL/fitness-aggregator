from backend.database import SessionLocal, Workout
from sqlalchemy import select
from fastapi import APIRouter


workout_router = APIRouter()


@workout_router.get("/api/get_workouts")

def get_workouts():

    with SessionLocal() as session:
        statement = select(Workout)
        result = session.execute(statement)

    return [result]
