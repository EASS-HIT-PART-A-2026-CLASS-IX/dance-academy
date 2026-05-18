# 💃 Dance Academy

🎓 **Dance Academy** is a full-stack Python application developed as part of the EASS course.

The system evolved across three exercises (EX1, EX2, EX3) and demonstrates the transition from a simple API to a complete multi-service system.

👉 This project builds upon EX1 and EX2 and extends them into a multi-service architecture.

---

## ✨ Project Objectives

- 🩰 Model a dance academy domain
- 👩‍🏫 Manage dance routines and instructors
- 🔌 Practice API development using FastAPI
- 🖥️ Build a UI using Streamlit
- ✅ Implement CRUD operations
- 🧪 Fulfill EX1 + EX2 requirements
- 🔗 Build a multi-service architecture (EX3)

---

## 🛠️ Technologies Used

- 🐍 Python 3
- ⚡ FastAPI (Backend API)
- 🖥️ Streamlit (UI)
- 🌐 Requests (service communication)
- 📦 Virtual Environment (`.venv`)
- ⚙️ pyproject.toml
- 🧪 Pytest

---

## 📂 Project Structure

```text
Dance-Academy-Pro/
├── dance_app/                # Backend (EX1)
│   ├── main.py
│   ├── main_ex1.py
│   ├── models.py
│   ├── repository.py
│   ├── schemas.py
│   ├── instructors.py
│
├── recommendation_service/  # EX3
│   └── main.py
│
├── stats_service/           # EX3
│   └── main.py
│
├── interface/               # EX2 + EX3 UI
│   ├── app.py
│   └── api.py
│
├── tests/
│   └── test_routines.py
│
├── pyproject.toml
├── README.md
└── .venv/