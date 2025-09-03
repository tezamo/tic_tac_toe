
import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

# --- Session State ---
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None
if "scores" not in st.session_state:
    st.session_state.scores = {"X": 0, "O": 0, "Draws": 0}

WIN_COMBOS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def check_winner(board):
    for a,b,c in WIN_COMBOS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def reset_board():
    st.session_state.board = [""] * 9
    st.session_state.winner = None
    st.session_state.current_player = "X"

def reset_scores():
    st.session_state.scores = {"X": 0, "O": 0, "Draws": 0}

def make_move(i):
    if st.session_state.winner is not None:
        return
    if st.session_state.board[i] == "":
        st.session_state.board[i] = st.session_state.current_player
        winner = check_winner(st.session_state.board)
        if winner:
            st.session_state.winner = winner
            st.session_state.scores[winner] += 1
        elif "" not in st.session_state.board:
            st.session_state.winner = "Draw"
            st.session_state.scores["Draws"] += 1
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# --- UI ---
st.title("🎮 Tic Tac Toe")
st.caption("Two players, one browser tab. Click to play.")

status_area = st.empty()

if st.session_state.winner is None:
    status_area.info(f"Player **{st.session_state.current_player}** to move")
else:
    if st.session_state.winner == "Draw":
        status_area.warning("It's a **draw**!")
    else:
        status_area.success(f"Player **{st.session_state.winner}** wins!")

# Board
for r in range(3):
    cols = st.columns(3, gap="small")
    for c in range(3):
        i = r * 3 + c
        label = st.session_state.board[i] if st.session_state.board[i] else " "
        cols[c].button(label, key=f"cell_{i}", on_click=make_move, args=(i,), use_container_width=True)

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
