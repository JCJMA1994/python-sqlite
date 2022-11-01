import sqlite3


def connect():
    """
    Connect to the database
    """
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    return conn, cursor


def createTable(connection, cursor):
    """
    Create the table
    """
    query = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        user TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL);"""
    cursor.execute(query)
    connection.close()
    print("Table created successfully")


def insertData(connection, cursor):
    """
    Insert data into the table
    """
    query = "insert into users (id, user, email, password) values (2, 'Ginni', 'ggervaise0@ustream.tv', '123456789');"
    cursor.execute(query)
    connection.commit()
    print("Data inserted successfully")
    connection.close()


def selectData(connection, cursor):
    """
    Select data from the table
    """
    query = "select * from users;"
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data


def updateData(connection, cursor):
    """
    Update data from the table
    """
    query = "update users set password = '987654321' where id = 1;"
    cursor.execute(query)
    connection.commit()
    print("Data updated successfully")
    connection.close()


def deleteData(connection, cursor):
    """
    Delete data from the table
    """
    query = "delete from users where id = 1;"
    cursor.execute(query)
    connection.commit()
    print("Data deleted successfully")
    connection.close()


if __name__ == "__main__":
    con, cur = connect()
    createTable(con, cur)
    # insertData(con, cur)
    # print(selectData(con, cur))
    # updateData(con, cur)
    # deleteData(con, cur)
