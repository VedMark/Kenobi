#!/usr/bin/python2.7

from app.database.sqlSpecification import SqlSpecification


class QuestionsByTopicSpecification(SqlSpecification):
    def __init__(self, topic_id):
        SqlSpecification.__init__(self)
        self.topic_id = topic_id

    def toSqlClauses(self):
        return """
        SELECT t.id, t.question, a.answer_text, a.is_correct
        FROM answers a LEFT OUTER JOIN tests t
        ON t.id = a.test_id
        WHERE from_topic = {0}
        """.format(self.topic_id)
