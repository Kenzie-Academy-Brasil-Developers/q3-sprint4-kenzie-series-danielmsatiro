from app.models import DatabaseConnector

table = """
            CREATE TABLE if not exists ka_series(
            id BIGSERIAL constraint pk_series primary KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
            );
        """


class Series(DatabaseConnector):
    def __init__(self, **kwargs) -> None:
        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]

    def create_serie(self):
        self.get_conn_cur()
        self.cur.execute(table)

        query_values = tuple(self.__dict__.values())
        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """
        
        self.cur.execute(query, query_values)
        self.conn.commit()
        inserted_serie = self.cur.fetchone()

        self.cur.close()
        self.conn.close()
        
        return inserted_serie

    @classmethod
    def read_series(cls):
        cls.get_conn_cur()
        cls.cur.execute(table)
        
        query = """
            SELECT * FROM ka_series
        """
        
        cls.cur.execute(query)
        series = cls.cur.fetchall()
        
        cls.cur.close()
        cls.conn.close()
        
        return series

    def read_serie_by_id(id):
        pass
