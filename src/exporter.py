import pandas as pd
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_PATH / "data"

DATA_PATH.mkdir(exist_ok=True)

def export_csv(experimentos, resumo, historico_amostra, round_summary):
    
    # Centraliza a configuração de exportação para o padrão brasileiro
    csv_kwargs = {
        "index": False,
        "encoding": "utf-8",
        "sep": ";",
        "decimal": ","
    }

    pd.DataFrame(experimentos).to_csv(
        DATA_PATH / "experimentos.csv",
        **csv_kwargs
    )

    pd.DataFrame(resumo).to_csv(
        DATA_PATH / "resumo_jogadores.csv",
        **csv_kwargs
    )

    pd.DataFrame(historico_amostra).to_csv(
        DATA_PATH / "historico.csv",
        **csv_kwargs
    )
    
    pd.DataFrame(round_summary).to_csv(
        DATA_PATH / "round_summary.csv",
        **csv_kwargs
    )