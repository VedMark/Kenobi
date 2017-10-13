#!/usr/bin/python2.7

from utils.specifications import SqlSpecification


class ScheduleByGroupSpecification(SqlSpecification):
    def __init__(self, group):
        SqlSpecification.__init__(self)
        self.group = group

    def toSqlClauses(self):
        return """
        SELECT sch.id, sch.class, s.name, sch.day, sch.lesson
        FROM schedules sch, subjects s
        WHERE sch.subject = s.id AND sch.class={0};
        """.format(self.group)
