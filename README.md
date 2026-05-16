# 💃 Dance Academy

🎓 **Dance Academy** is a full-stack Python application developed as part of the EASS course.

The system allows managing dance routines through a **FastAPI backend** and a **Streamlit user interface**.

---

## ✨ Project Objectives

- 🩰 Model a dance academy domain
- 👩‍🏫 Manage dance routines and instructors
- 🔌 Practice API development using FastAPI
- 🖥️ Build a UI using Streamlit
- ✅ Implement CRUD operations
- 🧪 Fulfill EX1 + EX2 course requirements

---

## 🛠️ Technologies Used

- 🐍 Python 3
- ⚡ FastAPI (Backend API)
- 🖥️ Streamlit (UI)
- 📦 Virtual Environment (`.venv`)
- ⚙️ pyproject.toml
- 🧪 Pytest

---

## 📂 Project Structure

```text
dance-academy/
├── dance_app/
│   ├── main.py
│   ├── main_ex1.py
│   ├── models.py
│   ├── repository.py
│   ├── schemas.py
│   ├── instructors.py
│   └── __init__.py
│
├── interface/
│   ├── app.py         # Streamlit UI
│   └── api.py         # API communication layer
│
├── tests/
│   └── test_routines.py
│
├── pyproject.toml
├── README.md
└── .venv/
