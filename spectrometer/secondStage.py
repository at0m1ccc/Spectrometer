from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import main
import configparser


class SpectrometerInput(QWidget):
    def __init__(self, fullName, ini_file, main_window):
        super().__init__()
        self.fullName = fullName
        self.main_window = main_window
        self.spectrometerName = None
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')
        self.main_window.setWindowTitle(config.get('Settings', 'window_title'))
        self.labLabel = QLabel(f"Лаборант {self.fullName}", self)
        self.label = QLabel(config.get('Settings', 'prompt'), self)
        self.lineEdit = QLineEdit(self)

        self.backButton = QPushButton(config.get('Buttons', 'back'), self)
        self.backButton.clicked.connect(self.go_back)

        self.applyButton = QPushButton(config.get('Buttons', 'apply'), self)
        self.applyButton.clicked.connect(self.apply_spectrometer)

        self.nextButton = QPushButton(config.get('Buttons', 'next'), self)
        self.nextButton.clicked.connect(self.next_stage)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.applyButton)
        self.buttonLayout.addWidget(self.nextButton)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labLabel)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.layout.addLayout(self.buttonLayout)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def go_back(self):
        self.close()
        main.start_first_stage(self.main_window)

    def apply_spectrometer(self):
        self.spectrometerName = self.lineEdit.text()
        self.labLabel.setText(f"Лаборант {self.fullName}\nСпектрометр: {self.spectrometerName}")

    def next_stage(self):
        #self.spectrometerName = self.lineEdit.text()
        self.labLabel.setText(f"Переход к следующему этапу с названием спектрометра: {self.spectrometerName}")
