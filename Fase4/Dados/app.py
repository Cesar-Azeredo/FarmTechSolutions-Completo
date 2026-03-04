from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from ml_pipeline import run_regression_pipeline, suggest_management_actions


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "farmtech.db"


@st.cache_data
def load_database_views(db_path: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    with sqlite3.connect(db_path) as conn:
        sensor_df = pd.read_sql_query("SELECT * FROM sensor_readings", conn)
        pred_df = pd.read_sql_query("SELECT * FROM predictions", conn)
        try:
            iot_df = pd.read_sql_query("SELECT * FROM iot_weather_logs", conn)
        except Exception:
            iot_df = pd.DataFrame()

    return sensor_df, pred_df, iot_df


st.set_page_config(page_title="FarmTech Fase4 - Previsão Inteligente", layout="wide")
st.title("🌾 FarmTech Solutions - Fase 4")
st.subheader("Assistente Agrícola Inteligente (Regressão + Dashboard Interativo)")

with st.sidebar:
    st.header("Controles")
    if st.button("Treinar/Reavaliar modelos"):
        st.cache_data.clear()
        st.cache_resource.clear()


sensor_df, pred_df, iot_df = load_database_views(DB_PATH)
artifacts = run_regression_pipeline()

joined = sensor_df.merge(pred_df, left_on="id", right_on="reading_id", how="inner")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Leituras IoT", len(sensor_df))
col2.metric("Previsões registradas", len(pred_df))
col3.metric("Ações de irrigação estimadas", int(pred_df["volume_irrigacao"].gt(0).sum()))
col4.metric("Melhor modelo", artifacts.best_model_name)

st.markdown("---")

st.header("1) Métricas dos modelos de regressão")
st.dataframe(artifacts.results, use_container_width=True)

best_pred = artifacts.best_model.predict(artifacts.X_test)
mae = mean_absolute_error(artifacts.y_test, best_pred)
mse = mean_squared_error(artifacts.y_test, best_pred)
rmse = mse ** 0.5
r2 = r2_score(artifacts.y_test, best_pred)

m1, m2, m3, m4 = st.columns(4)
m1.metric("MAE", f"{mae:,.2f}")
m2.metric("MSE", f"{mse:,.2f}")
m3.metric("RMSE", f"{rmse:,.2f}")
m4.metric("R²", f"{r2:.4f}")

st.markdown("---")

st.header("2) Correlações e tendências")
numeric_cols = [
    "temperatura",
    "umidade_solo",
    "ph_solo",
    "nitrogenio",
    "fosforo",
    "potassio",
    "volume_irrigacao",
    "rendimento_estimado",
]

corr = joined[numeric_cols].corr(numeric_only=True)
fig_corr = px.imshow(corr, text_auto=True, aspect="auto", title="Matriz de Correlação")
st.plotly_chart(fig_corr, use_container_width=True)

fig_trend = px.scatter(
    joined,
    x="umidade_solo",
    y="rendimento_estimado",
    color="cultura",
    trendline="ols",
    title="Tendência: Umidade do Solo x Rendimento Estimado",
)
st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("---")

st.header("3) Previsão interativa e recomendação de manejo")

c1, c2, c3 = st.columns(3)
with c1:
    temperatura = st.number_input("Temperatura (°C)", min_value=0.0, max_value=50.0, value=25.0)
    umidade = st.number_input("Umidade do solo (%)", min_value=0.0, max_value=100.0, value=55.0)
    ph = st.number_input("pH do solo", min_value=3.0, max_value=9.0, value=6.3)
with c2:
    nitrogenio = st.selectbox("Nitrogênio adequado?", [0, 1], index=1)
    fosforo = st.selectbox("Fósforo adequado?", [0, 1], index=1)
    potassio = st.selectbox("Potássio adequado?", [0, 1], index=1)
with c3:
    irrigacao_ativa = st.selectbox("Irrigação ativa?", [0, 1], index=0)
    cultura = st.selectbox("Cultura", sorted(sensor_df["cultura"].dropna().unique().tolist()))
    volume_irrigacao = st.number_input("Volume de irrigação previsto (L/m²)", min_value=0.0, max_value=20.0, value=3.0)

if st.button("Gerar previsão de rendimento"):
    input_df = pd.DataFrame(
        [
            {
                "temperatura": temperatura,
                "umidade_solo": umidade,
                "ph_solo": ph,
                "nitrogenio": nitrogenio,
                "fosforo": fosforo,
                "potassio": potassio,
                "irrigacao_ativa": irrigacao_ativa,
                "cultura": cultura,
                "volume_irrigacao": volume_irrigacao,
            }
        ]
    )

    pred = float(artifacts.best_model.predict(input_df)[0])
    st.success(f"Rendimento estimado: {pred:,.2f}")

    actions = suggest_management_actions(umidade, ph, pred)
    st.markdown("**Recomendações de manejo:**")
    for action in actions:
        st.write(f"- {action}")

st.markdown("---")

st.header("4) Integração IoT → Banco de Dados")
if iot_df.empty:
    st.info("Tabela iot_weather_logs ainda não disponível. Execute: `python iot_ingestion.py` em Fase4/Dados.")
else:
    st.dataframe(iot_df.sort_values("timestamp", ascending=False), use_container_width=True)
    fig_rain = px.line(iot_df.sort_values("timestamp"), x="timestamp", y="rain_probability", title="Probabilidade de chuva (logs IoT)")
    st.plotly_chart(fig_rain, use_container_width=True)
