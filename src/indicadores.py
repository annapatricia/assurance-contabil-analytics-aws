import pandas as pd

def calcular_indicadores(df):
    indicadores = {}

    indicadores["total_lancamentos"] = len(df)
    indicadores["percentual_manual"] = (
        df[df["tipo_lancamento"] == "MANUAL"].shape[0] / len(df)
    )

    indicadores["valor_medio"] = df["valor"].mean()

    return indicadores
