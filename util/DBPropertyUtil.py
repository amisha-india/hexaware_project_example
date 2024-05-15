class PropertyUtil:
    @staticmethod
    def get_property_string():
        """Generates connection string given the server name and database name"""

        SERVER_NAME = "DESKTOP-DLFEC7O\SQLEXPRESS"
        DATABASE_NAME = "HexawareMoviesDB"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={SERVER_NAME};"
            f"Database={DATABASE_NAME};"
            f"Trusted_Connection=yes;"
        )

        return conn_str