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

- [x] **Describe the game's purpose.**

  It's a number-guessing game built with Streamlit. The app picks a secret number within a range that depends on the chosen difficulty (Easy 1–20, Normal 1–100, Hard 1–50). The player types guesses, gets "higher/lower" hints, earns or loses points based on how quickly they win, and has a limited number of attempts per difficulty.

- [x] **Detail which bugs you found.**

  - **Secret number "had commitment issues":** on even-numbered attempts the code ran `str(st.session_state.secret)`, turning the secret into a string. Comparing an `int` guess to a `str` secret raised `TypeError: '<' not supported between instances of 'int' and 'str'`.
  - **Hints lied:** `check_guess` returned a `(outcome, message)` tuple, but the tests and display layer expected a single outcome string, so the higher/lower hints were wrong/unreliable.
  - **Difficulty did nothing:** `get_range_for_difficulty` was an unimplemented stub (`NotImplementedError`), so the range stayed 1–100 no matter what difficulty was selected.
  - **Float guesses rejected:** `parse_guess` used `int(raw)`, which throws on "3.5", so valid-looking decimal input was rejected as "not a number." It also accepted negative numbers.
  - **Score glitch:** in `update_score`, a "Too High" wrong guess *added* 5 points on even attempts (a hidden `attempt_number % 2 == 0` trick) instead of penalizing it like "Too Low."

- [x] **Explain what fixes you applied.**

  - Refactored the game logic out of `app.py` into `logic_utils.py` (`check_guess`, `parse_guess`, `get_range_for_difficulty`, `update_score`) and added a `conftest.py` so pytest could import the module.
  - Removed the `str(secret)` conversion so the secret stays an `int`; made `check_guess` return only the outcome string (`"Win"/"Too High"/"Too Low"`) and moved the emoji messages into a `MESSAGES` dict in `app.py`.
  - Implemented `get_range_for_difficulty` for Easy/Normal/Hard.
  - Rewrote `parse_guess` to use `int(float(raw))`, catch `(ValueError, TypeError)`, and reject negatives/out-of-range input.
  - Made `update_score` penalize "Too High" and "Too Low" symmetrically (flat −5), removing the parity trick.
  - Wrote pytest tests covering each function, including a regression test that fails against the old score glitch.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and open the app in the browser.
2. Pick a difficulty in the sidebar and confirm the range updates correctly (e.g. Easy shows 1–20).
3. Enter a guess and submit — the secret number now stays the same across submits, and the higher/lower hint points in the correct direction.
4. Make a wrong guess and watch the score drop by 5 regardless of whether it was too high or too low (the old "free points on even attempts" glitch is gone).
5. Guess the secret to win — balloons appear, the win bonus is added (at least 10 points), and the game shows the final score.
6. Run `pytest` from the starter directory and confirm all tests pass.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
![Alt text](Jason_Project1_WinningGame.png?raw=true "Jason M, Winning Game Image")

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/Jason/Documents/Repos/codepath_AI110/project1/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 15 items                                                                                                                                                                                                             
tests/test_game_logic.py ...............    
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
