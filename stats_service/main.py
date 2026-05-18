from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/stats")
def get_stats():
    # מבקש את כל הרוטינות מה-backend
    response = requests.get("http://127.0.0.1:8000/routines")
    routines = response.json()

    total = len(routines)

    # אם אין רוטינות
    if total == 0:
        return {
            "total_routines": 0,
            "average_difficulty": 0
        }

    # מחשב ממוצע difficulty
    avg_difficulty = sum(r["difficulty"] for r in routines) / total

    return {
        "total_routines": total,
        "average_difficulty": avg_difficulty
    }