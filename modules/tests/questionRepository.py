#!/usr/bin/python2.7

from app.database.appRepository import AppRepository
from modules.tests.question import Question


class QuestionRepository(AppRepository):
    __ID = 'id'
    __QUESTION = 'question'
    __ANSWER_TEXT = 'answer_text'
    __IS_CORRECT = 'is_correct'

    def __init__(self):
        AppRepository.__init__(self)

    def _build_instances(self):
        instances = list()
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                id = self.query.value(QuestionRepository.__ID)
                question = self.query.value(QuestionRepository.__QUESTION)
                answer_text = self.query.value(QuestionRepository.__ANSWER_TEXT)
                is_correct = self.query.value(QuestionRepository.__IS_CORRECT)
                instances.append(Question(id=id, question=question, answer=answer_text, correct=is_correct))
                self.query.next()
            self.query.finish()
        return instances
