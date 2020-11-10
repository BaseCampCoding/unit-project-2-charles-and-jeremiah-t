def check_user_credentials(cur, username: str):
    cur.execute('SELECT Username FROM accountinfo WHERE Username = ?', (username, ))
    return True



def check_password_credentials(cur, password: str):
    cur.execute('SELECT Password FROM accountinfo WHERE Password = ?', (password, ))
    return True


    