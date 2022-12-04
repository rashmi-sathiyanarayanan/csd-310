import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


def create_client_table(cursor):
    cursor.execute("CREATE TABLE client (client_id INT NOT NULL, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL, phone_number BIGINT, DOB DATE, SSN INT, PRIMARY KEY (client_id))")
    db.commit()


def create_account_table(cursor):
    cursor.execute("CREATE TABLE accounts (account_number INT, account_type VARCHAR(255), account_balance DOUBLE, date_created DATE, client_id INT NOT NULL, PRIMARY KEY (account_number), CONSTRAINT fk_client FOREIGN KEY(client_id) REFERENCES client(client_id))")
    db.commit()


def create_assets_table(cursor):
    cursor.execute("CREATE TABLE assets (asset_id INT NOT NULL, asset_type VARCHAR(255) NOT NULL, asset_amount DOUBLE  NOT NULL, client_id INT, PRIMARY KEY(asset_id), CONSTRAINT FOREIGN KEY(client_id)REFERENCES client(client_id))")
    db.commit()


def create_transactions_table(cursor):
    cursor.execute("CREATE TABLE transactions (transaction_id INT NOT NULL, transaction_type VARCHAR(255) NOT NULL, transaction_amount DOUBLE NOT NULL, transaction_date DATE, account_number INT NOT NULL, PRIMARY KEY(transaction_id), CONSTRAINT fk_accounts FOREIGN KEY(account_number)REFERENCES accounts(account_number))")
    db.commit()


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))


    cursor = db.cursor()
    create_client_table(cursor)
    print ("\n Client table created successfully")
    create_account_table(cursor)
    print("\n Accounts table created successfully")
    create_transactions_table(cursor)
    print("\n Transactions table created successfully")
    create_assets_table(cursor)
    print("\n Assets table created successfully")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
