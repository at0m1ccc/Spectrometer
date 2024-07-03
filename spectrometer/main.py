import os
import socket
import sys
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
    sock = acquire_lock()

    try:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.addToolBar(generalMenu.GeneralMenu(main_window))
        main_window.setStatusBar(QStatusBar())
        start_first_stage(main_window)
        main_window.show()
        sys.exit(app.exec_())
    finally:
        release_lock(sock)


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


HOST = '127.0.0.1'
PORT = 9999


def acquire_lock():
    try:
        # Создаем сокет и привязываем его к указанному хосту и порту
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(1)  # Разрешаем только одно подключение (экземпляр программы)
        print(f"Программа запущена на порту {PORT}")
        return sock
    except OSError as e:
        # Если порт уже занят, программа уже запущена
        print(f"Программа уже запущена. Ошибка: {e}")
        sys.exit(1)


def release_lock(sock):
    sock.close()

if __name__ == '__main__':
    main()
