#!/usr/bin/python2.7

from modules.tests.questionRepository import QuestionRepository


class QuestionModel:
    def __init__(self):
        self._repository = QuestionRepository()

    def getEnries(self, specification):
        return self._repository.selectSatisfying(specification)
