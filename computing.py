import sqlite3

conn = sqlite3.connect('information.db')

cur = conn.cursor()



cur.execute(""" CREATE TABLE IF NOT EXISTS accountinfo(
    Username TEXT,
    Email TEXT,
    Password TEXT
)"""
)

cur.execute(""" CREATE TABLE IF NOT EXISTS passwords(
  UserID INTEGER,
  Application TEXT,
  Username TEXT,
  Email TEXT,
  Password TEXT
)"""
)



def check_user_credentials(cur, username: str):
    cur.execute('SELECT Username FROM accountinfo WHERE Username = ?', (username, ))
    rows = cur.fetchall()
    return len(rows) > 0



def check_password_credentials(cur, password: str):
    cur.execute('SELECT Password FROM accountinfo WHERE Password = ?', (password, ))
    rows = cur.fetchall()
    return len(rows) > 0
    


class Password:
    def __init__(self, application, username, email, password):
        self.application = application
        self.username = username
        self.email = email
        self.password = password

    def get_app_info(application, pin_num):
        cur.execute('SELECT * FROM passwords WHERE application = :application AND UserId = :UserId', {'application': application, 'UserID': pin_num})
        for row in cur.fetchall():
            print(row)
        
    def print_all(pin_num):
        cur.execute('SELECT * FROM passwords WHERE UserID = :UserID', {'UserID': pin_num})
        for row in cur.fetchall():
            temp = Password(row[1], row[2], row[3], row[4])
            temp.printToConsole()
    def printToConsole(self):
        print(self.application + ' ' + self.username + ' ' + self.email + ' ' + self.password)
