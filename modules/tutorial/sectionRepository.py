#!/usr/bin/python2.7

from app.database.appRepository import AppRepository
from modules.tutorial.section import Section


class SectionRepository(AppRepository):
    __ID = 'id'
    __SECTION = 'name'

    def __init__(self):
            AppRepository.__init__(self)

    def _build_instances(self):
        instances = list()
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                id = self.query.value(SectionRepository.__ID)
                section = self.query.value(SectionRepository.__SECTION)
                instances.append(Section(id=id, section=section))
                self.query.next()
            self.query.finish()
        return instances
