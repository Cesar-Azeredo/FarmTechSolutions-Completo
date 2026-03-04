from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DB_PATH = Path(__file__).resolve().parent / "database" / "farmtech.db"


@dataclass
class PipelineArtifacts:
    best_model_name: str
    best_model: Pipeline
    results: pd.DataFrame
    X_test: pd.DataFrame
    y_test: pd.Series


def load_training_dataframe(db_path: Path = DB_PATH) -> pd.DataFrame:
    query = """
        SELECT
            s.id,
            s.temperatura,
            s.umidade_solo,
            s.ph_solo,
            s.nitrogenio,
            s.fosforo,
            s.potassio,
            s.irrigacao_ativa,
            s.cultura,
            p.volume_irrigacao,
            p.rendimento_estimado
        FROM sensor_readings s
        INNER JOIN predictions p ON p.reading_id = s.id
    """

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)

    df = df.dropna(subset=["rendimento_estimado"]).reset_index(drop=True)
    return df


def _build_preprocessor() -> ColumnTransformer:
    numeric_features = [
        "temperatura",
        "umidade_solo",
        "ph_solo",
        "nitrogenio",
        "fosforo",
        "potassio",
        "irrigacao_ativa",
        "volume_irrigacao",
    ]
    categorical_features = ["cultura"]

    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )


def run_regression_pipeline(random_state: int = 42) -> PipelineArtifacts:
    df = load_training_dataframe()

    X = df[
        [
            "temperatura",
            "umidade_solo",
            "ph_solo",
            "nitrogenio",
            "fosforo",
            "potassio",
            "irrigacao_ativa",
            "cultura",
            "volume_irrigacao",
        ]
    ]
    y = df["rendimento_estimado"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=random_state
    )

    preprocessor = _build_preprocessor()

    models: Dict[str, object] = {
        "LinearRegression": LinearRegression(),
        "RandomForestRegressor": RandomForestRegressor(
            n_estimators=300, random_state=random_state
        ),
        "GradientBoostingRegressor": GradientBoostingRegressor(random_state=random_state),
    }

    rows = []
    trained: Dict[str, Pipeline] = {}

    for name, model in models.items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        rows.append(
            {
                "model": name,
                "MAE": mae,
                "MSE": mse,
                "RMSE": rmse,
                "R2": r2,
            }
        )
        trained[name] = pipeline

    results = pd.DataFrame(rows).sort_values("R2", ascending=False).reset_index(drop=True)
    best_model_name = results.iloc[0]["model"]

    return PipelineArtifacts(
        best_model_name=best_model_name,
        best_model=trained[best_model_name],
        results=results,
        X_test=X_test,
        y_test=y_test,
    )


def suggest_management_actions(
    umidade_solo: float,
    ph_solo: float,
    rendimento_previsto: float,
) -> list[str]:
    actions = []

    if umidade_solo < 40:
        actions.append("Aumentar irrigação nas próximas 24h (solo seco).")
    elif umidade_solo > 75:
        actions.append("Reduzir irrigação e monitorar encharcamento.")
    else:
        actions.append("Manter plano atual de irrigação.")

    if ph_solo < 5.8:
        actions.append("Aplicar corretivo para elevar o pH do solo.")
    elif ph_solo > 7.2:
        actions.append("Avaliar manejo para reduzir alcalinidade do solo.")
    else:
        actions.append("pH em faixa adequada para produtividade.")

    if rendimento_previsto < 9000:
        actions.append("Priorizar adubação e revisão do manejo nutricional.")
    elif rendimento_previsto < 15000:
        actions.append("Ajustar fertilização de forma moderada para ganho de rendimento.")
    else:
        actions.append("Rendimento previsto alto: manter estratégia atual e monitorar estabilidade.")

    return actions


if __name__ == "__main__":
    artifacts = run_regression_pipeline()
    print("Melhor modelo:", artifacts.best_model_name)
    print("\nMétricas:")
    print(artifacts.results.to_string(index=False))
