def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIXME: Logic breaks here --> guess and secret aren't defined as int or str
# check_guess moved to logic_utils.py

def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    Both values are coerced to int so comparisons are always numeric,
    regardless of whether guess/secret arrive as int or str.
    """
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

#FIXED: Refactored check_guess from app.py into logic_utils.py, added int typecasting to ensure numeric comparison regardless of input type.

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def reset_game_state(low: int, high: int, secret=None):
    """
    Return the fresh game state for a brand-new game.

    A proper reset clears EVERY piece of game state so a previous win/loss,
    score, or guess history can't leak into the new round. Pass ``secret`` to
    inject a deterministic value in tests; otherwise a random one in
    [low, high] is chosen.

    Returns a dict with: secret, attempts, score, status, history.
    """
    import random

    if secret is None:
        secret = random.randint(low, high)

    return {
        "secret": secret,
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "history": [],
    }
