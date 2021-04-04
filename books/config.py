import os


class Configuration:
    def __init__(self):
        self.pg_host = os.getenv('PG_HOST')
        self.pg_port = os.getenv('PG_PORT')
        self.pg_database = os.getenv('PG_DATABASE')
        self.pg_username = os.getenv('PG_USERNAME')
        self.pg_password = os.getenv('PG_PASSWORD')
        self.__pg_connection_url = (
            f'postgresql+psycopg2://{self.pg_username}:{self.pg_password}@{self.pg_host}:{self.pg_port}'
            f'/{self.pg_database}'
        )

    @property
    def pg_connection_url(self):
        return self.__pg_connection_url


CONFIGURATION = Configuration()
