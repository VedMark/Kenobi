#!/usr/bin/python2.7

from PyQt5.QtCore import QMetaObject, Q_ARG, QVariant, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtQuick import QQuickItem
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from modules.schedule.schedulePresenter import SchedulePresenter


class ScheduleView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self._presenter = SchedulePresenter(self)
        self._widget = QQuickWidget(self)
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(1, 1, 1, 1)
        self.layout().addWidget(self._widget)
        self._widget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self._widget.rootContext().setContextProperty('scheduleView', self)
        self._widget.rootContext().setContextProperty('groupsModel', self)
        self._widget.setSource(QUrl('modules/schedule/scheduleForm/ScheduleForm.qml'))
        self.reqReprSchedules.connect(self.setModel)
        self.reqInitSchedule.connect(self.initSchedule)

    def handleResizing(self):
        self.setVisible(not self.isVisible())
        if self.isVisible():
            self.reqInitSchedule.emit(self._widget.rootObject())

    _reqGroups = pyqtSignal(name='requireGroups')
    _reqSchedules = pyqtSignal(str, name='requireSchedules', arguments=['group'])
    _reqReprSchedules = pyqtSignal(QQuickItem, str, list, name='reqReprSchedules')
    _reqInitSchedule = pyqtSignal(QQuickItem, name='reqInitSchedule')

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

    @pyqtSlot(QQuickItem, name='initSchedule')
    def _initSchedule(self, obj):
        QMetaObject.invokeMethod(obj, "initSchedule")
