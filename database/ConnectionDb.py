#!/usr/bin/python3.6

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from utils import decorators


@decorators.singleton
class ConnectionDb:
    __DATABASE_TYPE = 'QSQLITE'
    __DATABASE_FILE = 'KenobiDB.sqlite'
    __TABLE_INFO_COLUMNS = 'name'

    def __init__(self):
        self.connection = QSqlDatabase.addDatabase('QSQLITE')
        self.connection.setDatabaseName(ConnectionDb.__DATABASE_FILE)
        assert self.connection.open(), \
            'Error while connecting to database ' + self.connection.connectionName()
        self.query = QSqlQuery(self.connection)

    def __str__(self):
        return 'Database: ' + ConnectionDb.__DATABASE_TYPE

    def get_column(self, col_name, table_name):
        request = 'SELECT {0} FROM {1}'.format(col_name, table_name)
        self.__execute_query(request)
        return self.__choose_column(col_name)

    def get_column_names(self, table_name):
        request = 'PRAGMA TABLE_INFO({0})'.format(table_name)
        self.__execute_query(request)
        return self.__choose_column(ConnectionDb.__TABLE_INFO_COLUMNS)

    def __execute_query(self, request):
        return self.query.exec(request)

    def __choose_column(self, column):
        names = []
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                names.append(self.query.value(column))
                self.query.next()
            self.query.finish()
        return names
