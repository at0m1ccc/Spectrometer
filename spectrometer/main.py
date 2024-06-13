import os
import sys
import fcntl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStatusBar, \
    QMessageBox

import fifthStage
import firstStage
import fourthStage
import secondStage
import generalMenu
import thirdStage
import portalocker
import configparser

NumberStage = 0
info = {"fullName": "", "spectrometer": "", "sample": "", "key2": "", "key4": ""}
configFile = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setFixedSize(700, 300)
        self.central_widget = None
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

    def setWindowTitle(self, title):
        super().setWindowTitle(title)

    def closeEvent(self, event):
        closeMessage = QMessageBox()
        closeMessage.setWindowTitle('Подтверждение закрытия')
        closeMessage.setText('Вы уверены, что хотите закрыть приложение?')
        closeMessage.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        closeMessage.button(QMessageBox.Yes).setText('Да')
        closeMessage.button(QMessageBox.No).setText('Нет')
        reply = closeMessage.exec_()

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    lock_fd = acquire_lock()

    try:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.addToolBar(generalMenu.GeneralMenu(main_window))
        main_window.setStatusBar(QStatusBar())
        start_first_stage(main_window)
        main_window.show()
        sys.exit(app.exec_())
    finally:
        release_lock(lock_fd)


def start_first_stage(main_window):
    main_window.setCentralWidget(firstStage.FIOInput(
        os.path.join(os.path.dirname(__file__), 'config1Stage.ini'), main_window))


def start_second_stage(main_window):
    main_window.setCentralWidget(secondStage.SpectrometerInput(
        os.path.join(os.path.dirname(__file__), 'config2Stage.ini'), main_window))


def start_third_stage(main_window):
    main_window.setCentralWidget(thirdStage.SampleInput(
        os.path.join(os.path.dirname(__file__), 'config3Stage.ini'), main_window))


def start_fourth_stage(main_window):
    main_window.setCentralWidget(fourthStage.KeyInput(
        os.path.join(os.path.dirname(__file__), 'config4Stage.ini'), main_window))


def start_fifth_stage(main_window):
    main_window.setCentralWidget(fifthStage.OutputStage(
        os.path.join(os.path.dirname(__file__), 'config5Stage.ini'), main_window))


LOCK_FILE = '/tmp/my_app.lock'


def acquire_lock():
    try:
        lock_fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_RDONLY)
        return lock_fd
    except FileExistsError:
        print("Программа уже запущена. Выход.")
        sys.exit(1)


def release_lock(lock_fd):
    os.close(lock_fd)
    os.remove(LOCK_FILE)


if __name__ == '__main__':
    main()
