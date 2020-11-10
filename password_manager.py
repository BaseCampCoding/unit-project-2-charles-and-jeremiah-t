import sqlite3

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
while True:
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
    break

cur.execute(""" INSERT INTO accountinfo (Username, Email, Password) VALUES (?, ?, ?)""", (username, email, password))
conn.close()
elif answer == 'login':
    username_validation = input("Username: ")
    password_validation = input("Password: ")
    cur.execute(""" SELECT * FROM accountinfo WHERE Username = )


# elif answer == 'exit':

# else:
#     print("Invalid option")
#             cur.execute(""" INSERT INTO passwords (Email, Password) VALUES (?, ?)""", (email, password))