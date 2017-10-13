#!/usr/bin/python2.7

import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from app.AppView import AppView


def run_kenobi_app():
    application = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    appWindow = AppView()
    appWindow.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    run_kenobi_app()
