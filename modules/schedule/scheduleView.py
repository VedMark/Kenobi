#!/usr/bin/python2.7

from PyQt5.QtCore import QMetaObject, Q_ARG, QVariant, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtQuick import QQuickItem
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QWidget

from modules.schedule.schedulePresenter import SchedulePresenter


class ScheduleView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self._presenter = SchedulePresenter(self)
        self._widget = QQuickWidget(self)
        self._widget.rootContext().setContextProperty('scheduleView', self)
        self._widget.rootContext().setContextProperty('groupsModel', self)
        self._widget.setSource(QUrl('modules/schedule/scheduleForm/ScheduleForm.qml'))
        self.reqReprSchedules.connect(self.setModel)

    _reqGroups = pyqtSignal(name='requireGroups')
    _reqSchedules = pyqtSignal(str, name='requireSchedules', arguments=['group'])
    _reqReprSchedules = pyqtSignal(QQuickItem, str, list, name='reqReprSchedules')

    @pyqtSlot(name='getGroups')
    def _getGroups(self):
        self.requireGroups.emit()

    def reprGroupsList(self, groups):
        self.setPropertyList('groupsModel', groups)

    def setPropertyList(self, objectName, values):
        self._widget.rootContext().setContextProperty(objectName, values)

    @pyqtSlot(str, name='getSchedules')
    def _getSchedules(self, group):
        self.requireSchedules.emit(group)

    def reprSchedules(self, schedules):
        self.reqReprSchedules.emit(self._widget.rootObject(), 'setScheduleModel', schedules)

    @pyqtSlot(QQuickItem, str, list, name='setModel')
    def _setModel(self, obj, callF, values):
        QMetaObject.invokeMethod(obj, callF, Q_ARG(QVariant, values))
