from dataclasses import dataclass
from .instructors import Instructor

@dataclass
class DanceRoutineModel:
    id: int
    name: str
    style: str
    instructor: Instructor
    difficulty: int
    duration_minutes: int
    song_name: str
    description: str | None = None