# ❌⭕ Tic-Tac-Toe — Python CLI Game

A classic **Tic-Tac-Toe** two-player game played in the terminal, built with pure Python.

\---

## 🚀 Features

* Two-player mode (X and O)
* Dynamic board display after each move
* Win detection across rows, columns and both diagonals
* Draw detection when the board is full
* Input validation — rejects out-of-bounds and already-taken positions
* Instructions menu included

\---

## 🛠️ Technologies

* Python 3.x
* No external libraries required

\---

## ⚙️ Installation \& Run

1. Clone the repository:

git clone https://github.com/mariodpbr-Leferyan/Beginner-Python-Projectss.git
cd python-projects/tic\_tac\_toe


2. Run the program:

python main.py


\---

## 📋 Usage Example

```
TIC-TAC-TOE
===========
1-Instructions
2-Play
3-Quit

Option: 2

 . . .
 . . .
 . . .
Player X \[1]>
Row: 2
Column: 2

 . . .
 . X .
 . . .
Player O \[2]>
...
Player X won in 5 moves.


\---

## 🧠 How It Works

* The board is a 3×3 matrix initialized with empty positions (`.`)
* Each turn, the active player inputs a row and column (1–3)
* After each move, the game checks all rows, columns and diagonals for a winning sequence
* If all 9 positions are filled with no winner, the game ends in a draw

\---

## 📁 Project Structure

```
tic\_tac\_toe/
├── main.py     # Main application
└── README.md   # This file
```

\---

## 👤 Author

**Mário Rosa** · [LinkedIn](https://linkedin.com/in/mario-pinheiro-rosa) · [GitHub](https://github.com/mariodpbr-Leferyan)

