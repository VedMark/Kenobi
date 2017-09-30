#!/usr/bin/python3.6

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


def run_kenobi_app():
    application = QApplication(sys.argv)

    widget = QWidget()
    widget.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

    sys.exit(application.exec_())


if __name__ == '__main__':
    run_kenobi_app()
