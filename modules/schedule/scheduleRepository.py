#!/usr/bin/python2.7

from app.database.appRepository import AppRepository
from app.database.exceptions import DatabaseRequestError
from modules.schedule.schedule import Schedule


class ScheduleRepository(AppRepository):
    __ID = 'id'
    __GROUP = 'group'
    __SUBJECT = 'subject'
    __DAY = 'day'
    __LESSON = 'lesson'

    def __init__(self):
            AppRepository.__init__(self)

    def selectSatisfying(self, specification):
        try:
            self.query.exec_(specification.toSqlClauses())
            return self.__build_instances()
        except DatabaseRequestError as exception:
            exception.show()

    def __build_instances(self):
        instances = list()
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                id = self.query.value('id')
                group = self.query.value('class')
                subject = self.query.value('name')
                day = self.query.value('day')
                lesson = self.query.value('lesson')
                instances.append(Schedule(id=id, group=group, subject=subject, day=day, lesson=lesson))
                self.query.next()
            self.query.finish()
        return instances
