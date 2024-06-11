from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
import configparser
import main


class FIOInput(QWidget):
    def __init__(self, ini_file, main_window):
        main.NumberStage = 1
        super().__init__()
        self.main_window = main_window
        self.fullName = None
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')

        self.main_window.setWindowTitle(config['MainWindow.firstStage']['title'])

        self.label = QLabel(config['Label']['text'], self)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QComboBox(self)
        self.messageLabel = QLabel(config['MessageLabel']['text'], self)

        laborants = config.get('LineEdit', 'laborants').split(',')
        for laborant in laborants:
            self.lineEdit.addItem(laborant.strip())

        self.applyButton = QPushButton(config['ApplyButton']['text'], self)
        self.applyButton.clicked.connect(self.apply_full_name)
        self.applyButton.setFixedSize(320, 50)

        self.nextButton = QPushButton(config['NextButton']['text'], self)
        self.nextButton.clicked.connect(self.next_stage)
        self.nextButton.setFixedSize(320, 50)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.applyButton)
        button_layout.addWidget(self.nextButton)
        button_layout.setSpacing(25)
        button_layout.setContentsMargins(0, 25, 0, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addLayout(button_layout)
        layout.addWidget(self.messageLabel)

        self.setLayout(layout)

    def apply_full_name(self):
        main.info["fullName"] = self.lineEdit.currentText()
        if main.info["fullName"]:
            self.messageLabel.setText('ФИО применено: ' + main.info["fullName"])
        else:
            self.messageLabel.setText('Сначала выберите фио!')

    def next_stage(self):
        if not main.info["fullName"]:
            self.messageLabel.setText('Сначала выберите фио!')
            return
        else:
            main.start_second_stage(self.main_window)
