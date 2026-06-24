from logic_utils import (
    check_guess,
    update_score,
    get_range_for_difficulty,
    parse_guess,
)

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

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_range_unpacks_into_low_high():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_parse_valid_integer_string():
    assert parse_guess("50") == (True, 50, None)

def test_parse_float_string_truncates_to_int():
    # "3.9" -> float 3.9 -> int 3 (truncates toward zero)
    assert parse_guess("3.9") == (True, 3, None)

def test_parse_non_numeric_string():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_negative_is_rejected():
    ok, value, err = parse_guess("-5")
    assert ok is False
    assert value is None
    assert err == "Guess must be non-negative."