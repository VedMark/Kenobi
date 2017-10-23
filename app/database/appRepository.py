#!/usr/bin/python2.7

from abc import abstractmethod, ABCMeta

from PyQt5.QtSql import QSqlQuery

from app.database.connection import Connection
from app.database.exceptions import DatabaseRequestError


class AppRepository:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.connection = Connection()
        self.query = QSqlQuery(self.connection.connection)

    def __str__(self):
        return self.connection.type + ', ' + self.connection.file

    def selectSatisfying(self, specification):
        try:
            self.query.exec_(specification.toSqlClauses())
            return self._build_instances()
        except DatabaseRequestError as exception:
            exception.show()

    @abstractmethod
    def _build_instances(self):
        pass
