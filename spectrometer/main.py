import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
import firstStage
import secondStage
import generalMenu


class ButtonPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        for i in range(4):
            button = QPushButton(f'Button {i+1}', self)
            button.setFixedSize(50, 50)  # Set the size of the buttons to be square
            layout.addWidget(button)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setFixedSize(1010, 640)
        self.central_widget = None

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create the main layout
        main_layout = QVBoxLayout(central_widget)

        # Add the button panel at the top
        self.button_panel = ButtonPanel(self)
        main_layout.addWidget(self.button_panel)

        # Create a placeholder for the main content
        self.content_area = QWidget(self)
        main_layout.addWidget(self.content_area)


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


if __name__ == '__main__':
    main()
