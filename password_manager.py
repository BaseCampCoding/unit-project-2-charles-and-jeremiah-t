import sqlite3
import computing
import PySimpleGUI as app

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
        layout = [[app.Text("Welcome to the InfoSeeker!")], [app.Text("Here's everyone's information.")], 
        [app.Text("Information: ", size = (30,1))], [app.Text("Username: charles", size= (40,1))], [app.Text("Email: charles@bcca.org", size= (40,1))], [app.Text("Password: password", size=(40,1))], [app.Text("Username: jeremiah", size= (40,1))], [app.Text("Email: jeremiahtatum@yahoo.com", size=(40,1))], [app.Text("Password: tacobell", size= (40,1))], [app.Button("Exit")]]
        user_info = ((username_validation, ))
        password_info = ((password_validation, ))
        def user_dict_info(cur, info):
            info_dict = {}
            for index, column in enumerate(cur.description):
                info_dict[column[0]] = user_info[index]
            return info_dict
        cur.execute('SELECT 1 as Username')
        conn.row_factory = user_dict_info
        print(cur.fetchone() [0])
        print(user_dict_info(cur, user_info))

        def password_dict_info(cur, info):
            password_dict = {}
            for index, column in enumerate(cur.description):
                password_dict[column[0]] = password_info[index]
            return password_dict
        cur.execute('SELECT 3 as Password')
        conn.row_factory = password_dict_info
        print(cur.fetchone() [0])
        print(password_dict_info(cur, password_info))
    

    else:
        print("Sorry. Failed to log in.")
    # def user_dict_info(cur, info):
    #     info_dict = {}
    #     for index, column in enumerate(cur.description):
    #         info_dict[column[0]] = user_info[index]
    #     return info_dict
    # cur.execute('SELECT 1 as Username')
    # conn.row_factory = user_dict_info
    # print(cur.fetchone() [0])
    # print(user_dict_info(cur, user_info))

    # def password_dict_info(cur, info):
    #     password_dict = {}
    #     for index, column in enumerate(cur.description):
    #         password_dict[column[0]] = password_info[index]
    #     return password_dict
    # cur.execute('SELECT 3 as Password')
    # conn.row_factory = password_dict_info
    # print(cur.fetchone() [0])
    # print(password_dict_info(cur, password_info))
    

    window = app.Window("InfoSeeker", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == app.WINDOW_CLOSED:
            break
        window[' -OUT- '].update(values[' -IN- '])



elif choice == 'exit':
    pass

else:
    print("Invalid option")