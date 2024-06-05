import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
import firstStage
import fourthStage
import secondStage
import generalMenu
import thirdStage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setFixedSize(1010, 640)
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
    main_window.setCentralWidget(firstStage.FIOInput('config1Stage.ini', main_window))


def start_second_stage(main_window, fio):
    main_window.setCentralWidget(secondStage.SpectrometerInput(fio, 'config2Stage.ini', main_window))


def start_third_stage(main_window, fio, spectrometer):
    main_window.setCentralWidget(thirdStage.SampleInput(fio, spectrometer, 'config3Stage.ini', main_window))


def start_fourth_stage(main_window, fio, spectrometer, sample):
    main_window.setCentralWidget(fourthStage.KeyInput(fio, spectrometer, sample, 'config4Stage.ini', main_window))


if __name__ == '__main__':
    main()
