from PyQt5.QtSql import QSqlDatabase

from app.database.exceptions import DatabaseConnectionError


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Connection:
    __metaclass__ = Singleton
    __DATABASE_TYPE = 'QSQLITE'
    __DATABASE_FILE = 'app/database/KenobiDB.sqlite'

    def __init__(self):
        try:
            self.connection = QSqlDatabase.addDatabase(Connection.__DATABASE_TYPE)
            self.connection.setDatabaseName(Connection.__DATABASE_FILE)
            self.connection.open()
            if not self.connection.isOpen():
                raise DatabaseConnectionError(self, 'Cannot open')
        except DatabaseConnectionError as exception:
            exception.show()

    @property
    def type(self):
        return self.__DATABASE_TYPE

    @property
    def file(self):
        return self.__DATABASE_FILE

    def __del__(self):
        self.connection.close()
        del self.connection
