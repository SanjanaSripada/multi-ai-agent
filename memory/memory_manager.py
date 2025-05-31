import sqlite3
from datetime import datetime
import json

class MemoryManager:
    def __init__(self, db_path='database/context.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread = False)
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            type TEXT,
            timestamp TEXT,
            sender TEXT,
            intent TEXT,
            extracted_fields TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log_entry(self, source, data_type, sender, intent, extracted_fields):
        print("LOGGING")
        query = """
        INSERT INTO memory (source, type, timestamp, sender, intent, extracted_fields)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (
            source, 
            data_type, 
            datetime.now().isoformat(), 
            sender, 
            intent, 
            json.dumps(extracted_fields)
        ))
        self.conn.commit()

    def fetch_all(self):
        cursor = self.conn.execute("SELECT * FROM memory")
        return [
            {
                "id": row[0],
                "source": row[1],
                "type": row[2],
                "timestamp": row[3],
                "sender": row[4],
                "intent": row[5],
                "extracted_fields": json.loads(row[6])
            }
            for row in cursor.fetchall()
    ]

