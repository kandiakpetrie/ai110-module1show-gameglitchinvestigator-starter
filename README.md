# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
1) The game's purpose was for the user to guess the secret number by entering their guesses into the game. The game would then hint to the user if their guesses were too high or too low. The game then ends with the user guessing the secret number or running out of attempts. 
- [ ] Detail which bugs you found.
1) In the logic behind the hints that told the user about if their current guess were too high or too low, the messages were mixed up and actually programmed backwards so if the guess was actually too high the program would output "Too Low" and vice versa. 
2) The second bug I found was that when a user lost their game and wanted to start a new game, they wouldn't be prompted to, and instead was stuck on the last message of losing their game. In the program it was found that st.stop was called preventing the game from resetting and starting again.
- [ ] Explain what fixes you applied.
1) So upon futher investigation of the too low/too high hint bug, it was found that the bug was due to the program comparing the inputed guesses as strings rather than integers, causing the hints to be reversed. So I changed the input and the secret number to get type casted as integers when being compared. 
2) When looking into the game reset bug, it showed that the program only reset the attempts and the secret, keeping the points from the previous game and the previous guesses. So, with the help of Claude, the reset_game_state() was added into logic_utils.py and wired into the app. This method would reset the game to it's starting settings, clearing the score and history while resetting the secret number, the attempts, and the status. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user enters a guess of 75
2. The game returns "Too High" or "Go LOWER!"
3. The user enters another guess of 15 
4. The game returns "Too Low" or "Go HIGHER!"
5. The scores updates with each guess the user makes
6. This process repeats until the user guess is the secret number or until the user runs out of guesses
7. The game ends and prompts the user with the option of starting a new game

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
============================== X passed in 0.00s ==============================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
