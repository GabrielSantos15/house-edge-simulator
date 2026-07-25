from dataclasses import dataclass
import pandas as pd
import random
from pathlib import Path

# ===========================
# CAMINHOS
# ===========================

ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_PATH / "data"

DATA_PATH.mkdir(exist_ok=True)

# ===========================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ===========================

@dataclass
class SimulationConfig:
    experiment_id: int
    players: int
    initial_bank: int
    bet: int
    strategy: str
    roulette: str
    max_rounds: int | None = None


config = SimulationConfig(
    experiment_id=1,
    players=100,
    initial_bank=100,
    bet=5,
    strategy="Fixed Bet",
    roulette="European"
)

VERMELHOS = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
}


# ===========================
# DATASETS
# ===========================

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


# ===========================
# SIMULAÇÃO
# ===========================

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


# ===========================
# EXPORTAÇÃO
# ===========================

pd.DataFrame(experimentos).to_csv(
    DATA_PATH / "experimentos.csv",
    index=False,
    encoding="utf-8"
)

pd.DataFrame(resumo_jogadores).to_csv(
    DATA_PATH / "resumo_jogadores.csv",
    index=False,
    encoding="utf-8"
)

pd.DataFrame(historico).to_csv(
    DATA_PATH / "historico.csv",
    index=False,
    encoding="utf-8"
)