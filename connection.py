import sqlite3


def connect():
    """
    Connect to the database
    """
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    return conn, cursor


def createTable(connection, cursor):
    """
    Create the table
    """
    query = """CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        note_1 INTEGER NOT NULL,
        note_2 INTEGER NOT NULL,
        average INTEGER NOT NULL);"""
    cursor.execute(query)
    connection.close()
    print("Table created successfully")
