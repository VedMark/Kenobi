#!/usr/bin/python2.7
import random

from PyQt5.QtCore import QObject, pyqtSlot

from modules.tests.questionModel import QuestionModel
from modules.tests.specifications.questionsByTopicSpecification import QuestionsByTopicSpecification


class TestPresenter(QObject):
    def __init__(self, view):
        QObject.__init__(self)
        self._view = view
        self._model = QuestionModel()
        self.__set_connections()

    def __set_connections(self):
        self._view.requireTest.connect(self.getTest)

    @pyqtSlot(str, name='getTest')
    def _getTest(self, topic_id):
        spec = QuestionsByTopicSpecification(topic_id)
        entries = self._model.getEnries(spec)
        entries = map(lambda x: {'id': x.id,
                                 'question': x.question,
                                 'content': x.answer,
                                 'correct': True if x.correct == 1 else False,
                                 'answered': False},
                      entries)
        random.shuffle(entries)
        random.shuffle(entries)
        self._view.reprTest(sorted(entries, key=lambda x: x['question']))
