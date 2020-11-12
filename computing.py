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
    

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Password:
    def __init__(self, application, username, email, password):
        self.application = application
        self.username = username
        self.email = email
        self.password = password

    # def update_application(data):
    #     c.execute('''SELECT * FROM passwords''')
    #                 for row in c.fetchall():
    #                     data = f'Appliction: {row[0]} \n Username: {row[1]} \n Email: {row[2]} \n Password: {row[3]}'

    def get_app_info(application, username):
        cur.execute('SELECT * FROM passwords WHERE application = :application AND username = :username', {'application': application, 'username': username})
        for row in cur.fetchall():
            print(row)
        
