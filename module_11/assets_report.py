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

    print("\n--DISPLAYING Asset RECORDS--\n")

    cursor = db.cursor()

    # The first query is to select all the fields from the assets table
    cursor.execute("SELECT asset_id, asset_type, asset_amount, client_id FROM movies.assets")
    assets = cursor.fetchall()
    for asset in assets:
        print(f"Asset ID:      {asset[0]}");
        print(f"Asset Type:    {asset[1]}");
        print(f"Asset Amount: ${asset[2]}");
        print(f"Client ID:     {asset[3]}\n");

    retrieve = "Select AVG(asset_amount) AS average from assets;"
    cursor.execute(retrieve)
    assets = cursor.fetchall()
    for asset in assets:
        print(f"The average of all client assets is: $" + str(asset[0]))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()