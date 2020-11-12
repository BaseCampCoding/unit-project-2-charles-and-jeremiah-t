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

    def application(self, data):
        i want this function to retrun the print statement basically
        
        return ...
        
