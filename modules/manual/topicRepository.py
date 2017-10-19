#!/usr/bin/python2.7

from app.database.appRepository import AppRepository
from modules.manual.topic import Topic


class TopicRepository(AppRepository):
    __ID = 'id'
    __SECTION = 'section'
    __TITLE = 'title'
    __CONTENT = 'content'

    def __init__(self):
        AppRepository.__init__(self)

    def _build_instances(self):
        instances = list()
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                id = self.query.value(TopicRepository.__ID)
                section = self.query.value(TopicRepository.__SECTION)
                title = self.query.value(TopicRepository.__TITLE)
                content = self.query.value(TopicRepository.__CONTENT)
                instances.append(Topic(id=id, section=section, title=title, content=content))
                self.query.next()
            self.query.finish()
        return instances
