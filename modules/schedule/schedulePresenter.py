#!/usr/bin/python2.7

from PyQt5.QtCore import QObject, pyqtSlot
from modules.schedule.scheduleModel import ScheduleModel
from modules.schedule.specifications.allGroupsSpecification import AllGroupsSpecification
from modules.schedule.specifications.scheduleByGroupSpecification import ScheduleByGroupSpecification


class SchedulePresenter(QObject):
    def __init__(self, view):
        QObject.__init__(self)
        self._view = view
        self._model = ScheduleModel()
        self.__set_connections()

    def __set_connections(self):
        self._view.requireGroups.connect(self.getGroups)
        self._view.requireSchedules.connect(self.getSchedules)

    @pyqtSlot(name='getGroups')
    def _getGroups(self):
        spec = AllGroupsSpecification()
        entries = self._model.getEnries(spec)
        self._view.reprGroupsList(sorted([entry.group for entry in entries]))

    @pyqtSlot(str, name='getSchedules')
    def _getSchedules(self, group):
        spec = ScheduleByGroupSpecification(group)
        schedules = self._model.getEnries(spec)
        schedules = map(lambda x: {'lesson': x.lesson, 'subject': x.subject, 'day': x.day}, schedules)
        schedules = self.__sortSchedules(schedules)
        self._view.reprSchedules(schedules)

    @staticmethod
    def __sortSchedules(schedules):
        d = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5}
        schedules = sorted(schedules, key=lambda x: (d[x['day']], x['lesson']))
        return schedules
