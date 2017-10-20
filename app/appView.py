#!/usr/bin/python2.7

from PyQt5.QtWidgets import QDialog, QSizePolicy, QPushButton, \
    QStylePainter, QStyleOptionButton, QStyle, QHBoxLayout
from modules.schedule.scheduleView import ScheduleView
from modules.manual.manualView import ManualView


class ShrinkExpandButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.setFixedWidth(2 * self.fontMetrics().height())
        self.setStyleSheet('QPushButton { \
                           font: bold 20px "Helvetica"; \
                           background: rgb(255, 210, 0); \
                           border: 2px solid black \
                           }')

    def paintEvent(self, event):
        painter = QStylePainter(self)
        painter.rotate(-90)
        painter.translate(-self.height(), 0)
        option = QStyleOptionButton()
        self.initStyleOption(option)
        size = option.rect.size()
        size.transpose()
        option.rect.setSize(size)
        painter.drawControl(QStyle.CE_PushButton, option)


class AppView:
    def __init__(self):
        self._mainWindow = QDialog(None)

        self._button = ShrinkExpandButton("Schedule", self._mainWindow)
        self._schedule = ScheduleView(self._mainWindow)
        self._manual = ManualView(self._mainWindow)

        self._mainWindow.setLayout(QHBoxLayout())
        self._mainWindow.layout().setSpacing(0)
        self._mainWindow.layout().setContentsMargins(0, 0, 0, 0)
        self._mainWindow.layout().addWidget(self._schedule)
        self._mainWindow.layout().addWidget(self._button)
        self._mainWindow.layout().addWidget(self._manual)

        self._schedule.setVisible(False)
        self._schedule.setFixedWidth(300)
        self._button.clicked.connect(self._schedule.handleResizing)

    def show(self):
        self._mainWindow.showMaximized()
