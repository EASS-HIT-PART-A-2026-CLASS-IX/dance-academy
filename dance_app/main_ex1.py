from fastapi import FastAPI, HTTPException
from .repository import DanceRoutineRepository
from .schemas import DanceRoutine, DanceRoutineCreate

app = FastAPI(title="Dance Studio Manager – EX1")

repo = DanceRoutineRepository()


@app.get("/routines", response_model=list[DanceRoutine])
def list_routines():
    return repo.list()


@app.post("/routines", response_model=DanceRoutine, status_code=201)
def create_routine(data: DanceRoutineCreate):
    return repo.create(data)


@app.get("/routines/{routine_id}", response_model=DanceRoutine)
def get_routine(routine_id: int):
    routine = repo.get(routine_id)
    if not routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    return routine


@app.put("/routines/{routine_id}", response_model=DanceRoutine)
def update_routine(routine_id: int, data: DanceRoutineCreate):
    routine = repo.update(routine_id, data)
    if not routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    return routine


@app.delete("/routines/{routine_id}")
def delete_routine(routine_id: int):
    deleted = repo.delete(routine_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Routine not found")
    return {"ok": True}