import pandas as pd
from sklearn.ensemble import IsolationForest

def detectar_anomalias(df):
    modelo = IsolationForest(contamination=0.01, random_state=42)
    df["anomalia"] = modelo.fit_predict(df[["valor"]])
    return df
