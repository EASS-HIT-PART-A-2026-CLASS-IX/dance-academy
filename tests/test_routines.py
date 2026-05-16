from fastapi.testclient import TestClient
from dance_app.main_ex1 import app

client = TestClient(app)


def valid_payload():
    return {
        "name": "Hip Hop Basics",
        "style": "HipHop",
        "instructor": "Lian Reifman",
        "difficulty": 2,
        "duration_minutes": 60,
        "song_name": "Work It Out",
        "description": "Warmup and isolation routine"
    }


def test_list_routines_empty():
    response = client.get("/routines")
    assert response.status_code == 200
    assert response.json() == []


def test_create_routine():
    response = client.post("/routines", json=valid_payload())
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Hip Hop Basics"
    assert data["difficulty"] == 2
    assert "id" in data


def test_delete_routine():
    create_response = client.post("/routines", json=valid_payload())
    routine_id = create_response.json()["id"]

    delete_response = client.delete(f"/routines/{routine_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"ok": True}