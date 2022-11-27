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

    input("\n\n Press any line to continue...")

    print("\n--DISPLAYING Studio RECORDS--")
    cursor = db.cursor()

    cursor.execute("SELECT studio_id, studio_name FROM studio")

    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    print("\n\n--DISPLAYING Genre RECORDS--")
    cursor.execute("SELECT genre_id, genre_name FROM genre")

    genre = cursor.fetchall()
    for genre in genre:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    print("\n\n--DISPLAYING Short Film RECORDS--")
    cursor.execute("SELECT film_name, film_runtime FROM film where film_runtime<120")

    films = cursor.fetchall()
    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    print("\n\n--DISPLAYING Director RECORDS in Order--")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

