#!/usr/bin/python2.7

from PyQt5.QtCore import QObject, pyqtSlot
from modules.tutorial.specifications.allSectionsSpecification import AllSectionsSpecification
from modules.tutorial.specifications.topicsByIdSpecification import TopicsByIdSpecification
from modules.tutorial.sectionRepository import SectionRepository
from modules.tutorial.topicRepository import TopicRepository


class TutorialPresenter(QObject):
    def __init__(self, view):
        QObject.__init__(self)
        self._view = view
        self._section_repository = SectionRepository()
        self._topic_repository = TopicRepository()
        self.__set_connections()

    def __set_connections(self):
        self._view.requireSections.connect(self.getSections)
        self._view.requireTopics.connect(self.getTopics)

    @pyqtSlot(name='getSections')
    def _getSections(self):
        spec = AllSectionsSpecification()
        entries = self._section_repository.selectSatisfying(spec)
        self._view.reprSectionsList([{'sectionId': entry.id, 'title': entry.section} for entry in entries])

    @pyqtSlot(str, name='getTopics')
    def _getTopics(self, section_id):
        spec = TopicsByIdSpecification(section_id)
        entries = self._topic_repository.selectSatisfying(spec)
        self._view.reprTopicsList([{'id': entry.id,
                                    'section': entry.section,
                                    'title': entry.title,
                                    'content': entry.content
                                    }
                                   for entry in entries])
