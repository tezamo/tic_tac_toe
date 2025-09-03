# 🎮 Tic Tac Toe (Streamlit)

A simple, one-screen Tic Tac Toe game built with Streamlit. Two players click alternately in the same browser tab. Scores persist for the session.

## Local Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the URL shown (usually http://localhost:8501).

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io/
3. Click **Deploy App** → connect your GitHub repo.
4. Select `app.py` as the entry file and deploy.
5. Copy the deployed URL and put it in your GitHub README so people can play with one click.

## Codespaces (optional)

```bash
pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0 --server.port 7860
```
Forward the port (e.g., 7860) and open the preview link.

## Play Online

Click here to play Tic Tac Toe in your browser:

[Play Tic Tac Toe](https://tictactoe-mxetgvjyzlm5ffg9svwmo8.streamlit.app/)

