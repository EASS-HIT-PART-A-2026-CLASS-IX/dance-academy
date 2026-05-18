from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/recommend")
def recommend(difficulty: int):
    # מביא את כל הרוטינות מה-backend
    response = requests.get("http://127.0.0.1:8000/routines")
    routines = response.json()

    # מסנן רק רוטינות עם אותו difficulty בדיוק
    filtered = [
        r["name"]
        for r in routines
        if r["difficulty"] == difficulty
    ]

    # אם אין התאמות
    if not filtered:
        return {"recommendations": ["No exact match found"]}

    return {"recommendations": filtered}