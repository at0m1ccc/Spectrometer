from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtGui import QFont
import main
import configparser


class SpectrometerInput(QWidget):
    def __init__(self, ini_file, main_window):
        main.NumberStage = 2
        main.configFile = ini_file
        super().__init__()
        self.main_window = main_window
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')

        font = QFont("Arial", 10)
        self.main_window.setWindowTitle(config.get('Settings', 'window_title'))

        self.infoLabel = QLabel(f"Лаборант {main.info["fullName"]}", self)
        self.infoLabel.setFont(QFont("Arial", 10))

        self.label = QLabel(config.get('Settings', 'prompt'), self)
        self.label.setFont(font)

        self.spectrometers = QComboBox(self)
        list_spectrs = config.get('Settings', 'spectrometers').split(",")
        for spectrometer in list_spectrs:
            self.spectrometers.addItem(spectrometer)

        self.spectrometers.setEditable(True)

        self.backButton = QPushButton(config.get('Buttons', 'back'), self)
        self.backButton.clicked.connect(self.go_back)
        self.backButton.setFixedSize(210, 50)

        self.applyButton = QPushButton(config.get('Buttons', 'apply'), self)
        self.applyButton.clicked.connect(self.apply_spectrometer)
        self.applyButton.setFixedSize(210, 50)

        self.nextButton = QPushButton(config.get('Buttons', 'next'), self)
        self.nextButton.clicked.connect(self.next_stage)
        self.nextButton.setFixedSize(210, 50)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.applyButton)
        self.buttonLayout.addWidget(self.nextButton)
        self.buttonLayout.setSpacing(25)

        self.layout2 = QHBoxLayout()
        self.layout2.addStretch()
        self.layout2.addWidget(self.infoLabel)
        self.layout2.addStretch()

        self.layout3 = QHBoxLayout()
        self.layout3.addStretch()
        self.layout3.addWidget(self.label)
        self.layout3.addStretch()

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout2)
        self.layout.addWidget(self.spectrometers)
        self.layout.addLayout(self.buttonLayout)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def go_back(self):
        self.close()
        main.start_first_stage(self.main_window)

    def apply_spectrometer(self):
        config = configparser.ConfigParser()
        config.read('config2Stage.ini', encoding='utf-8')

        main.info["spectrometer"] = self.spectrometers.currentText()
        if main.info["spectrometer"]:
            self.infoLabel.setText(f"Лаборант {main.info["fullName"]}\n{main.info["spectrometer"]}")
            if main.info['spectrometer'] not in config.get('Settings', 'spectrometers'):
                config['Settings']['spectrometers'] = f'{main.info['spectrometer']}, {config.get('Settings', 'spectrometers')}'
                with open('config2Stage.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
        else:
            self.messageLabel.setText('Сначала выберите cпектрометр!')

    def next_stage(self):
        config = configparser.ConfigParser()
        config.read('config2Stage.ini', encoding='utf-8')
        main.info["spectrometer"] = self.spectrometers.currentText()
        if main.info["spectrometer"]:
            if main.info['spectrometer'] not in config.get('Settings', 'spectrometers'):
                config['Settings']['spectrometers'] = f'{main.info['spectrometer']}, {config.get('Settings', 'spectrometers')}'
                with open('config2Stage.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
            main.start_third_stage(self.main_window)
        else:
            self.messageLabel.setText('Сначала выберите cпектрометр!')
