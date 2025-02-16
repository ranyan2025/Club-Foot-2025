import mysql.connector


def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kikokiko",
        database="club_foot"
    )
    return conn
