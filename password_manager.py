import sqlite3

conn = sqlite3.connect('information.db')
cur = conn.cursor()

# cur.execute(""" CREATE TABLE IF NOT EXISTS passwords(
#     Email TEXT,
#     Password TEXT
# )"""
# )

# print("Welcome to the password manager! ")
# while True:
#     answer = input("""Which option suits your needs today?
#     -save
#     -exit
#     >>> """)
#     if answer == 'save':
#         while True:
#             email = input("What's your email?")
#             password = input("What's your password?")
#             cur.execute(""" INSERT INTO passwords (Email, Password) VALUES (?, ?)""", (email, password))