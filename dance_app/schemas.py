from pydantic import BaseModel, Field
from typing import Optional
from .instructors import Instructor

class DanceRoutineBase(BaseModel):
    name: str
    style: str
    instructor: Instructor
    difficulty: int = Field(ge=1, le=5)
    duration_minutes: int = Field(gt=0)
    song_name: str
    description: Optional[str] = None

class DanceRoutineCreate(DanceRoutineBase):
    pass

class DanceRoutine(DanceRoutineBase):
    id: int