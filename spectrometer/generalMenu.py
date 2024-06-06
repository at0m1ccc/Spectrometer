import configparser

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class GeneralMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        config = configparser.ConfigParser()
        config.read('configGeneralMenu.ini', encoding='utf-8')

        self.infoButton = QPushButton(config['InfoButton']['text'])
        self.infoButton.setFixedSize(int(config['InfoButton']['size']), int(config['InfoButton']['size']))
        self.infoButton.setFixedSize(150,100)

        self.stagesButton = QPushButton(config['StagesButton']['text'])
        self.stagesButton.setFixedSize(int(config['StagesButton']['size']), int(config['StagesButton']['size']))
        self.stagesButton.setFixedSize(150,100)

        self.configButton = QPushButton(config['ConfigButton']['text'])
        self.configButton.setFixedSize(int(config['ConfigButton']['size']), int(config['ConfigButton']['size']))
        self.configButton.setFixedSize(150,100)

        self.updateButton = QPushButton(config['UpdateButton']['text'])
        self.updateButton.setFixedSize(int(config['UpdateButton']['size']), int(config['UpdateButton']['size']))
        self.updateButton.setFixedSize(150,100)


        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.infoButton)
        hbox_buttons.addWidget(self.stagesButton)
        hbox_buttons.addWidget(self.configButton)
        hbox_buttons.addWidget(self.updateButton)

        vbox_layout = QVBoxLayout()

        vbox_layout.addLayout(hbox_buttons)

        self.setLayout(vbox_layout)
