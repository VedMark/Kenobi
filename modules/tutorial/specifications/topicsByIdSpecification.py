#!/usr/bin/python2.7

from app.database.sqlSpecification import SqlSpecification


class TopicsByIdSpecification(SqlSpecification):
    def __init__(self, section_id):
        SqlSpecification.__init__(self)
        self.section_id = section_id

    def toSqlClauses(self):
        return """
        SELECT t.id, t.section, t.title, t.content
        FROM topics t
        WHERE t.section={0};
        """.format(self.section_id)
