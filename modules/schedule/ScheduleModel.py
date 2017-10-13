#!/usr/bin/python2.7

from modules.schedule.ScheduleRepository import ScheduleRepository
from modules.schedule.specifications.AllGroupsSpecification import AllGroupsSpecification
from modules.schedule.specifications.ScheduleByGroupSpecification import ScheduleByGroupSpecification


class ScheduleModel:
    __TABLE_NAME = 'schedules'

    def __init__(self):
        self._repository = ScheduleRepository()

    def getGroups(self):
        spec = AllGroupsSpecification()
        entries = self._repository.selectSatisfying(spec)
        return sorted([entry.group for entry in entries])

    def getScheduleByGroup(self, gr_name):
        spec = ScheduleByGroupSpecification(gr_name)
        entries = self._repository.selectSatisfying(spec)
        return entries
