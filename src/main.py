from config import (
    configs,
    analysis_config
)

import simulator
import exporter
import sampler

def main():
    experimentos = []
    resumos = []
    historico_completo = []

    for config in configs:
        e, r, h = simulator.run_simulation(config)

        experimentos.extend(e)
        resumos.extend(r)
        historico_completo.extend(h)

    historico_amostra = sampler.create_history_sample(
        resumo_jogadores=resumos,
        historico=historico_completo,
        top_players=analysis_config.top_players,
        bottom_players=analysis_config.bottom_players,
        random_players=analysis_config.random_players
    )

    round_summary = sampler.create_round_summary(
        historico=historico_completo
    )

    exporter.export_csv(
        experimentos,
        resumos,
        historico_amostra,
        round_summary
    )

    print("Arquivos gerados com sucesso!")


if __name__ == "__main__":
    main()