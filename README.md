# 🎮 Tic Tac Toe (Streamlit)

A simple, one-screen Tic Tac Toe game built with Streamlit. Two players click alternately in the same browser tab. Scores persist for the session.



## How to Play

- Two players take turns clicking on the 3×3 grid.

- Player X always goes first.

- The first to line up three symbols horizontally, vertically, or diagonally wins.

 - Scores are tracked for the current session.

  - Hit Reset Board to start a new game, or Reset Scores to clear session stats.

## Local Run

```bash

git clone <your-repo-url>
cd tictactoe-streamlit
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

[🎮 Play Tic Tac Toe 🎮](https://tictactoe-mxetgvjyzlm5ffg9svwmo8.streamlit.app/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

For questions or contributions, open an issue or contact [me](mailto:tezamo@web.de).

[![pages-build-deployment](https://github.com/tezamo/tic_tac_toe/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/tezamo/tic_tac_toe/actions/workflows/pages/pages-build-deployment)
[![contributors](https://img.shields.io/github/contributors/tezamo/tic_tac_toe.svg)](https://github.com/tezamo/tic_tac_toe/graphs/contributors)
[![GitHub release](https://img.shields.io/github/v/release/tezamo/tic_tac_toe.svg)](https://GitHub.com/tezamo/tic_tac_toe/releases/)
[![GitHub license](https://img.shields.io/github/license/tezamo/tic_tac_toe.svg)](https://github.com/tezamo/tic_tac_toe/blob/main/LICENSE)