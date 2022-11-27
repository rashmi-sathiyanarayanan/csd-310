import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    cursor.execute("""SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' 
                      from film inner join genre on film.genre_id = genre.genre_id 
                      inner join studio on film.studio_id = studio.studio_id""")

    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any line to continue...")

    cursor = db.cursor()
    title = "DISPLAYING FILMS"

    show_films(cursor, title)

    cursor.execute("INSERT into film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (4, 'Avengers', 2020, 135, 'Joss Whedon', 2, 2)")
    title = "DISPLAYING FILMS AFTER INSERT"
    show_films(cursor, title)

    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2")
    title = "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror"
    show_films(cursor, title)

    cursor.execute("DELETE from movies.film WHERE film_name = 'Gladiator'")
    title = "DISPLAYING FILMS AFTER DELETE"
    show_films(cursor, title)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
