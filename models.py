import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "database" / "vehicle_service.db"


def init_db():
    connection = sqlite3.connect(DB_PATH)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            vehicle_type TEXT NOT NULL,
            service_type TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            notes TEXT
        )
        """
    )
    connection.commit()
    connection.close()
