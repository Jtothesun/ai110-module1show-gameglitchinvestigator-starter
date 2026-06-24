

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 50

def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    try:
        value = int(float(raw))

        if value < 0:
            #raise ValueError("Guess must be non-negative.")
            return False, None, "Guess must be non-negative."
    except Exception:
        return False, None, "That is not a number."
  
    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    elif guess < secret:
        return "Too Low"
    else:
        return "Too High"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        return current_score + max(points, 10)

    if outcome == "Too High" or outcome == "Too Low": #FIX: Refactored bug of rewarding wrong guesses on even attempts
        return current_score - 5

    return current_score

