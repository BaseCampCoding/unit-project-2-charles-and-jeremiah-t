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

cur.execute(""" CREATE TABLE IF NOT EXISTS passwords(
    UserID INTEGER,
    Application TEXT,
    Username TEXT,
    Email TEXT,
    Password TEXT
)"""
)

while True:
    print("Welcome! ")
    choice = input("""What would you like to do?
        - New Account
        -Login to Account
        -Exit
        [new/login/exit]
        > """).lower()

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
        pass
    elif choice == 'login':
        username_validation = input("Username: ")
        password_validation = input("Password: ")
        uncheck = computing.check_user_credentials(cur, username_validation)
        pwcheck = computing.check_password_credentials(cur, password_validation)
        
        if uncheck and pwcheck == True:
            print("You have successfully logged in!")
            while True:
                answer = input("""What would you like to do? 
                - Save information
                - View information
                - Exit
                [Save/ View/ Exit]
                """)

                if answer == 'save':
                    userID = input("Enter your pin number. ")
                    application = input("What application are you using? ")
                    username = input(f"What's your username for {application}? ")
                    email = input(f"What's your email for {application}? ")
                    password = input(f"What's your password for {application}? ")
                    pin_num = int(userID)
                    cur.execute(""" INSERT INTO passwords VALUES(?, ?, ?, ?, ?)""", (pin_num, application, username, email, password))
                    conn.commit()
                    # con.close()
                    continue
                elif answer == 'view':
                    answer2 = input(""" Would you like to view one or all? \n [one/all] """).strip().lower()
                    if answer2 == 'one':
                        appp = input("Which application would you like information for? \n")
                        username = input("What's your Pin Code? ")
                        test = computing.Password.get_app_info(appp, username)
                        

                    elif answer2 == 'all':
                        userID = input("What's your Pin Number ")
                        pin_num = int(userID)
                        computing.Password.print_all(pin_num)
                    else:
                        print("Invalid Sorry.")

                    
                    continue
                elif answer == 'exit':
                    break
                else:
                    print("Invalid Option. ")

           

        else:
            print("Sorry. Failed to log in.")

    elif choice == 'exit':
        break

    else:
        print("Invalid option")