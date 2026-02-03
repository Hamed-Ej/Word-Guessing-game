# Word Guessing Game (Python)

A simple terminal-based word guessing game written in Python. The player tries to guess a randomly chosen word, one character at a time, with a limited number of guesses.

## Features
- Random word selection from a predefined list
- 12 total guesses
- Displays correctly guessed letters and remaining blanks
- Friendly terminal prompts

## Requirements
- Python 3.8+

## How to Run
1. Open a terminal in the project directory.
2. Run the game:

```bash
python app.py
```

## How to Play
- The game picks a random word.
- Enter one character per guess.
- Correct guesses reveal letters in the word.
- Incorrect guesses reduce the remaining attempts.
- Win by revealing the entire word before guesses run out.

## Project Structure
```
.
├── app.py
└── README.md
```

## Notes
- Words are defined in `app.py` in the `WORDS` list.
- You can add or remove words there to change the game’s vocabulary.

## License
MIT
