#!/usr/bin/python2.7

from PyQt5.QtCore import QMetaObject, Q_ARG, QVariant, QUrl, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlComponent
from PyQt5.QtQuick import QQuickItem

from modules.tests.testPresenter import TestPresenter


class TestComponent(QQmlComponent):

    def __init__(self, engine, parent=None):
        QQmlComponent.__init__(self, engine, QUrl('modules/tests/testForm/TestForm.qml'), parent)
        self._presenter = TestPresenter(self)
        self._item = self.create()
        self.reqReprTest.connect(self.setModel)

    @pyqtProperty(QQuickItem)
    def item(self):
        return self._item

    _reqTest = pyqtSignal(str, name='requireTest')
    _reqAnswer = pyqtSignal(str, name='requireAnswer')
    _reqReprTest = pyqtSignal(QQuickItem, str, list, name='reqReprTest')
    _reqReprTopics = pyqtSignal(QQuickItem, str, list, name='reqReprTopics')

    @pyqtSlot(str, name='getTest')
    def _getTest(self, topicId):
        self.requireTest.emit(topicId)

    def reprTest(self, tests):
        self.reqReprTest.emit(self._item, 'setTestModel', tests)

    @pyqtSlot(str, name='getAnswer')
    def _getAnswer(self, variant):
        self.requireAnswer.emit(variant)

    def reprTopicsList(self, topics):
        self.reqReprTopics.emit(self._widget.rootObject(), 'setTopicsModel', topics)

    @pyqtSlot(QQuickItem, str, list, name='setModel')
    def _setModel(self, obj, callF, values):
        QMetaObject.invokeMethod(obj, callF, Q_ARG(QVariant, values))
