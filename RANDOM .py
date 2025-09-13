import time
import streamlit as st

# Controls
st.set_page_config(page_title="Big Number Repeater", layout="centered")
st.title("Big Number Repeater")

with st.sidebar:
    repeats = st.number_input("Repeats per number", 1, 20, 5)
    delay = st.number_input("Seconds per repeat", 0.1, 10.0, 1.0, step=0.1)
    end_at = st.number_input("End at number", 1, 100, 10)
    start = st.button("Start")

placeholder = st.empty()

def show_num(n: int):
    placeholder.markdown(
        f"""
        <div style="display:flex;align-items:center;justify-content:center;height:70vh;background:#fff;">
            <span style="font-size:200px;font-weight:800;color:#222;">{n}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Run animation
if start:
    st.session_state["stop"] = False
    for n in range(1, int(end_at) + 1):
        for _ in range(int(repeats)):
            if st.session_state.get("stop"):
                break
            show_num(n)
            time.sleep(float(delay))
        if st.session_state.get("stop"):
            break

# Optional Stop button
if st.button("Stop"):
    st.session_state["stop"] = True
