#!/usr/bin/python2.7

from modules.tutorial.topicRepository import TopicRepository


class TopicModel:
    def __init__(self):
        self._repository = TopicRepository()

    def getEnries(self, specification):
        return self._repository.selectSatisfying(specification)
