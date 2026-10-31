
import sqlite3
from datetime import datetime

DB_NAME = "tech_assistant.db"

def initialize_memory():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            memory TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_memory(user_id, memory):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memories
        (user_id, memory, created_at)
        VALUES (?, ?, ?)
    """, (
        user_id,
        memory,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_memories(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, memory, created_at
        FROM memories
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "memory": row[1],
            "created_at": row[2]
        }
        for row in rows
    ]


def delete_memory(user_id, memory_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM memories
        WHERE user_id = ? AND id = ?
    """, (user_id, memory_id))

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted > 0


def delete_all_memories(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM memories WHERE user_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()
  
