import sqlite3

class UserAuthentication:
    def __init__(self):
        db = sqlite3.connect("bank.sqlite")
        self.cursor = db.cursor()

    def healthcheck(self):
        try:
            self.cursor.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False
        
    def login(self, username, password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = self.cursor.fetchone()
            return user is not None
        except sqlite3.Error:
            return False
    
    def register(self, username, password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.cursor.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False