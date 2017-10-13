#!/usr/bin/python2.7

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from abc import ABCMeta, abstractmethod


class DatabaseError(Exception):
    __metaclass__ = ABCMeta

    def __init__(self, database, message):
        super(DatabaseError, self).__init__(message)
        self._message = message
        self.database = database

    @abstractmethod
    def show(self):
        pass


class DatabaseConnectionError(DatabaseError):
    def __init__(self, database, message):
        super(DatabaseError, self).__init__(database, message)

    def show(self):
        QMessageBox.critical(None,
                             DatabaseConnectionError.__name__,
                             self._message + ' ' + str(self.database))
        QCoreApplication.quit(QCoreApplication.instance())


class DatabaseRequestError(DatabaseError):
    def __init__(self, database, message):
        super(DatabaseError, self).__init__(database, message)

    def show(self):
        QMessageBox.warning(None,
                            DatabaseRequestError.__name__,
                            self._message + ' ' + str(self.database))
