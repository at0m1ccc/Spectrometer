import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
import firstStage
import fourthStage
import secondStage
import generalMenu
import thirdStage
import configparser

NumberStage = 0
info = {"fullName": "", "spectrometer": "", "sample": "", "key2": "", "key4": ""}


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


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setMenuWidget(generalMenu.GeneralMenu(main_window))
    start_first_stage(main_window)
    main_window.show()
    sys.exit(app.exec_())


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


if __name__ == '__main__':
    main()
