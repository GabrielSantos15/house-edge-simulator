# Sequência de Fibonacci utilizada para calcular o multiplicador da aposta.
# A sequência inicia em [1, 2] em vez de [1, 1] para evitar ambiguidades
# ao identificar a posição atual da progressão.
_SEQUENCIA = [1, 2]

while len(_SEQUENCIA) < 30:
    _SEQUENCIA.append(_SEQUENCIA[-1] + _SEQUENCIA[-2])


def _indice_atual(current_bet: int, initial_bet: int) -> int:
    """
    Retorna a posição da aposta atual na sequência de Fibonacci,
    considerando a relação entre a aposta atual e a aposta inicial.
    """
    razao = round(current_bet / initial_bet)

    for indice, valor in enumerate(_SEQUENCIA):
        if valor == razao:
            return indice

    # Caso a aposta não corresponda exatamente a um valor da sequência
    # (por exemplo, devido a uma aposta all-in), reinicia a progressão.
    return 0


def get_bet(state: dict) -> int:
    """
    Estratégia Fibonacci.

    - Derrota: avança uma posição na sequência.
    - Vitória: recua duas posições na sequência.
    - A aposta é calculada multiplicando a aposta inicial pelo valor
      correspondente da sequência de Fibonacci.
    """
    initial_bet = state["initial_bet"]
    current_bet = state["current_bet"]
    won = state["won"]

    indice = _indice_atual(current_bet, initial_bet)

    if won:
        indice = max(indice - 2, 0)
    else:
        indice = min(indice + 1, len(_SEQUENCIA) - 1)

    return initial_bet * _SEQUENCIA[indice]