import mysql.connector
import datetime
import json

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)

def drop_db():
  cursor = mydb.cursor()
  cursor.execute("DROP DATABASE `db`;")

def create_db():
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS DB;")

    cursor.execute("USE DB;")

    cursor.execute("CREATE TABLE IF NOT EXISTS USERS (id INT AUTO_INCREMENT PRIMARY KEY, username varchar(255) NOT NULL, UNIQUE (`id`));")

    cursor.execute("CREATE TABLE IF NOT EXISTS EVENTS (id INT AUTO_INCREMENT PRIMARY KEY, userID INT NOT NULL, name VARCHAR(255) NOT NULL, description TEXT, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

    cursor.execute("CREATE TABLE tasks (id INT AUTO_INCREMENT PRIMARY KEY, userID INT NOT NULL, name VARCHAR(255) NOT NULL, description TEXT, complete BOOLEAN NOT NULL DEFAULT 0, due_date DATE, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

    print(cursor.rowcount, "record inserted.")

    cursor.close()


def create_user(username):
    cursor = mydb.cursor()
    cursor.execute("USE DB;")

    QUERY = "INSERT INTO USERS (username) VALUES ('%s');" % username
    cursor.execute(QUERY)

    print(QUERY)
    mydb.commit()
    cursor.close()

def create_event(userID, name, description):
    print(userID, name, description)
    cursor = mydb.cursor()
    cursor.execute("USE DB;")

    QUERY = "INSERT INTO EVENTS (userID , name, description) VALUES (%d, '%s', '%s');" %(userID, name, description)
    print(QUERY)

    cursor.execute(QUERY)
    mydb.commit()
    cursor.close()



def create_task(userID, name, description, due_date):
    cursor = mydb.cursor()
    cursor.execute("USE DB;")

    QUERY = "INSERT INTO tasks (userID, name, description, complete, due_date) VALUES ( %d, '%s',  '%s', 0, '%s');" % (userID, name, description, due_date)
    print(QUERY)

    cursor.execute(QUERY)
    mydb.commit()
    cursor.close()

def check_user(username):
    cursor = mydb.cursor()
    cursor.execute("USE DB;")

    QUERY = "SELECT * FROM USERS WHERE username = '%s'" % username
    print(QUERY)
    cursor.execute(QUERY)
    results = cursor.fetchall()
    cursor.close()

    for users in results:
        return users[0]
    return None

def get_events(user_id):
    cursor = mydb.cursor()
    cursor.execute("USE DB;")
    QUERY = "SELECT * FROM EVENTS WHERE userID = %d" % user_id
    print(QUERY)
    cursor.execute(QUERY)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_tasks(user_id):
    cursor = mydb.cursor()
    cursor.execute("USE DB;")
    QUERY = "SELECT * FROM TASKS WHERE userID = %d" % user_id
    print(QUERY)
    cursor.execute(QUERY)
    results = cursor.fetchall()
    cursor.close()
    lst = [] 
    for tasks in results:
        lst.append(tasks)
    return lst

if __name__ == "__main__":
    drop_db()
    create_db()