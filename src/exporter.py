import pandas as pd
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_PATH / "data"

DATA_PATH.mkdir(exist_ok=True)

def export_csv(experimentos, resumo, historico):
    pd.DataFrame(experimentos).to_csv(
        DATA_PATH / "experimentos.csv",
        index=False,
        encoding="utf-8"
    )

    pd.DataFrame(resumo).to_csv(
        DATA_PATH / "resumo_jogadores.csv",
        index=False,
        encoding="utf-8"
    )

    pd.DataFrame(historico).to_csv(
        DATA_PATH / "historico.csv",
        index=False,
        encoding="utf-8"
    )