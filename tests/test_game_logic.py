from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_on_even_attempt_does_not_add_points():
    # THE BUG: the old code did `current_score + 5` when attempt_number was
    # even. A wrong guess must never increase the score. This is the
    # regression test that fails against the glitched version.
    assert update_score(100, "Too High", 2) == 95

def test_too_high_on_odd_attempt_subtracts_points():
    assert update_score(100, "Too High", 3) == 95

def test_too_low_subtracts_points():
    assert update_score(100, "Too Low", 2) == 95

def test_wrong_guesses_are_symmetric():
    # "Too High" and "Too Low" are both wrong guesses and must be penalized
    # identically, regardless of attempt parity.
    for attempt in (1, 2, 3, 4):
        assert (
            update_score(100, "Too High", attempt)
            == update_score(100, "Too Low", attempt)
        )
