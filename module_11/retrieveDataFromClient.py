# Red Team
# Ronald Stewart
# Rashmi Sathiyanarayanan
# Oyun Tsolmon
# Module 11.1
# 10 December 2022

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


def display_client_added_each_month(cursor):
    cursor.execute("SELECT DATE_FORMAT(`date_created`, '%Y-%m') as `date`, count(date_created) as `client_count` FROM client WHERE date_created >= CURDATE() - INTERVAL 6 MONTH GROUP BY `date`, MONTH(`date_created`) ORDER BY `client_count` DESC")
    clients = cursor.fetchall()
    print("-- DISPLAYING how many clients were added EACH MONTH for the past six months --")
    for client in clients:
        print("Date Created: {}\nNumber Of Clients added: {}\n".format(client[0], client[1]))


def display_client_added_for_the_last_six_month(cursor):
    cursor.execute("SELECT first_name, last_name, date_created FROM client WHERE date_created >= CURDATE() - INTERVAL 6 MONTH")
    clients = cursor.fetchall()
    print("-- DISPLAYING the clients added for the PAST SIX MONTHS--")
    for client in clients:
        print("First Name: {}\nLast Name: {}\nDate Created: {}\n".format(client[0], client[1], client[2]))


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))


    cursor = db.cursor()

    display_client_added_for_the_last_six_month(cursor)
    display_client_added_each_month(cursor)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
