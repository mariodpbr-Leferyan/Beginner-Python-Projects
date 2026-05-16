# 🐍 Python Projects — Mário Rosa

A collection of Python games and utilities built as part of my programming portfolio.
Each project is self-contained and runs in the terminal.

\---

## 📁 Projects

|Project|Type|Libraries|
|-|-|-|
|💱 Currency Converter|Utility|`requests`|
|❌⭕ Tic-Tac-Toe|Game|None|
|🏝️ Treasure Hunt|Game|None|
|🪓 Hangman|Game|None|

\---

## 💱 Currency Converter — EUR ↔ USD

Fetches **live exchange rates** from a public API and converts between Euros and US Dollars.

**Features:**

* Real-time EUR/USD rate via the [Frankfurter API](https://www.frankfurter.app/) (free, no API key required)
* Converts EUR → USD or USD → EUR
* Input validation and error handling (network errors, invalid values)

**Run:**

```bash
cd currency\_converter
pip install -r requirements.txt
python main.py
```

**Example:**

```
Fetching live exchange rate...
Current rate: 1 EUR = 1.0832 USD

Choose the conversion direction:
1. Euros -> Dollars
2. Dollars -> Euros
0. Quit
> 1

Amount (0 to quit): 100
Amount in dollars: 100.0 € -> 108.32 $
```

\---

## ❌⭕ Tic-Tac-Toe — Two Player CLI Game

Classic Tic-Tac-Toe for two players in the terminal.

**Features:**

* Dynamic board display after each move
* Win detection across rows, columns and both diagonals
* Draw detection when the board is full
* Input validation — rejects letters, out-of-bounds and taken positions

**Run:**

```bash
cd tic\_tac\_toe
python main.py
```

**Example:**

```
TIC-TAC-TOE
===========
1-Instructions
2-Play
3-Quit

Option: 2

 . . .
 . X .
 . . .
Player O \[2]>
Row: 1
Column: 1
...
Player X won in 5 moves.
```

\---

## 🏝️ Treasure Hunt — Text Adventure Game

A branching text adventure where every choice leads to a different outcome.

**Features:**

* Three decision points with multiple paths
* ASCII art introduction
* Clear win/lose feedback at each stage

**Run:**

```bash
cd treasure\_hunt
python main.py
```

**Story Map:**

```
Start
 ├── LEFT ✅
 │    └── WAIT ✅
 │         ├── YELLOW → 🏆 WIN
 │         ├── RED    → 💀 GAME OVER
 │         └── BLUE   → 💀 GAME OVER
 │    ├── SWIM → 💀 GAME OVER
 │    └── BOAT → 💀 GAME OVER
 └── RIGHT → 💀 GAME OVER
```

\---

## 🪓 Hangman — Word Guessing Game

Classic Hangman with ASCII art stages and a 200+ word list.

**Features:**

* 200+ challenging words
* ASCII hangman updates with each wrong guess (6 lives)
* Tracks and displays wrong guesses
* Input validation — rejects numbers, multiple letters and repeated guesses
* Play again option after each round

**Run:**

```bash
cd hangman
python main.py
```

**Example:**

```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*6/6 LIVES LEFT\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Word to guess: \_ \_ \_ \_ \_ \_
Wrong guesses: e, t

Guess a letter: a
✅ 'a' is in the word!

Word to guess: \_ a \_ \_ \_ \_
```

\---

## 📁 Repository Structure

```
python-projects/
│
├── currency\_converter/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── tic\_tac\_toe/
│   ├── main.py
│   └── README.md
│
├── treasure\_hunt/
│   ├── main.py
│   └── README.md
│
├── hangman/
│   ├── main.py
│   ├── hangman\_art.py
│   ├── hangman\_words.py
│   └── README.md
│
└── README.md   ← este ficheiro
```

\---

## ⚙️ Requirements

* Python 3.x
* `requests` library (only for Currency Converter):

```bash
pip install requests
```

\---

## 👤 Author

**Mário Rosa**

* 🔗 [LinkedIn](https://linkedin.com/in/mario-pinheiro-rosa)
* 🐙 [GitHub](https://github.com/mariodpbr-Leferyan/Beginner-Python-Projects)

