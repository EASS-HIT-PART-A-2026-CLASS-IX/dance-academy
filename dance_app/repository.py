from typing import Dict, List
from .models import DanceRoutineModel
from .schemas import DanceRoutineCreate

class DanceRoutineRepository:
    def __init__(self):
        self._db: Dict[int, DanceRoutineModel] = {}
        self._id_counter = 1

    def list(self) -> List[DanceRoutineModel]:
        return list(self._db.values())

    def create(self, data: DanceRoutineCreate) -> DanceRoutineModel:
        routine = DanceRoutineModel(
            id=self._id_counter,
            **data.model_dump()
        )
        self._db[self._id_counter] = routine
        self._id_counter += 1
        return routine

    def get(self, routine_id: int):
        return self._db.get(routine_id)

    def update(self, routine_id: int, data: DanceRoutineCreate):
        if routine_id not in self._db:
            return None
        updated = DanceRoutineModel(
            id=routine_id,
            **data.model_dump()
        )
        self._db[routine_id] = updated
        return updated

    def delete(self, routine_id: int) -> bool:
        return self._db.pop(routine_id, None) is not None