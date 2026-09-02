from fastapi import FastAPI, APIRouter
from backend.api.workouts import workout_router

app = FastAPI()

router = APIRouter()
#include workout router
app.include_router(workout_router)

@app.get("/")
def root():
    return {"message": "Hello World"}



