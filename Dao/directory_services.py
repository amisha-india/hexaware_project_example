
# Encapsulation
from util.myDBConnection import myDBConnection
from abc import ABC, abstractmethod


class DirectorNotFoundError(Exception):
    """Exception raised when a director is not found."""

    def __init__(self, director_id):
        super().__init__(f"Director with ID {director_id} not found.")


class IDirectorService(ABC):
    @abstractmethod
    def read_directors(self):
        pass

    @abstractmethod
    def create_director(self, director):
        pass


class DirectorService(IDirectorService, myDBConnection):
    def read_directors(self):
        try:
            self.cursor.execute("Select * from Directors")
            directors = self.cursor.fetchall()  # Get all data
            for director in directors:
                print(director)
        except Exception as e:
            print(e)

    def create_director(self, director):
        try:
            self.cursor.execute(
                "INSERT INTO Directors (Name) VALUES (?)",
                (director.name),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)

    def get_director_by_id(self, director_id):
        try:
            self.cursor.execute(
                "SELECT * FROM Directors WHERE DirectorId = ?", (director_id,)
            )
            director = self.cursor.fetchall()  # Get the director
            if director is None:
                raise DirectorNotFoundError(director_id)
            print(director)
        except Exception as e:
            print(e)
