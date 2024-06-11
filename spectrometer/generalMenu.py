import configparser
import os
import webbrowser

from PyQt5.QtCore import Qt

import main

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QDialog, QLabel, QComboBox, QCheckBox


class GeneralMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.updateButton = None
        self.configButton = None
        self.stagesButton = None
        self.infoButton = None
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'configGeneralMenu.ini'), encoding='utf-8')

        self.infoButton = QPushButton(config['InfoButton']['text'])
        self.infoButton.setFixedSize(int(config['InfoButton']['size']), int(config['InfoButton']['size']))
        self.infoButton.setFixedSize(150, 100)
        self.infoButton.clicked.connect(self.open_info)

        self.stagesButton = QPushButton(config['StagesButton']['text'])
        self.stagesButton.setFixedSize(int(config['StagesButton']['size']), int(config['StagesButton']['size']))
        self.stagesButton.setFixedSize(150, 100)
        self.stagesButton.clicked.connect(self.go_to_other_stages)

        self.configButton = QPushButton(config['ConfigButton']['text'])
        self.configButton.setFixedSize(int(config['ConfigButton']['size']), int(config['ConfigButton']['size']))
        self.configButton.setFixedSize(150, 100)

        self.updateButton = QPushButton(config['UpdateButton']['text'])
        self.updateButton.setFixedSize(int(config['UpdateButton']['size']), int(config['UpdateButton']['size']))
        self.updateButton.setFixedSize(150, 100)

        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.infoButton)
        hbox_buttons.addWidget(self.stagesButton)
        hbox_buttons.addWidget(self.configButton)
        hbox_buttons.addWidget(self.updateButton)

        vbox_layout = QVBoxLayout()

        vbox_layout.addLayout(hbox_buttons)

        self.setLayout(vbox_layout)

    @staticmethod
    def open_info():
        webbrowser.open(os.path.join(os.path.dirname(__file__), 'manual.pdf'))

    def go_to_other_stages(self):
        dialog = CustomDialog(self.main_window)
        dialog.exec_()


class CustomDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Переход по этапам")
        self.setFixedSize(300, 150)
        self.main_window = main_window

        self.label = QLabel("Выберите на какой этап перейти", self)
        self.label.setBaseSize(50, 100)
        self.stages = QComboBox(self)
        count = 1
        while count <= main.NumberStage:
            self.stages.addItem(str(count))
            count += 1

        self.checkbox = QCheckBox("Подтвердить переход", self)

        self.transitionButton = QPushButton("Перейти", self)
        self.transitionButton.clicked.connect(self.move_to_stage)

        self.revokeButton = QPushButton("Отмена", self)
        self.revokeButton.clicked.connect(self.cancel_move)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.revokeButton)
        self.buttons_layout.addWidget(self.transitionButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.stages)
        layout.addWidget(self.checkbox)
        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)

    def move_to_stage(self):
        if self.checkbox.isChecked():
            if self.stages.currentIndex() == 0:
                main.start_first_stage(self.main_window)
            elif self.stages.currentIndex() == 1:
                main.start_second_stage(self.main_window)
            elif self.stages.currentIndex() == 2:
                main.start_third_stage(self.main_window)
            elif self.stages.currentIndex() == 3:
                main.start_fourth_stage(self.main_window)
            self.close()

    def cancel_move(self):
        self.close()
