#!/usr/bin/python2.7

from app.database.appRepository import AppRepository
from modules.schedule.schedule import Schedule


class ScheduleRepository(AppRepository):
    __ID = 'id'
    __GROUP = 'class'
    __SUBJECT = 'name'
    __DAY = 'day'
    __LESSON = 'lesson'

    def __init__(self):
            AppRepository.__init__(self)

    def _build_instances(self):
        instances = list()
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                id = self.query.value(ScheduleRepository.__ID)
                group = self.query.value(ScheduleRepository.__GROUP)
                subject = self.query.value(ScheduleRepository.__SUBJECT)
                day = self.query.value(ScheduleRepository.__DAY)
                lesson = self.query.value(ScheduleRepository.__LESSON)
                instances.append(Schedule(id=id, group=group, subject=subject, day=day, lesson=lesson))
                self.query.next()
            self.query.finish()
        return instances
