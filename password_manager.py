import sqlite3
import computing

conn = sqlite3.connect('information.db')
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS accountinfo(
    Username TEXT,
    Email TEXT,
    Password TEXT
)"""
)


print("Welcome! ")
choice = input("""What would you like to do?
    - New Account
    -Login to Account
    -Exit
    [new/login/exit]
    > """).lower()
# while True:
if choice == 'new':
    username = input("What woud you like your user name to be? ")
    email = input("What's your email? ")
    password_first = input("What would you like your password to be? ")
    while True:
        password_same = input("Please reenter your password. ")
        if password_first == password_same:
            password = password_first
            
            break
        else:
            print("Passwords do not match please try again. ")
    

    cur.execute(""" INSERT INTO accountinfo (Username, Email, Password) VALUES (?, ?, ?)""", (username, email, password))
    conn.commit()
    conn.close()

elif choice == 'login':
    username_validation = input("Username: ")
    password_validation = input("Password: ")
    uncheck = computing.check_user_credentials(cur, username_validation)
    pwcheck = computing.check_password_credentials(cur, password_validation)
    if uncheck and pwcheck == True:
        print("You have successfully logged in!")
    else:
        print("Sorry. Failed to log in.")

    # uncheck = computing.check_credentials(cur, username)



 elif choice == 'exit':
     break

 else:
    print("Invalid option")
