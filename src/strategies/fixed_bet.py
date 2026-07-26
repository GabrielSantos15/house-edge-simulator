def get_bet(state: dict) -> int:
    """Aposta sempre o valor base, independentemente do resultado anterior."""
    return state["initial_bet"]