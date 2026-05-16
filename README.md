# 🏝️ Treasure Hunt — Text Adventure Game

A terminal-based **text adventure game** where the player explores a mysterious island in search of hidden treasure. Every choice matters!

\---

## 🚀 Features

* Interactive branching story with multiple paths
* Three decision points with different outcomes
* ASCII art introduction
* Clear win/lose feedback at each stage
* Beginner-friendly code structure

\---

## 🛠️ Technologies

* Python 3.x
* No external libraries required

\---

## ⚙️ Installation \& Run

1. Clone the repository:

git clone https://github.com/mariodpbr-Leferyan/Beginner-Python-Projectss.git
cd python-projects/treasure\_hunt


2. Run the program:

python main.py


\---

## 📋 Usage Example

```
Welcome to the Lost Treasure Island! 🏝️

You arrive at a fork in the jungle path.
To the LEFT, a narrow path covered with vines and exotic flowers.
To the RIGHT, a wide path with recent footprints on the ground.

Choice your path. Narrow path turn LEFT. Wide path turn RIGHT.
> left

You continue safely! ✅

Lake with Island
After hours of walking, you reach a crystal-clear lake...
Will you cross? Choice SWIM, WAIT or BOAT.
> wait

You waited patiently. A mysterious boatman appeared! ✅
...
🔴 RED | 🟡 YELLOW | 🔵 BLUE — Which door do you choose?
> yellow

VICTORY 🏆 You found the treasure! 💰💎👑
```

\---

## 🗺️ Story Map

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

## 📁 Project Structure

```
treasure\_hunt/
├── main.py     # Main application
└── README.md   # This file
```

\---

## 👤 Author

**Mário Rosa** · [LinkedIn](https://linkedin.com/in/mario-pinheiro-rosa) · [GitHub](https://github.com/mariodpbr-Leferyan)

