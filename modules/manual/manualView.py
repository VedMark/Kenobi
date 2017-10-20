#!/usr/bin/python2.7

from PyQt5.QtCore import QMetaObject, Q_ARG, QVariant, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtQuick import QQuickItem
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from modules.manual.manualPresenter import ManualPresenter


class ManualView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self._presenter = ManualPresenter(self)
        self.reqReprSections.connect(self.setModel)
        self.reqReprTopics.connect(self.setModel)
        self._widget = QQuickWidget(self)
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(1, 1, 1, 1)
        self.layout().addWidget(self._widget)
        self._widget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self._widget.rootContext().setContextProperty('manualView', self)
        self._widget.setSource(QUrl('modules/manual/manualForm/ManualForm.qml'))
        self.getSections()

    _reqSections = pyqtSignal(name='requireSections')
    _reqTopics = pyqtSignal(str, name='requireTopics')
    _reqReprSections = pyqtSignal(QQuickItem, str, list, name='reqReprSections')
    _reqReprTopics = pyqtSignal(QQuickItem, str, list, name='reqReprTopics')

    @pyqtSlot(name='getSections')
    def _getSections(self):
        self.requireSections.emit()

    def reprSectionsList(self, sections):
        self.reqReprSections.emit(self._widget.rootObject(), 'setSectionsModel', sections)

    @pyqtSlot(str, name='getTopics')
    def _getTopics(self, section_id):
        self.requireTopics.emit(section_id)

    def reprTopicsList(self, topics):
        self.reqReprTopics.emit(self._widget.rootObject(), 'setTopicsModel', topics)

    @pyqtSlot(QQuickItem, str, list, name='setModel')
    def _setModel(self, obj, callF, values):
        QMetaObject.invokeMethod(obj, callF, Q_ARG(QVariant, values))
