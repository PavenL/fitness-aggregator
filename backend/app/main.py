from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/api/workouts")
def root():
    return [
  {
    "exercise": "Bench Press",
    "weight": 70,
    "reps": 8
  },
  {
    "exercise": "Bench Press",
    "weight": 70,
    "reps": 7
  }
]
