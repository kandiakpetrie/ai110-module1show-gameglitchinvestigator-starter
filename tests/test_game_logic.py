from logic_utils import check_guess, reset_game_state


# ---------------------------------------------------------------------------
# check_guess returns a (outcome, message) tuple.
# ---------------------------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # guess 60 vs secret 50 -> Too High
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # guess 40 vs secret 50 -> Too Low
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# BUG #1: High/Low glitch.
# The original bug compared guess and secret as STRINGS. Lexicographically
# "9" > "100", so a low guess was wrongly reported as "Too High". These tests
# pin down that comparison must be NUMERIC (int-coerced) and that the hint
# direction is never reversed.
# ---------------------------------------------------------------------------

def test_low_single_digit_against_large_number_is_too_low():
    # The trap case: as strings, "9" > "100" is True. Numerically 9 < 100.
    outcome, _message = check_guess(9, 100)
    assert outcome == "Too Low"


def test_large_number_against_single_digit_is_too_high():
    outcome, _message = check_guess(100, 9)
    assert outcome == "Too High"


def test_string_inputs_are_compared_numerically():
    # Guess/secret arriving as str must still compare numerically, not lexically.
    assert check_guess("9", "100")[0] == "Too Low"
    assert check_guess("100", "9")[0] == "Too High"
    assert check_guess("50", "50")[0] == "Win"


def test_hint_message_matches_direction():
    # "Too High" must tell the player to go LOWER, and vice versa --
    # a reversed hint is the user-facing symptom of the high/low bug.
    _outcome, high_msg = check_guess(60, 50)
    assert "LOWER" in high_msg.upper()

    _outcome, low_msg = check_guess(40, 50)
    assert "HIGHER" in low_msg.upper()


# ---------------------------------------------------------------------------
# BUG #2: New Game does not reset properly.
# A fresh game must clear EVERY piece of state -- secret, attempts, score,
# status, and history -- so a previous win/loss or score can't leak in.
# ---------------------------------------------------------------------------

def test_reset_clears_all_state():
    fresh = reset_game_state(1, 100, secret=42)
    assert fresh["secret"] == 42
    assert fresh["attempts"] == 1
    assert fresh["score"] == 0
    assert fresh["status"] == "playing"
    assert fresh["history"] == []


def test_reset_returns_all_expected_keys():
    fresh = reset_game_state(1, 100)
    assert set(fresh) == {"secret", "attempts", "score", "status", "history"}


def test_reset_secret_is_within_range():
    low, high = 1, 20
    for _ in range(50):
        fresh = reset_game_state(low, high)
        assert low <= fresh["secret"] <= high


def test_reset_does_not_carry_over_previous_game():
    # Simulate the end of a finished, high-scoring game...
    ended = {
        "secret": 7,
        "attempts": 8,
        "score": 250,
        "status": "won",
        "history": [10, 20, 7],
    }
    fresh = reset_game_state(1, 100, secret=7)
    # ...none of the stale values may survive the reset.
    assert fresh["score"] != ended["score"]
    assert fresh["status"] != ended["status"]
    assert fresh["history"] != ended["history"]
    assert fresh["attempts"] != ended["attempts"]
    assert fresh["status"] == "playing"


def test_reset_history_is_a_fresh_list():
    # Each reset must hand back its own empty list, not a shared mutable one.
    first = reset_game_state(1, 100)
    first["history"].append("stale")
    second = reset_game_state(1, 100)
    assert second["history"] == []
