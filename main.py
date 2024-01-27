import psycopg2
from config import host, user, password, dbname, port

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host, user=user, password=password, database=dbname, port=port
    )

    connection.autocommit = True

    # the cursor is performing database operations

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

        # create a new table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE IF NOT EXISTS books(
        #         bookId serial PRIMARY KEY,
        #         title varchar(100) NOT NULL,
        #         authors varchar(100) NOT NULL,
        #         average_rating numeric,
        #         language varchar(50));
        #         """
        #     )
        #     print("[INFO] Table created successfully")

        # insert data into a table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """INSERT INTO books (title, authors, average_rating, language) VALUES
        #         ('The Road to Dune', 'Frank Herbert', 3.86, 'eng'),
        #         ('I am Charlotte Simmons', 'Tom Wolfe', 3.42, 'eng'),
        #         ('The Puffin Book of Nonsense Verse', 'Quentin Blake', 4.02, 'eng'),
        #         ('The Portrait of a Lady', 'Henry James', 3.78, 'eng'),
        #         ('Treasure Island', 'Robert Louis Stevenson', 3.83, 'eng');
        #         """
        #     )
        #     print("[INFO] Data was successfully inserted")

        # get data from a table
        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """SELECT title, authors FROM books
        #         WHERE average_rating > 3.80"""
        #     )
        #     print(cursor.fetchall())

        # delete a table
        with connection.cursor() as cursor:
            cursor.execute("""DROP TABLE books;""")
            print("[INFO] table was deleted")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
