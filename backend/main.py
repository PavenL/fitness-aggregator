from fastapi import FastAPI, APIRouter
from backend.api.workouts import workout_router

app = FastAPI()

router = APIRouter()
app.include_router(workout_router)

@app.get("/")
def root():
    return {"message": "Hello World"}



