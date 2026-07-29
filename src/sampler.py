import pandas as pd


def create_history_sample(
    resumo_jogadores,
    historico,
    top_players=30,
    bottom_players=30,
    random_players=40,
):
    """Reduz o historico completo a uma amostra representativa por experimento:
    os que chegaram mais longe (top), os que faliram mais rapido (bottom) e
    um grupo aleatorio para dar volume sem explodir o tamanho do CSV.
    """
    df_resumo = pd.DataFrame(resumo_jogadores)
    df_historico = pd.DataFrame(historico)

    historico_amostra = []

    # Processa os experimentos
    for experimento in df_resumo["experimento"].unique():

        resumo_exp = df_resumo[df_resumo["experimento"] == experimento]

        # Top maiores bancas
        top = resumo_exp.nlargest(top_players, "maior_banca")

        # Piores bancas finais
        bottom = resumo_exp.nsmallest(bottom_players, "banca_final")

        # Aleatórios
        random_sample = resumo_exp.sample(
            n=min(random_players, len(resumo_exp)),
            random_state=42
        )

        # Junta removendo duplicados
        jogadores = pd.concat([
            top,
            bottom,
            random_sample
        ])["jogador"].drop_duplicates()

        # Filtra o histórico apenas desses jogadores DENTRO deste experimento.
        # O "jogador" sozinho não basta: os IDs recomeçam em 1 a cada
        # experimento, então sem o filtro por "experimento" a amostra de um
        # experimento vaza dados de outro (mesmo jogador = pessoas diferentes).
        historico_exp = df_historico[
            (df_historico["experimento"] == experimento)
            & (df_historico["jogador"].isin(jogadores))
        ]

        historico_amostra.append(historico_exp)

    return pd.concat(historico_amostra, ignore_index=True)


def create_round_summary(historico):
    """Agrega o histórico rodada a rodada por experimento: quantos jogadores
    ainda estão ativos, quantos já faliram e como o saldo está distribuído.
    """
    df = pd.DataFrame(historico)

    round_summaries = []

    # Processa cada experimento separadamente
    for experimento in df["experimento"].unique():

        df_exp = df[df["experimento"] == experimento]

        # Linhas = rodadas
        # Colunas = jogadores
        # Valores = saldo após cada rodada
        pivot_df = df_exp.pivot_table(
            index="rodada",
            columns="jogador",
            values="saldo_final"
        )

        total_jogadores = pivot_df.shape[1]

        # Mantém o último saldo conhecido do jogador e considera 0 para
        # quem já faliu (saldo_final chega a exatamente 0 na falência)
        pivot_df = pivot_df.ffill().fillna(0)

        # Contagem de jogadores que efetivamente apostaram naquela rodada
        # (alinhada explicitamente ao índice do pivot, em vez de depender
        # da ordem do groupby coincidir com a do pivot_table)
        jogadores_ativos = (
            df_exp.groupby("rodada")["jogador"]
            .nunique()
            .reindex(pivot_df.index)
        )

        jogadores_falidos = (pivot_df == 0).sum(axis=1)

        summary = pd.DataFrame({
            "experimento": experimento,
            "rodada": pivot_df.index,
            "jogadores_ativos": jogadores_ativos.values,
            "jogadores_falidos": jogadores_falidos.values,
            "percentual_falidos": (
                jogadores_falidos / total_jogadores * 100
            ).values,
            "saldo_medio": pivot_df.mean(axis=1).values,
            "saldo_mediano": pivot_df.median(axis=1).values,
            "saldo_maximo": pivot_df.max(axis=1).values,
            "saldo_minimo": pivot_df.min(axis=1).values,
            "desvio_padrao": pivot_df.std(axis=1).values,
        })

        round_summaries.append(summary)

    return pd.concat(round_summaries, ignore_index=True)