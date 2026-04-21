from database import get_connection

class Users:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
    def register(self,username,email,password):
        self.cursor.execute('''INSERT INTO users (username,email,password) VALUES (?,?,?)''', (username,email,password))
        self.conn.commit()
    def find_by_username(self,username):
        self.cursor.execute('''SELECT * FROM users WHERE username=?''',(username,))
        return self.cursor.fetchone()
    def find_by_email(self,email):
        self.cursor.execute('''SELECT * FROM users WHERE email=?''',(email,))
        return self.cursor.fetchone()
    def increment_attempts(self,username):
        self.cursor.execute('''UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?''', (username,))
        self.conn.commit()
    def reset_attempts(self,username):
        self.cursor.execute('''UPDATE users SET failed_attempts = 0 WHERE username=?''',(username,))
        self.conn.commit()
    def block_user(self,username):
        self.cursor.execute('''UPDATE users SET block = 1 WHERE username=?''',(username,))
        self.conn.commit()
    def unblock_user(self,username):
        self.cursor.execute('''UPDATE users SET block = 0 WHERE username=?''',(username,))
        self.conn.commit()
    def update_password(self,email,new_password):
        self.cursor.execute('''UPDATE users SET password=?, token_reset=NULL, token_expires=NULL WHERE email=?''',(new_password,email))
        self.conn.commit()
    def save_reset_token(self,email,token,expires_at):
        self.cursor.execute('''UPDATE users SET token_reset=?,token_expires=? WHERE email=?''',(token,expires_at,email))
        self.conn.commit()
    def find_by_token(self,token):
        self.cursor.execute('''SELECT * FROM users WHERE token_reset=?''',(token,))
        return self.cursor.fetchone()
    def delete_account(self,username):
        self.cursor.execute('''DELETE FROM users WHERE username=?''',(username,))
        self.conn.commit()