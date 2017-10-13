#!/usr/bin/python2.7

from abc import abstractmethod, ABCMeta


class SqlSpecification():
    __metaclass__ = ABCMeta

    @abstractmethod
    def toSqlClauses(self):
        # type: () -> str
        pass
