#!/usr/bin/python2.7

from PyQt5.QtCore import QObject, QMetaObject, Q_ARG, QVariant, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtQuick import QQuickItem
from PyQt5.QtQuickWidgets import QQuickWidget
from modules.schedule.schedulePresenter import SchedulePresenter


class ScheduleView(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self._presenter = SchedulePresenter(self)
        self._widget = QQuickWidget(parent)
        self._widget.rootContext().setContextProperty('scheduleView', self)
        self._widget.rootContext().setContextProperty('groupsModel', self)
        self._widget.setSource(QUrl('modules/schedule/form.qml'))
        self.reqReprSchedules.connect(self.setScheduleModel)

    _reqGroups = pyqtSignal(name='requireGroups')

    @pyqtSlot(name='getGroups')
    def _getGroups(self):
        self.requireGroups.emit()

    def reprGroupsList(self, groups):
        self.setPropertyList('groupsModel', groups)

    def setPropertyList(self, objectName, values):
        self._widget.rootContext().setContextProperty(objectName, values)

    _reqSchedules = pyqtSignal(str, name='requireSchedules', arguments=['group'])

    @pyqtSlot(str, name='getSchedules')
    def _getSchedules(self, group):
        self.requireSchedules.emit(group)

    _reqReprSchedules = pyqtSignal(QQuickItem, list, name='reqReprSchedules')

    @pyqtSlot(QQuickItem, list, name='setScheduleModel')
    def _setScheduleModel(self, obj, values):
        QMetaObject.invokeMethod(obj, "setScheduleModel", Q_ARG(QVariant, values))

    def reprSchedules(self, schedules):
        self.reqReprSchedules.emit(self._widget.rootObject(), schedules)
