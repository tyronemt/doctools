import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)


def create_db():
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS DB;")

    cursor.execute("USE DB;")

    cursor.execute("CREATE TABLE IF NOT EXISTS USERS (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255) NOT NULL, UNIQUE (`id`));")

    cursor.execute("CREATE TABLE IF NOT EXISTS EVENTS (id INT AUTO_INCREMENT PRIMARY KEY, userID INT NOT NULL, name VARCHAR(255) NOT NULL, description TEXT, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

    cursor.execute("CREATE TABLE tasks (id INT AUTO_INCREMENT PRIMARY KEY, userID INT NOT NULL, name VARCHAR(255) NOT NULL, description TEXT, complete BOOLEAN NOT NULL DEFAULT 0, due_date DATE, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

    print(cursor.rowcount, "record inserted.")

    cursor.close()


def create_user(name):
    cursor = mydb.cursor()

    QUERY = "INSERT INTO USERS (name) VALUES ('%s');" % name
    cursor.execute(QUERY)

    print(QUERY)
    mydb.commit()
    cursor.close()

def create_event(userID, name, description):
    cursor = mydb.cursor()

    QUERY = "INSERT INTO EVENTS (userID , name, description) VALUES (%d, '%s', '%s');" % userID, name, description
    print(QUERY)

    cursor.execute(QUERY)
    mydb.commit()
    cursor.close()



def create_task(userID, name, description, due_date):
    cursor = mydb.cursor()

    QUERY = "INSERT INTO tasks (userID, name, description, complete, due_date) VALUES ( %d, '%s',  '%s', 0, '%s');" % userID, name, description, due_date
    print(QUERY)

    cursor.execute(QUERY)
    mydb.commit()
    cursor.close()

if __name__ == "__main__":
    create_db()