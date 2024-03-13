from db.conn import get_connection
from .entities.Movie import Movie

# Model is like Repository


class MovieModel():

    # Con classmethod se instancia directamente
    @classmethod
    def get_movies(self):
        try:
            conn = get_connection()
            movies = []

            with conn.cursor() as cursor:
                cursor.execute(
                    'SELECT id, title, duration, released from movie ORDER BY title ASC')
                result_set = cursor.fetchall()

                for row in result_set:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())
            conn.close()
            return movies
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def get_movie_by_id(self, id):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                print(id)
                cursor.execute(
                    'SELECT id, title, duration, released FROM movie WHERE id = %s', (id,))  # for some reason it has to be a comma
                row = cursor.fetchone()
                print(row)
                movie = None
                if row:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie = movie.to_JSON()
                print(movie)
            conn.close()
            return movie
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def add_movie(self, movie):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                print(id)
                cursor.execute("""INSERT INTO movie (id, title, duration, released) 
                                VALUES (%s, %s, %s, %s) """, (movie.id, movie.title, movie.duration, movie.released))
                affected_rows = cursor.rowcount
                conn.commit()  # Confirm changes with commit
            conn.close()
            return affected_rows
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def remove_movie_by_id(self, id):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                print(id)
                cursor.execute(
                    'DELETE FROM movie WHERE id = %s', (id,))  # for some reason it has to be a comma
                affected_rows = cursor.rowcount
                conn.commit()  # Confirm changes with commit
            conn.close()
            return affected_rows
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    @classmethod
    def update_movie(self, movie: Movie):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                # UPDATE Customers
                # SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
                # WHERE CustomerID = 1;
                cursor.execute("""UPDATE movie
                                SET title = %s, duration = %s, released = %s 
                                WHERE id = %s""", 
                                (movie.title, movie.duration, movie.released, movie.id))
                affected_rows = cursor.rowcount
                conn.commit()  # Confirm changes with commit
            conn.close()
            return affected_rows
        except Exception as ex:
            print(ex)
            raise Exception(ex)
