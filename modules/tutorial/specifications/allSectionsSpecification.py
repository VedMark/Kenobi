#!/usr/bin/python2.7

from app.database.sqlSpecification import SqlSpecification


class AllSectionsSpecification(SqlSpecification):
    def __init__(self):
        SqlSpecification.__init__(self)
        pass

    def toSqlClauses(self):
        return """
        SELECT DISTINCT *
        FROM sections s
        """
