from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtGui import QFont
import main
import configparser
from datetime import datetime


class OutputStage(QWidget):
    def __init__(self, ini_file, main_window):
        main.NumberStage = 5
        super().__init__()
        self.main_window = main_window
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')
        self.main_window.setWindowTitle(config.get('Settings', 'window_title'))

        self.infoLabel = QLabel(f"Лаборант: {main.info["fullName"]}\nСпектрометр: {main.info["spectrometer"]}\nПроба: {main.info["sample"]}", self)
        self.infoLabel.setFont(QFont("Arial", 10))

        self.fileName = QLineEdit(f"{datetime.now()}", self)

        self.backButton = QPushButton(config.get('Buttons', 'back'), self)
        self.backButton.clicked.connect(self.go_back)

        self.nextButton = QPushButton(config.get('Buttons', 'next'), self)
        self.nextButton.clicked.connect(self.next_stage)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.nextButton)

        self.infomation = QHBoxLayout()
        self.infomation.addStretch()
        self.infomation.addWidget(self.infoLabel)
        self.infomation.addWidget(self.fileName)
        self.infomation.addStretch()

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.infomation)
        self.layout.addLayout(self.buttonLayout)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def go_back(self):
        self.close()
        main.start_fourth_stage(self.main_window)

    def next_stage(self):
        main.start_first_stage(self.main_window)
