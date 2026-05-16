import requests

BASE_URL = "http://localhost:8000"

# =========================
# GET all routines
# =========================
def get_routines():
    response = requests.get(f"{BASE_URL}/routines")
    response.raise_for_status()
    return response.json()

# =========================
# ADD routine
# =========================
def add_routine(routine_data: dict):
    response = requests.post(
        f"{BASE_URL}/routines",
        json=routine_data
    )
    response.raise_for_status()
    return response.json()

# =========================
# DELETE routine
# =========================
def delete_routine(routine_id: int):
    response = requests.delete(f"{BASE_URL}/routines/{routine_id}")
    response.raise_for_status()
    return response.json()

# =========================
# (בונוס קטן) GET routine by id
# =========================
def get_routine_by_id(routine_id: int):
    response = requests.get(f"{BASE_URL}/routines/{routine_id}")
    response.raise_for_status()
    return response.json()