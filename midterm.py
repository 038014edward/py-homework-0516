import os
import pack.modu as lib
import sqlite3


# 檢查 library.db 是否存在
if not os.path.isfile("library.db"):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
    )
