#!/usr/bin/python2.7

from utils.specifications import SqlSpecification


class AllGroupsSpecification(SqlSpecification):
    def __init__(self):
        SqlSpecification.__init__(self)
        pass

    def toSqlClauses(self):
        return """
        SELECT DISTINCT sch.id, sch.class, s.name, sch.day, sch.lesson
        FROM schedules sch, subjects s
        WHERE sch.class=s.id
        GROUP BY class;
        """
