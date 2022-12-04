import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_client(cursor, title):
    cursor.execute("select * from client")

    client = cursor.fetchall()
    print("\n -- {} --".format(title))

    for client in client:
        print(client)

def show_accounts(cursor, title):
    cursor.execute("select * from accounts")

    accounts = cursor.fetchall()
    print("\n -- {} --".format(title))

    for account in accounts:
        print(account)

def show_assets(cursor, title):
    cursor.execute("select * from assets")

    assets = cursor.fetchall()
    print("\n -- {} --".format(title))

    for asset in assets:
        print(asset)


def show_transactions(cursor, title):
    cursor.execute("select * from transactions")

    transactions = cursor.fetchall()
    print("\n -- {} --".format(title))

    for transaction in transactions:
        print(transaction)


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    print("\n Showing tables in database")
    cursor.execute("SHOW Tables")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


    print("\n Inserting values into client")
    cursor.execute(""" INSERT INTO client values
                      (111,'Ron','Stewart','2739 Apple Lane, Macomb, Illinois 61455',3093180133,19901220,111111111),
                      (112,'Oyun','Tsolmon','3732 Farnum Road, New York, New York 10036',2123542070,19910924,222222222),
                      (113,'Rashmi','Sathiyanarayanan','734 Rosemary Way, Newark, Delaware 19713',3028679909,19870205,333333333),
                      (114,'Margaret','Davis','234 New Creek Road, Wheeler, Missisippi 38880',2602249866,19731023,444444444),
                      (115,'Gerard','Osmond','1458 Breezewood Court, Dodge City, Kansas 67801',6203915532,19750326,555555555),
                      (116,'Aaron','Lewis','4785 Woodrow Way, Batson, Texas 77519',9362625016,19920516,666666666)""")

    db.commit()



    print("\n Inserting values into accounts")
    cursor.execute("""INSERT INTO accounts values
                      (12345,'checking',1000,20220112,111),
                      (12346,'checking',245,20220213,112),
                      (12347,'savings',356,20211023,113),
                      (12348,'savings',457,20220517,114),
                      (12349,'checking',888,20220316,115),
                      (12350,'checking',234,20211119,116)""")

    db.commit()


    print("\n Inserting values into assets")
    cursor.execute("""INSERT INTO assets values
                      (1,'real estate',1000000,111),
                      (2,'stock',20000,112),
                      (3,'current assets',300000,113),
                      (4,'commodity',25000,114),
                      (5,'Intangible assets',150000,115),
                      (6,'patent',500000,116),
                      (7,'bond',60000,112),
                      (8,'real estate',500000,113),
                      (9,'stock',50000,111),
                      (10,'commodity',8000,116)""")

    db.commit()

    print("\n Inserting values into transactions")
    cursor.execute("""INSERT INTO transactions values
                      (235,'credit',450,20221012,12345),
                      (236,'credit',451,20221013,12345),
                      (261,'credit',452,20221014,12345),
                      (237,'credit',453,20221014,12345),
                      (238,'credit',454,20221014,12345),
                      (239,'credit',455,20221015,12345),
                      (240,'credit',456,20221016,12345),
                      (241,'credit',457,20221017,12345),
                      (242,'credit',458,20221018,12345),
                      (243,'credit',459,20221018,12345),
                      (244,'credit',460,20221019,12345),
                      (245,'credit',461,20221012,12346),
                      (246,'credit',462,20221012,12346),
                      (247,'credit',463,20221013,12346),
                      (248,'credit',464,20221013,12346),
                      (249,'credit',465,20221014,12346),
                      (250,'credit',466,20221014,12346),
                      (251,'credit',467,20221015,12346),
                      (252,'credit',468,20221016,12346),
                      (253,'credit',469,20221017,12346),
                      (254,'credit',470,20221018,12346),
                      (255,'credit',472,20221019,12346),
                      (256,'debit',4500,20221012,12347),
                      (257,'debit',500,20221012,12347),
                      (258,'credit',200,20221012,12348),
                      (259,'debit',300,20221012,12349),
                      (260,'credit',800,20221012,12350)""")

    db.commit()

    title = "DISPLAYING CLIENT"
    show_client(cursor, title)

    title = "DISPLAYING ACCOUNTS"
    show_accounts(cursor, title)

    title = "DISPLAYING ASSETS"
    show_assets(cursor, title)

    title = "DISPLAYING TRANSACTIONS"
    show_transactions(cursor, title)


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
