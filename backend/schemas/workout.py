from pydantic import BaseModel

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