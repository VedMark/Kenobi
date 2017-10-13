#!/usr/bin/python2.7

from abc import abstractmethod, ABCMeta
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from app.database.exceptions import DatabaseConnectionError


class AppRepository:
    __metaclass__ = ABCMeta
    __DATABASE_TYPE = 'QSQLITE'
    __DATABASE_FILE = 'app/database/KenobiDB.sqlite'
    __TABLE_INFO_COLUMNS = 'name'

    def __init__(self):
        try:
            self.connection = QSqlDatabase.addDatabase('QSQLITE')
            self.connection.setDatabaseName(AppRepository.__DATABASE_FILE)
            self.connection.open()
            if not self.connection.isOpen():
                raise DatabaseConnectionError(self, 'Cannot open')
            self.query = QSqlQuery(self.connection)
        except DatabaseConnectionError as exception:
            exception.show()

    def __del__(self):
        self.connection.close()
        del self.connection
        del self.query

    def __str__(self):
        return AppRepository.__DATABASE_TYPE + ', ' + AppRepository.__DATABASE_FILE

    @abstractmethod
    def selectSatisfying(self, specification):
        pass

    def __build_instances(self):
        pass

    def __choose_column(self, column):
        names = []
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                names.append(self.query.value(column))
                self.query.next()
            self.query.finish()
        return names
