#!/usr/bin/python2.7

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from abc import abstractmethod, ABCMeta


class AppRepository:
    __metaclass__ = ABCMeta
    __DATABASE_TYPE = 'QSQLITE'
    __DATABASE_FILE = 'app/database/KenobiDB.sqlite'
    __TABLE_INFO_COLUMNS = 'name'

    def __init__(self):
            self.connection = QSqlDatabase.addDatabase('QSQLITE')
            self.connection.setDatabaseName(AppRepository.__DATABASE_FILE)
            self.connection.open()
            self.query = QSqlQuery(self.connection)

    def __del__(self):
        self.connection.close()
        del self.connection
        del self.query

    def __str__(self):
        return 'Database: ' + AppRepository.__DATABASE_TYPE

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
