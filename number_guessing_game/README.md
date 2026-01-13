# 🔢 Number Guessing Game

A fun and interactive command-line number guessing game where you try to guess a randomly selected number between 1 and 100 within limited attempts. Choose your difficulty level, use hints when stuck, and try to beat your high scores!

## ✨ Features

### 🎮 Core Gameplay
- **Random Number Generation**: Computer selects a random number between 1-100
- **Multiple Difficulty Levels**: 
  - Easy: 10 chances
  - Medium: 5 chances
  - Hard: 3 chances
- **Smart Feedback**: Tells you if your guess is too high or too low
- **Win/Loss Conditions**: Win by guessing correctly, lose by running out of chances

### 🚀 Enhanced Features
- **Multiple Rounds**: Play as many games as you want
- **Timer System**: See how fast you can guess the number
- **Hint System**: Get helpful clues when you're stuck
  - Even/Odd hints
  - Range-based hints
- **High Score Tracking**: Best attempts saved for each difficulty level
- **Game Statistics**: Track your win rate and total rounds played

### 🎯 User Experience
- Clean, formatted command-line interface
- Input validation to prevent errors
- Visual feedback with emojis
- Progress tracking during gameplay

## 📋 Prerequisites

- Python 3.6 or higher
- No additional packages required (uses only Python standard library)

## 🚀 Installation & Setup

### Method 1: Direct Download
```bash
# Clone or download the repository
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game

# Run the game
python guessing_game.py
```

### Method 2: Manual Setup
1. Create a new Python file:
```bash
touch guessing_game.py
```

2. Copy the game code into the file (from the provided Python script)

3. Run the game:
```bash
python guessing_game.py
```

## 🎮 How to Play

### Starting the Game
```
==================================================
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
==================================================

Rules:
1. I'll pick a random number between 1 and 100.
2. You need to guess the number within limited chances.
3. After each wrong guess, I'll tell you if the number is higher or lower.
4. Try to guess in as few attempts as possible!
```

### Choosing Difficulty
```
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2

Great! You have selected the Medium difficulty level.
You have 5 chances to guess the number.
```

### Gameplay Example
```
==================================================
Let's start the game!
==================================================

You have 5 chances left.
Enter your guess (1-100): 50
Incorrect! The number is greater than 50.

You have 4 chances left.
Enter your guess (1-100): 75
💡 Hint: The number is less than 75.

You have 3 chances left.
Enter your guess (1-100): 63
🎉 Congratulations! You guessed the correct number in 3 attempts!
⏱️ Time taken: 15.23 seconds
🏆 New high score for Medium difficulty: 3 attempts!
```

### Game Features in Action

**Hint System:**
- After several attempts, you'll get hints like:
  - "💡 Hint: The number is even."
  - "💡 Hint: The number is less than 50."

**Statistics Display:**
```
📊 Round Statistics:
Rounds played: 3
Wins: 2
Win rate: 66.7%

==================================================
HIGH SCORES
==================================================
Easy: 4 attempts
Medium: 3 attempts
Hard: No score yet
```

## 🏆 Scoring

- Try to guess the number in as few attempts as possible
- High scores are tracked separately for each difficulty level
- Your best (lowest) attempt count is saved as your high score
- Win rate is calculated and displayed after each round

## 🎯 Tips for Winning

1. **Start with the middle**: Begin with 50 to split the range in half
2. **Use binary search**: Each guess should eliminate half the remaining possibilities
3. **Pay attention to hints**: They're strategically timed to help you
4. **Track your previous guesses**: Keep mental notes of what ranges have been eliminated
5. **Adjust strategy based on difficulty**: With fewer chances, be more aggressive in narrowing the range

## 📁 Project Structure

```
number-guessing-game/
│
├── guessing_game.py    # Main game file
├── README.md           # This documentation
└── requirements.txt    # Python dependencies (none required)
```

## 🛠️ Code Structure

The game is built as a single Python class with the following methods:

- `__init__()`: Initialize game state and settings
- `display_welcome()`: Show welcome message
- `display_rules()`: Explain game rules
- `get_difficulty()`: Get user's difficulty choice
- `provide_hint()`: Generate hints based on game state
- `play_round()`: Main game loop for a single round
- `update_high_score()`: Track best scores
- `display_high_scores()`: Show high score board
- `play_game()`: Main game controller

## 🔧 Customization

Want to tweak the game? Here are some easy modifications:

### Change Number Range
```python
# In the play_round method, change:
number = random.randint(1, 100)  # to: number = random.randint(1, 50)
```

### Adjust Difficulty Settings
```python
# In __init__ method, modify:
self.difficulty_settings = {
    '1': {'name': 'Easy', 'chances': 15},    # Increased from 10
    '2': {'name': 'Medium', 'chances': 7},   # Increased from 5
    '3': {'name': 'Hard', 'chances': 4}      # Increased from 3
}
```

### Add New Difficulty Level
```python
self.difficulty_settings = {
    '1': {'name': 'Very Easy', 'chances': 20},
    '2': {'name': 'Easy', 'chances': 10},
    '3': {'name': 'Medium', 'chances': 5},
    '4': {'name': 'Hard', 'chances': 3},
    '5': {'name': 'Impossible', 'chances': 1}
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Improvement
- Add sound effects
- Create a graphical version
- Implement multiplayer mode
- Add more hint types
- Create difficulty levels with time limits
- Implement achievement system


## 🙏 Acknowledgments

- Inspired by classic number guessing games
- Built with Python's standard library
- Thanks to all contributors and testers


### 🎲 Ready to Play?

```bash
python guessing_game.py
```

**Good luck and have fun!** 🍀
