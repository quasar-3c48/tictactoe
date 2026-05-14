# tic tac toe

Simple TicTacToe project in **Python + Tkinter**.

## Features
- Playable TicTacToe vs computer
- Computer plays a random valid move
- Choose your symbol before starting (X or O)
- Standard win/draw rules
- Replay without reloading the app

## Run
From the project root:

```bash
python3 main.py
```

If needed, with local venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 main.py
```
## Evolvability
- The board size `BOARD_SIZE` and the win length `WIN_LENGTH` are configurable in `config.py`
- Computer strategy is isolated in `models/strategy_computer.py`
- MVC separation keeps UI, flow, and game rules independent
