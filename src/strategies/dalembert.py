def get_bet(state: dict) -> int:
    """
    Estratégia D'Alembert.

    - Vitória: reduz a aposta em uma unidade.
    - Derrota: aumenta a aposta em uma unidade.
    - A aposta nunca fica abaixo do valor inicial.
    """
    initial_bet = state["initial_bet"]
    current_bet = state["current_bet"]
    won = state["won"]

    unidade = initial_bet
    proxima_aposta = current_bet

    if won:
        proxima_aposta -= unidade
    else:
        proxima_aposta += unidade

    return max(proxima_aposta, initial_bet)