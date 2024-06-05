from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import main
import configparser


class SampleInput(QWidget):
    def __init__(self, fullName, spectrometerName, ini_file, main_window):
        super().__init__()
        self.main_window = main_window
        self.fullName = fullName
        self.spectrometerName = spectrometerName
        self.sampleName = None
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')
        self.main_window.setWindowTitle(config.get('Settings', 'window_title'))
        self.infoLabel = QLabel(f"Лаборант {self.fullName}\nСпектрометр: {self.spectrometerName}", self)
        self.label = QLabel(config.get('Settings', 'sample_name'), self)
        self.lineEdit = QLineEdit(self)

        self.messageLabel = QLabel("", self)

        self.backButton = QPushButton(config.get('Buttons', 'back'), self)
        self.backButton.clicked.connect(self.go_back)

        self.applyButton = QPushButton(config.get('Buttons', 'apply'), self)
        self.applyButton.clicked.connect(self.apply_sample)

        self.nextButton = QPushButton(config.get('Buttons', 'next'), self)
        self.nextButton.clicked.connect(self.next_stage)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.applyButton)
        self.buttonLayout.addWidget(self.nextButton)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.infoLabel)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.messageLabel)
        self.layout.addLayout(self.buttonLayout)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def go_back(self):
        self.close()
        main.start_second_stage(self.main_window, self.fullName)

    def apply_sample(self):
        if self.lineEdit.text() != '':
            self.sampleName = self.lineEdit.text()
            self.infoLabel.setText(f"Лаборант {self.fullName}\nСпектрометр: {self.spectrometerName}\nПроба: {self.sampleName}")
        else:
            self.messageLabel.setText('Сначала введите название пробы!')

    def next_stage(self):
        if self.lineEdit.text() == '' and self.sampleName is None:
            self.messageLabel.setText('Сначала введите название пробы!')
            return
        elif self.lineEdit.text() is not None and self.sampleName is None:
            self.sampleName = self.lineEdit.text()

        main.start_fourth_stage(self.main_window, self.fullName, self.spectrometerName, self.sampleName)
