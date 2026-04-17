import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any

class Memory:
    def __init__(self, db_path: str = 'agent_memory.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                role TEXT,  -- 'user', 'assistant', 'tool'
                content TEXT,
                tool_call_id TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
        ''')
        conn.commit()
        conn.close()

    def new_session(self, goal: str) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sessions (goal) VALUES (?)', (goal,))
        session_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return session_id

    def add_message(self, session_id: int, role: str, content: str, tool_call_id: str = None):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO messages (session_id, role, content, tool_call_id) VALUES (?, ?, ?, ?)',
            (session_id, role, content, tool_call_id)
        )
        conn.commit()
        conn.close()

    def get_history(self, session_id: int, limit: int = 20) -> List[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT role, content, tool_call_id, timestamp FROM messages WHERE session_id = ? ORDER BY timestamp DESC LIMIT ?',
            (session_id, limit)
        )
        rows = cursor.fetchall()
        conn.close()
        return [{'role': r[0], 'content': r[1], 'tool_call_id': r[2], 'timestamp': r[3]} for r in rows[::-1]]

    def get_recent_sessions(self, limit: int = 5) -> List[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, goal, created_at FROM sessions ORDER BY created_at DESC LIMIT ?',
            (limit,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'goal': r[1], 'created_at': r[2]} for r in rows]

