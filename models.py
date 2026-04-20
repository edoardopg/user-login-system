from database import get_connection
import bcrypt

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT,
                failed_attempts INTEGER DEFAULT 0,
                block INTEGER DEFAULT 0,
                token_reset TEXT,
                token_expires TEXT
                )
                ''')
    conn.commit()
    conn.close()

def create_admin():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) FROM users''')
    count = cursor.fetchone()[0]
    if count == 0:
        hashed = bcrypt.hashpw("admin123".encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        cursor.execute('''INSERT INTO users (username,email,password) VALUES (?,?,?)''',("admin","admin@admin.com",hashed))
        conn.commit()
    conn.close()