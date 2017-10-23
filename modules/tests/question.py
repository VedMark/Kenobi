#!/usr/bin/python2.7


class Question:
    def __init__(self, id, question, answer, correct):
        self._id = id
        self._question = question
        self._answer = answer
        self._correct = correct

    def _get_id(self):
        return self._id

    def _get_question(self):
        return self._question

    def _get_answer(self):
        return self._answer

    def _get_correct(self):
        return self._correct

    id = property(_get_id)
    question = property(_get_question)
    answer = property(_get_answer)
    correct = property(_get_correct)
