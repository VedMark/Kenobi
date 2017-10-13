#!/usr/bin/python2.7

from PyQt5.QtWidgets import QDialog
from modules.schedule.scheduleView import ScheduleView


class AppView:
    def __init__(self):
        self._mainWindow = QDialog(None)
        self._schedule = ScheduleView(self._mainWindow)

    def show(self):
        self._mainWindow.showMaximized()
