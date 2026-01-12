# 🎮 Rock Paper Scissors — Modular Python Game

A clean, modular implementation of the classic **Rock–Paper–Scissors** game built in Python.

---

## 📌 Project Overview

This is a terminal-based interactive game where a user plays Rock–Paper–Scissors against the computer.

### Key Features
- 🎯 User input validation with retry handling
- 🤖 Randomized computer opponent
- 🧩 Modular architecture using functions and separate files
- ♻️ DRY (Don’t Repeat Yourself) principle using shared constants
- 🧠 Clear and readable game-winning logic
- 🎨 Emoji-based visual feedback

---

## 🧱 Project Structure

```text
rock-paper-scissors/
│
├── main.py         # Application entry point
├── game.py         # Core game logic and flow
├── constants.py    # Shared constants and emoji mappings
└── README.md
```

---

## ⚙️ Tech Stack

- **Language:** Python 3
- **Standard Library:** `random`
- **Paradigm:** Procedural + Functional Design
- **Environment:** Command Line Interface (CLI)

No external dependencies — fully portable and easy to run.

---

## 🧠 Design Decisions

### Modularization
The game is broken into **single-responsibility functions**:
- `get_user_choice()` – input handling and validation
- `get_computer_choice()` – randomness abstraction
- `display_choices()` – presentation logic
- `determine_winner()` – business logic
- `play_game()` – game orchestration

This mirrors production-level code organization and improves maintainability.

---

### DRY Principle
All game symbols (`r`, `p`, `s`) are defined **once** in `constants.py`.

```python
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
```

This prevents duplication, reduces bugs, and makes future changes trivial.

---

### Readability Over Cleverness
Winning logic is written to be **explicit and self-documenting**, favoring clarity over overly compact expressions.

```python
(user_choice == ROCK and computer_choice == SCISSORS)
```

This prioritizes maintainability and code review friendliness.

---

## ▶️ How to Run

### Prerequisites
- Python 3.x installed

### Run the Game
```bash
python main.py
```

---

## 🧪 Example Gameplay

```text
Rock, paper, or scissors? (r/p/s): r

You chose 🪨
Computer chose ✂️
You win!

Continue? (y/n): n
```
