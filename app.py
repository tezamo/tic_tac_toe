
import streamlit as st

st.set_page_config(page_title="Tic Tac Toe by tezamo", page_icon="🎮", layout="centered")

# --- Session State ---
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

# removed for privacy concerns
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

# Controls
col1, col2, col3 = st.columns([1,1,2])
with col1:
    st.button("🔄 Reset Board", on_click=reset_board, use_container_width=True)
with col2:
    st.button("🧹 Reset Scores", on_click=reset_scores, use_container_width=True)

# Scoreboard
with col3:
    st.subheader("Scoreboard")
    st.write(f"**X**: {st.session_state.scores['X']}  |  **O**: {st.session_state.scores['O']}  |  **Draws**: {st.session_state.scores['Draws']}")

st.markdown("---")
st.caption("Built with Streamlit. Share this app by deploying the repo on Streamlit Community Cloud.")
