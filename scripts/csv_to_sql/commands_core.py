import psycopg2
from abc import abstractmethod, ABC


class Command(ABC):

    @abstractmethod
    def set_command(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_command(self):
        pass


class Copy(Command):

    def __init__(self):
        self.__command = ''

    def set_command(self, table_name: str, fields: list, file_path: str, delimiter: str) -> None:
        self.__command = f"COPY {table_name} ({', '.join(fields)}) FROM '{file_path}' DELIMITER '{delimiter}' CSV HEADER;"

    def get_command(self, *args, **kwargs) -> str:
        return self.__command


class Count(Command):

    def __init__(self):
        self.table_name = ''

    def set_command(self, table_name) -> None:
        self.table_name = f"SELECT COUNT(*) FROM {table_name};"

    def get_command(self) -> str:
        return self.table_name


class DBConnection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db_name: str, user_name: str, password: str, host: str, port: str):
        self.db_name = db_name
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port

    def connect_and_run(self, sql_command) -> None:
        try:
            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user_name,
                password=self.password,
                host=self.host,
                port=self.port
            )
            cursor = connection.cursor()
            cursor.execute(sql_command)
            connection.commit()
            print(f'Соединение установлено: {sql_command} выполнено')

        except (Exception, psycopg2.Error) as error:
            print('Соединение открыть не удалось:', error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print('Соедитнение закрыто')

