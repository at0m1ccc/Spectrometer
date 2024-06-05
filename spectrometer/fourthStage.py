from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
import main
import configparser


class KeyInput(QWidget):
    def __init__(self, fullName, spectrometerName, sampleName, ini_file, main_window):
        super().__init__()
        self.main_window = main_window
        self.fullName = fullName
        self.spectrometerName = spectrometerName
        self.sampleName = sampleName
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')
        self.main_window.setWindowTitle(config.get('Settings', 'window_title'))
        self.infoLabel = QLabel(f"Лаборант: {self.fullName}\nСпектрометр: {self.spectrometerName}\nПроба: {self.sampleName}", self)
        # self.lineEdit = QLineEdit(self)
        self.key2Label = QLabel("Ключ 2:")
        self.key4Label = QLabel("Ключ 4:")
        self.key2 = QComboBox(self)
        self.key4 = QComboBox(self)

        valueKey2 = config.get('Settings', 'key2').split(",")

        for value in valueKey2:
            self.key2.addItem(value)

        valueKey4 = config.get('Settings', 'key4').split(",")

        for value in valueKey4:
            self.key4.addItem(value)

        self.keysLabel = QHBoxLayout()
        self.keysLabel.addWidget(self.key2Label)
        self.keysLabel.addWidget(self.key2)
        self.keysLabel.addWidget(self.key4Label)
        self.keysLabel.addWidget(self.key4)
        self.keysLabel.setAlignment(Qt.AlignCenter)

        self.messageLabel = QLabel("", self)

        self.backButton = QPushButton(config.get('Buttons', 'back'), self)
        self.backButton.clicked.connect(self.go_back)

        self.nextButton = QPushButton(config.get('Buttons', 'next'), self)
        self.nextButton.clicked.connect(self.next_stage)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.nextButton)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.infoLabel)
        self.layout.addWidget(self.messageLabel)
        self.layout.addLayout(self.keysLabel)
        self.layout.addLayout(self.buttonLayout)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def go_back(self):
        self.close()
        main.start_third_stage(self.main_window, self.fullName, self.spectrometerName)

    def next_stage(self):
        main.start_first_stage(self.main_window)