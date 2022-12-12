import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    print("\n--DISPLAYING Year and Month from transaction_date--")
    cursor.execute("""select *, EXTRACT(YEAR from transaction_date) AS year, 
                   EXTRACT(MONTH from transaction_date) as month from transactions""")

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    print("\n--Displaying records grouped by account_number, year amd month of transaction--")
    cursor.execute("""select account_number, month,year, count(*) as count from
                      (select *, EXTRACT(YEAR from transaction_date) AS year, EXTRACT(MONTH from transaction_date) as month 
                      from transactions) a group by account_number, year, month having count >10""")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


    print("\n--Join with account table to get the client_id--")
    cursor.execute("""select b.*, c.client_id from
                      (select account_number, month,year, count(*) as count from 
                      (select *, EXTRACT(YEAR from transaction_date) AS year, EXTRACT(MONTH from transaction_date) as month 
                      from transactions) a group by account_number, year, month having count >10) b 
                      inner join accounts c on b.account_number = c.account_number""")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

    print("\n--Count of clients having more than ten transactions in a month--")
    cursor.execute("""select count(distinct d.client_id) as count from 
                      (select b.*, c.client_id from(select account_number, month,year, count(*) as count from 
                      (select *, EXTRACT(YEAR from transaction_date) AS year, EXTRACT(MONTH from transaction_date) as month from 
                      transactions) a group by account_number, year, month having count >10) b 
                      inner join accounts c on b.account_number = c.account_number)d""")

    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()