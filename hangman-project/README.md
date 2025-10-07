# 🎯 Hangman Game  

A classic word-guessing game built in Python as part of the **100 Days of Code – Day 7** project. The player guesses letters to uncover a hidden word before the hangman drawing is completed!

---

## ✨ Features
- 🎮 Word guessing game with limited lives  
- 🔤 Tracks and displays correct and incorrect guesses  
- 🧠 Prevents repeated guesses  
- 💀 ASCII art shows the hangman stages as lives decrease  
- ✅ Win or lose message depending on game outcome  

---

## 🚀 How to Run
1. Clone this repository or download the following files:
   - `main.py`
   - `hangman_art.py`
   - `hangman_words.py`
2. In your terminal or command prompt, run:
   ```bash
   python main.py

**🧠 Concepts Covered:**  
🔁 Loops and conditionals (`while`, `if/else`)  
🔤 String and list manipulation  
📦 Using the `random` module  
🧩 Modular code structure across multiple files  
🎨 ASCII art using lists of strings  
📜 Tracking game state (lives, guesses, word progress)  
🛑 Handling repeated inputs and user feedback  
📝 Clean function-based logic and file separation

Example:
 _                                             
| |                                            
| |__   __ _ _ __ ___   ___                    
| '_ \ / _` | '_ ` _ \ / _ \                   
| | | | (_| | | | | | |  __/                   
|_| |_|\__,_|_| |_| |_|\___|                   

Guess a letter: a
_ a _ _ _

Guess a letter: e
_ a _ _ e

Guess a letter: x
Wrong guess. You lose a life.
(ASCII art stage shown)

...

You win!

