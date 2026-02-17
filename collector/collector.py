import sqlite3
import psutil
from ping3 import ping
import time
from datetime import datetime, timezone
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "metrics.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            latency REAL,
            bytes_sent INTEGER,
            bytes_received INTEGER
        )
    """)
    conn.commit()
    conn.close()

def collect_metrics():
    latency = ping("8.8.8.8")  # Google DNS

    net = psutil.net_io_counters()
    bytes_sent = net.bytes_sent
    bytes_received = net.bytes_recv

    return latency, bytes_sent, bytes_received

def save_metrics(latency, bytes_sent, bytes_received):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO metrics (timestamp, latency, bytes_sent, bytes_received)
        VALUES (?, ?, ?, ?)
    """, (
        datetime.now(timezone.utc).isoformat(),
        latency,
        bytes_sent,
        bytes_received
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    for _ in range(10):  # run 10 times
        latency, sent, received = collect_metrics()
        save_metrics(latency, sent, received)
        print("Saved:", latency)
        time.sleep(5)

