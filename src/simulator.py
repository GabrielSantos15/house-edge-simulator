import random

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

    for jogador in range(1, config.players + 1):

        saldo = config.initial_bank
        maior_banca = saldo
        rodada = 0

        while saldo >= config.bet:

            if config.max_rounds is not None and rodada >= config.max_rounds:
                break

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
                saldo += config.bet
                variacao = config.bet
            else:
                saldo -= config.bet
                variacao = -config.bet

            saldo_depois = saldo

            rodada += 1
            maior_banca = max(maior_banca, saldo)

            historico.append({
                "experimento": config.experiment_id,
                "jogador": jogador,
                "rodada": rodada,
                "numero": numero,
                "cor": cor,
                "resultado": "Vitória" if ganhou else "Derrota",
                "valor_aposta": config.bet,
                "variacao": variacao,
                "saldo_inicial": saldo_antes,
                "saldo_final": saldo_depois
            })

        resumo_jogadores.append({
            "experimento": config.experiment_id,
            "jogador": jogador,
            "tempo_sobrevivencia": rodada,
            "banca_inicial": config.initial_bank,
            "banca_final": saldo,
            "maior_banca": maior_banca,
            "falencia": saldo < config.bet
        })

    return experimentos, resumo_jogadores, historico