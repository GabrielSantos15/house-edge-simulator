def get_bet(state: dict) -> int:
    """Dobra a aposta após cada derrota; volta ao valor base após uma vitória."""
    if state["won"]:
        return state["initial_bet"]
    return state["current_bet"] * 2
 