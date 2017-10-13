#!/usr/bin/python2.7

from modules.schedule.scheduleRepository import ScheduleRepository


class ScheduleModel:
    __TABLE_NAME = 'schedules'

    def __init__(self):
        self._repository = ScheduleRepository()

    def getEnries(self, specification):
        return self._repository.selectSatisfying(specification)
