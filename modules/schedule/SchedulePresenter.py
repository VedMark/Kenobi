#!/usr/bin/python2.7

from PyQt5.QtCore import QObject, pyqtSlot
from modules.schedule.ScheduleModel import ScheduleModel


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
        self._view.reprGroupsList(self._model.getGroups())

    @pyqtSlot(str, name='getSchedules')
    def _getSchedules(self, group):
        schedules = self._model.getScheduleByGroup(group)
        schedules = map(lambda x: {'lesson': x.lesson, 'subject': x.subject, 'day': x.day}, schedules)
        schedules =  self.__sortSchedules(schedules)
        self._view.reprSchedules(schedules)

    def __sortSchedules(self, schedules):
        d = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5}
        sort_days = lambda x: (d[x['day']], x['lesson'])
        schedules = sorted(schedules, key=sort_days)
        return schedules