import configparser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

import main


class FIOInput(QWidget):
    def __init__(self, ini_file,  main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui(ini_file)
        self.fullName = None

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')

        self.main_window.setWindowTitle(config['MainWindow']['title'])

        self.label = QLabel(config['Label']['text'], self)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self)
        self.messageLabel = QLabel(config['MessageLabel']['text'], self)

        self.applyButton = QPushButton(config['ApplyButton']['text'], self)
        self.applyButton.clicked.connect(self.apply_full_name)

        self.nextButton = QPushButton(config['NextButton']['text'], self)
        self.nextButton.clicked.connect(self.next_stage)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.applyButton)
        button_layout.addWidget(self.nextButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addLayout(button_layout)
        layout.addWidget(self.messageLabel)

        self.setLayout(layout)

    def apply_full_name(self):
        if self.lineEdit.text() != '':
            self.fullName = self.lineEdit.text()
            self.messageLabel.setText('ФИО применено: ' + self.fullName)
        else:
            self.messageLabel.setText('Сначала введите фио!')

    def next_stage(self):
        if self.lineEdit.text() == '' and self.fullName is None:
            self.messageLabel.setText('Сначала введите фио!')
            return
        elif self.lineEdit.text() is not None and self.fullName is None:
            self.fullName = self.lineEdit.text()

        main.start_second_stage(self.main_window, self.fullName)
