
import sqlite3
from datetime import datetime

DB_NAME = "tech_assistant.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def save_message(session_id, role, message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chats
        (session_id, role, message, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        session_id,
        role,
        message,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()

def get_history(session_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, message, created_at
        FROM chats
        WHERE session_id = ?
        ORDER BY id ASC
    """, (session_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "role": row[0],
            "message": row[1],
            "created_at": row[2]
        }
        for row in rows
    ]

def delete_history(session_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM chats WHERE session_id = ?",
        (session_id,)
    )

    conn.commit()
    conn.close()
  
