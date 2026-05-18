import streamlit as st
import requests
from api import get_routines, add_routine, delete_routine

st.set_page_config(page_title="Dance Academy", layout="centered")

st.title("🎓 Dance Academy")
st.write("Manage dance routines and view academy statistics.")

# =========================
# Refresh Button
# =========================
if st.button("🔄 Refresh routines"):
    st.rerun()

# =========================
# Summary Statistics (LOCAL)
# =========================
st.subheader("📊 Summary")

try:
    routines = get_routines()
    total_routines = len(routines)

    if total_routines > 0:
        avg_difficulty = sum(r["difficulty"] for r in routines) / total_routines
        avg_duration = sum(r["duration_minutes"] for r in routines) / total_routines

        col1, col2, col3 = st.columns(3)
        col1.metric("Total routines", total_routines)
        col2.metric("Average difficulty", round(avg_difficulty, 2))
        col3.metric("Average duration (min)", round(avg_duration, 1))
    else:
        st.info("No routines yet – add the first one!")
except Exception:
    st.warning("Statistics unavailable.")

st.divider()

# =========================
# External Stats Service (IMPROVED ✅)
# =========================
st.subheader("🌐 External Stats Service")

if st.button("Load external stats"):
    try:
        response = requests.get("http://127.0.0.1:8000/external-stats")
        data = response.json()

        st.success("✅ Stats loaded from external service")

        col1, col2 = st.columns(2)

        col1.metric(
            "Total routines (external)",
            data["total_routines"]
        )

        col2.metric(
            "Average difficulty (external)",
            round(data["average_difficulty"], 2)
        )

    except Exception as e:
        st.error(f"Error loading stats: {e}")

st.divider()

# =========================
# Recommendation UI (IMPROVED ✅)
# =========================
st.subheader("🎯 Get Recommendation")

difficulty_choice = st.slider("Choose difficulty", 1, 5)

if st.button("Get Recommendation"):
    try:
        response = requests.get(
            f"http://127.0.0.1:8000/recommendations?difficulty={difficulty_choice}"
        )

        result = response.json()

        st.success("✅ Recommendation loaded")

        st.markdown("### 💃 Recommended routines")

        for rec in result["recommendations"]:
            st.markdown(f"- ✅ **{rec}**")

    except Exception as e:
        st.error(f"Error: {e}")

st.divider()

# =========================
# List Routines
# =========================
st.subheader("📋 Routines")

try:
    routines = get_routines()

    if routines:
        for routine in routines:
            with st.expander(f"{routine['name']} ({routine['style']})"):
                st.write(f"**Instructor:** {routine['instructor']}")
                st.write(f"**Difficulty:** {routine['difficulty']}")
                st.write(f"**Duration:** {routine['duration_minutes']} minutes")
                st.write(f"**Song:** {routine['song_name']}")
                st.write(f"**Description:** {routine['description']}")

                if st.button(f"❌ Delete routine {routine['id']}", key=routine["id"]):
                    try:
                        delete_routine(routine["id"])
                        st.success("Deleted successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error deleting: {e}")
    else:
        st.info("No routines found.")

except Exception as e:
    st.error(f"Error loading routines: {e}")

st.divider()

# =========================
# Add New Routine
# =========================
st.subheader("➕ Add a new routine")

with st.form("add_routine_form"):
    name = st.text_input("Routine name")
    style = st.text_input("Dance style")
    instructor = st.text_input("Instructor")

    difficulty = st.number_input(
        "Difficulty (1–5)", min_value=1, max_value=5, value=1
    )

    duration_minutes = st.number_input(
        "Duration (minutes)", min_value=1, value=1
    )

    song_name = st.text_input("Song name")
    description = st.text_area("Description")

    submitted = st.form_submit_button("Add routine")

    if submitted:
        if not name or not style or not instructor:
            st.warning("Please fill in all required fields.")
        else:
            try:
                add_routine(
                    {
                        "name": name,
                        "style": style,
                        "instructor": instructor,
                        "difficulty": difficulty,
                        "duration_minutes": duration_minutes,
                        "song_name": song_name,
                        "description": description,
                    }
                )
                st.success("✅ Routine added successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Failed to add routine: {e}")