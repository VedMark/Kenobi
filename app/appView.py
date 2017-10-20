#!/usr/bin/python2.7

from PyQt5.QtWidgets import QDialog, QHBoxLayout
from modules.schedule.scheduleView import ScheduleView
from modules.tutorial.tutorialView import TutorialView


class AppView:
    def __init__(self):
        self._mainWindow = QDialog(None)

        self._schedule = ScheduleView(self._mainWindow)
        self._tutorial = TutorialView(self._mainWindow)

        self._mainWindow.setLayout(QHBoxLayout())
        self._mainWindow.layout().setSpacing(0)
        self._mainWindow.layout().setContentsMargins(0, 0, 0, 0)
        self._mainWindow.layout().addWidget(self._schedule)
        self._mainWindow.layout().addWidget(self._tutorial)

    def show(self):
        self._mainWindow.showMaximized()
