import random
from strategies import fixed_bet, martingale,fibonacci,dalembert

STRATEGIES = {
    "Fixed Bet": fixed_bet.get_bet,
    "Martingale": martingale.get_bet,
    "Fibonacci": fibonacci.get_bet,
    "D'Alembert": dalembert.get_bet,
}
 

VERMELHOS = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
}


def run_simulation(config):

    experimentos = [{
        "experimento": config.experiment_id,
        "jogadores": config.players,
        "banca_inicial": config.initial_bank,
        "valor_aposta": config.bet,
        "estrategia": config.strategy,
        "roleta": config.roulette
    }]

    resumo_jogadores = []
    historico = []

    get_bet = STRATEGIES[config.strategy]

    for jogador in range(1, config.players + 1):

        current_bet = config.bet
        won = True 
        saldo = config.initial_bank
        maior_banca = saldo
        rodada = 0

        while saldo > 0:

            if config.max_rounds is not None and rodada >= config.max_rounds:
                break

            state = {
                "initial_bet": config.bet,
                "current_bet": current_bet,
                "won": won,
            }

            aposta_desejada = get_bet(state)

            # Se a banca não cobre o valor pedido pela estratégia, 
            # o jogador vai all-in com o que sobrou 
            bet = min(aposta_desejada, saldo)

            saldo_antes = saldo

            numero = random.randint(0, 36)

            if numero == 0:
                cor = "Verde"
            elif numero in VERMELHOS:
                cor = "Vermelho"
            else:
                cor = "Preto"

            ganhou = cor == "Vermelho"

            if ganhou:
                saldo += bet
                variacao = bet
            else:
                saldo -= bet
                variacao = -bet

            saldo_depois = saldo

            rodada += 1
            maior_banca = max(maior_banca, saldo)

            historico.append({
                "experimento": config.experiment_id,
                "jogador": f"{config.experiment_id}_{jogador}",
                "rodada": rodada,
                "numero": numero,
                "cor": cor,
                "resultado": "Vitória" if ganhou else "Derrota",
                "valor_aposta": bet,
                "variacao": variacao,
                "saldo_inicial": saldo_antes,
                "saldo_final": saldo_depois
            })

            current_bet = bet
            won = ganhou

        resumo_jogadores.append({
            "experimento": config.experiment_id,
            "jogador": f"{config.experiment_id}_{jogador}",
            "tempo_sobrevivencia": rodada,
            "banca_inicial": config.initial_bank,
            "banca_final": saldo,
            "maior_banca": maior_banca,
            "falencia": saldo <= 0
        })

    return experimentos, resumo_jogadores, historico