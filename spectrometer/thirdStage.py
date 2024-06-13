from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtGui import QFont
import main
import configparser


class SampleInput(QWidget):
    def __init__(self, ini_file, main_window):
        main.NumberStage = 3
        main.configFile = ini_file
        super().__init__()
        self.main_window = main_window
        self.init_ui(ini_file)

    def init_ui(self, ini_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')
        self.main_window.setWindowTitle(config.get('Settings', 'window_title'))

        self.infoLabel = QLabel(f"Лаборант {main.info["fullName"]}\nСпектрометр: {main.info["spectrometer"]}", self)
        self.infoLabel.setFont(QFont("Arial", 9))

        self.label = QLabel(config.get('Settings', 'sample_name'), self)
        self.label.setFont(QFont("Arial", 9))

        self.samplesBox = QComboBox(self)
        self.samplesBox.setEditable(True)

        samples = config.get('Settings', 'samples').split(',')
        for sample in samples:
            self.samplesBox.addItem(sample.strip())

        self.messageLabel = QLabel("", self)

        self.backButton = QPushButton(config.get('Buttons', 'back'), self)
        self.backButton.clicked.connect(self.go_back)
        self.backButton.setFixedSize(215, 55)

        self.applyButton = QPushButton(config.get('Buttons', 'apply'), self)
        self.applyButton.clicked.connect(self.apply_sample)
        self.applyButton.setFixedSize(215, 55)

        self.nextButton = QPushButton(config.get('Buttons', 'next'), self)
        self.nextButton.clicked.connect(self.next_stage)
        self.nextButton.setFixedSize(215, 55)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.applyButton)
        self.buttonLayout.addWidget(self.nextButton)
        self.buttonLayout.setSpacing(15)
        self.buttonLayout.setContentsMargins(0,5,0,50)

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
        self.layout.addWidget(self.samplesBox)
        self.layout.addWidget(self.messageLabel)
        self.layout.addLayout(self.buttonLayout)


        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def go_back(self):
        self.close()
        main.start_second_stage(self.main_window)

    def apply_sample(self):
        config = configparser.ConfigParser()
        config.read('config3Stage.ini', encoding='utf-8')
        main.info["sample"] = self.samplesBox.currentText()
        if main.info["sample"]:
            self.infoLabel.setText(f"Лаборант {main.info["fullName"]}\nСпектрометр: {main.info["spectrometer"]}\nПроба: {main.info["sample"]}")
            if main.info['sample'] not in config.get('Settings', 'samples'):
                config['Settings']['samples'] = f'{main.info['sample']}, {config.get('Settings', 'samples')}'
                with open('config3Stage.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
        else:
            self.messageLabel.setText('Сначала введите название пробы!')

    def next_stage(self):
        config = configparser.ConfigParser()
        config.read('config3Stage.ini', encoding='utf-8')
        main.info["sample"] = self.samplesBox.currentText()
        if main.info["sample"]:
            self.infoLabel.setText(
                f"Лаборант {main.info["fullName"]}\nСпектрометр: {main.info["spectrometer"]}\nПроба: {main.info["sample"]}")
            if main.info['sample'] not in config.get('Settings', 'samples'):
                config['Settings']['samples'] = f'{main.info['sample']}, {config.get('Settings', 'samples')}'
                with open('config3Stage.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
            main.start_fourth_stage(self.main_window)
        else:
            self.messageLabel.setText('Сначала введите название пробы!')

