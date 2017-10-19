#!/usr/bin/python2.7

from modules.manual.sectionRepository import SectionRepository


class SectionModel:
    def __init__(self):
        self._repository = SectionRepository()

    def getEnries(self, specification):
        return self._repository.selectSatisfying(specification)
