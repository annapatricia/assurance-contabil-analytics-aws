import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def gerar_dados(qtd_registros=100_000):
    contas = ["1.1.01", "2.1.01", "3.1.01", "4.1.01"]
    centros_custo = ["ADM", "FIN", "OPS", "TI"]
    usuarios = ["user_a", "user_b", "user_c"]

    data_inicio = datetime(2024, 1, 1)

    dados = []

    for i in range(qtd_registros):
        dados.append({
            "data_lancamento": data_inicio + timedelta(days=random.randint(0, 365)),
            "conta_contabil": random.choice(contas),
            "tipo": random.choice(["DEBITO", "CREDITO"]),
            "valor": round(abs(np.random.normal(1000, 300)), 2),
            "centro_custo": random.choice(centros_custo),
            "usuario": random.choice(usuarios),
            "tipo_lancamento": random.choice(["MANUAL", "AUTOMATICO"])
        })

    return pd.DataFrame(dados)

if __name__ == "__main__":
    df = gerar_dados()
    df.to_csv("lancamentos_contabeis.csv", index=False)
