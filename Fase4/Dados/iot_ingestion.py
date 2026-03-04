from __future__ import annotations

import json
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "farmtech.db"
LOG_PATH = BASE_DIR / "logs_irrigacao_api.json"


def ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS iot_weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL UNIQUE,
            rain_probability REAL,
            description TEXT,
            predicted_temperature REAL,
            decision TEXT,
            reason TEXT
        )
        """
    )


def ingest_logs() -> int:
    if not LOG_PATH.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {LOG_PATH}")

    entries = json.loads(LOG_PATH.read_text(encoding="utf-8"))
    inserted = 0

    with sqlite3.connect(DB_PATH) as conn:
        ensure_table(conn)

        for item in entries:
            previsao = item.get("previsao", {})
            values = (
                item.get("timestamp"),
                previsao.get("probabilidade"),
                previsao.get("descricao"),
                previsao.get("temperatura"),
                item.get("decisao"),
                item.get("motivo"),
            )

            cursor = conn.execute(
                """
                INSERT OR IGNORE INTO iot_weather_logs (
                    timestamp,
                    rain_probability,
                    description,
                    predicted_temperature,
                    decision,
                    reason
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                values,
            )
            if cursor.rowcount > 0:
                inserted += 1

    return inserted


if __name__ == "__main__":
    count = ingest_logs()
    print(f"Registros IoT inseridos: {count}")
