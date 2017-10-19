#!/usr/bin/python2.7

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QSizePolicy
from modules.schedule.scheduleView import ScheduleView
from modules.manual.manualView import ManualView


class AppView:
    def __init__(self):
        self._mainWindow = QDialog(None)
        self._schedule = ScheduleView()
        self._manual = ManualView()
        self._schedule.setMinimumWidth(25)
        self._schedule.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self._manual.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout = QHBoxLayout()
        layout.addWidget(self._schedule)
        layout.addWidget(self._manual)
        layout.setContentsMargins(0, 0, 0, 1)
        self._mainWindow.setLayout(layout)

    def show(self):
        self._mainWindow.showMaximized()
