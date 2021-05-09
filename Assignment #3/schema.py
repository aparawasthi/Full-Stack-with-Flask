import sqlite3

connection = sqlite3.connect('flask_app1.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
        """CREATE TABLE fl_user(
            id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username VARCHAR(255) NOT NULL,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            gender VARCHAR(40) NOT NULL,
            passwd VARCHAR(255) NOT NULL,
            active TINYINT(1) NOT NULL,
            date_add DATETIME NOT NULL,
            date_upd DATETIME NOT NULL,
            reset_password_token VARCHAR(40),
            reset_password_validity DATETIME
        );"""
    )

cursor.execute(
        """CREATE TABLE fl_list(
            id_list INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_user INT(10) NOT NULL,
            name VARCHAR(255) NOT NULL,
            date_add DATETIME NOT NULL,
            date_upd DATETIME NOT NULL
        );"""
    )

cursor.execute(
        """CREATE TABLE fl_task(
            id_task INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_list INT(10) NOT NULL,
            name VARCHAR(255) NOT NULL,
            check_off TINYINT(1) NOT NULL,
            date_add DATETIME NOT NULL,
            date_upd DATETIME NOT NULL
        );"""
    )

connection.commit()
cursor.close()
connection.close()