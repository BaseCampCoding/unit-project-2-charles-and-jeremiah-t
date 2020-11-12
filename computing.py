def check_user_credentials(cur, username: str):
    cur.execute('SELECT Username FROM accountinfo WHERE Username = ?', (username, ))
    rows = cur.fetchall()
    return len(rows) > 0



def check_password_credentials(cur, password: str):
    cur.execute('SELECT Password FROM accountinfo WHERE Password = ?', (password, ))
    rows = cur.fetchall()
    return len(rows) > 0
    

class Account:
    def __init__(self, code):
        self.code = code
        self.is_valid = code in ACCOUNTS
        self.discount = ACCOUNTS.get(code, 1)