# 🪓 Hangman — Python CLI Game

A classic **Hangman** word-guessing game played in the terminal, built with pure Python. Features ASCII art stages and a large word list of challenging English words.

\---

## 🚀 Features

* 200+ word list with challenging vocabulary
* ASCII art hangman that updates with each wrong guess
* 6 lives — one per wrong letter
* Detects already-guessed letters and warns the player
* Win/lose detection with the correct word revealed on loss
* Clean logo display on start

\---

## 🛠️ Technologies

* Python 3.x
* No external libraries required

\---

## ⚙️ Installation \& Run

1. Clone the repository:

git clone https://github.com/mariodpbr-Leferyan/Beginner-Python-Projectss.git
cd python-projects/hangman


2. Run the game:

python main.py


> All three files (`main.py`, `hangman\_art.py`, `hangman\_words.py`) must be in the same folder.

\---

## 📋 Usage Example

```
 \_
| |\_\_   \_\_ \_ \_ \_\_   \_\_ \_ \_ \_\_ \_\_\_   \_\_ \_ \_ \_\_
| '\_ \\ / \_` | '\_ \\ / \_` | '\_ ` \_ \\ / \_` | '\_ \\
...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*6/6 LIVES LEFT\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Word to guess: \_ \_ \_ \_ \_ \_
Guess a letter: a

Word to guess: \_ \_ a \_ \_ \_

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*5/6 LIVES LEFT\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Guess a letter: e
You guessed e, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
      |
      |
      |
=========
```

\---

## 📁 Project Structure

```
hangman/
├── main.py            # Game logic
├── hangman\_art.py     # ASCII art — logo and hangman stages
├── hangman\_words.py   # Word list (200+ words)
└── README.md          # This file
```

\---

## 🧠 How It Works

* A random word is selected from `hangman\_words.py`
* The player guesses one letter at a time
* Correct guesses reveal the letter in the word display
* Wrong guesses cost a life and update the ASCII hangman
* The game ends when the word is complete (win) or lives reach 0 (lose)

\---

## 👤 Author

**Mário Rosa** · [LinkedIn](https://linkedin.com/in/mario-pinheiro-rosa) · [GitHub](https://github.com/mariodpbr-Leferyan)

