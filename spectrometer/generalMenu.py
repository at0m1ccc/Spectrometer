import configparser
import os
import webbrowser

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

import main

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QDialog, QLabel, QComboBox, QCheckBox, \
    QToolBar, QAction, QStatusBar, QToolButton, QMenu


class GeneralMenu(QToolBar):
    def __init__(self, main_window):
        super().__init__()
        self.updateButton = None
        self.configAction = None
        self.stagesButton = None
        self.infoButton = None
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'configGeneralMenu.ini'), encoding='utf-8')

        self.setIconSize(QSize(25, 25))
        self.addSeparator()
        self.setMovable(False)

        self.infoButton = QAction(QIcon("info.png"), config['InfoButton']['text'])
        self.infoButton.triggered.connect(self.open_info)
        self.addAction(self.infoButton)

        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QIcon('stages.png'))
        self.toolButton.setToolTip(config['StagesButton']['text'])
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)

        # Создаем QMenu
        self.menu = QMenu(self)

        stages = config.get('StagesButton', 'stages').split(', ')
        # Добавляем элементы в меню
        for stage in stages:
            self.add_menu_item(stage)

        # Устанавливаем меню для кнопки
        self.toolButton.setMenu(self.menu)
        self.addWidget(self.toolButton)

        self.configAction = QAction(QIcon("refactor.png"), config['ConfigButton']['text'])
        self.configAction.triggered.connect(self.open_config)
        self.addAction(self.configAction)

        self.updateButton = QAction(QIcon("file.png"), config['UpdateButton']['text'])
        self.addAction(self.updateButton)

    def add_menu_item(self, name):
        action = QAction(f'{name} этап', self)
        match name:
            case "Первый":
                action.triggered.connect(self.move_to_first_stage)
            case "Второй":
                action.triggered.connect(self.move_to_second_stage)
            case "Третий":
                action.triggered.connect(self.move_to_third_stage)
            case "Четвертый":
                action.triggered.connect(self.move_to_fourth_stage)
            case "Пятый":
                action.triggered.connect(self.move_to_fifth_stage)

        self.menu.addAction(action)

    def move_to_first_stage(self):
        main.start_first_stage(self.main_window)

    def move_to_second_stage(self):
        main.start_second_stage(self.main_window)

    def move_to_third_stage(self):
        main.start_third_stage(self.main_window)

    def move_to_fourth_stage(self):
        main.start_fourth_stage(self.main_window)

    def move_to_fifth_stage(self):
        main.start_fifth_stage(self.main_window)

    @staticmethod
    def open_info():
        webbrowser.open(os.path.join(os.path.dirname(__file__), 'manual.pdf'))

    @staticmethod
    def open_config():
        os.startfile(os.path.join(os.path.dirname(__file__), main.configFile))


# class CustomDialog(QDialog):
#     def __init__(self, main_window):
#         super().__init__()
#         self.setWindowTitle("Переход по этапам")
#         self.setFixedSize(300, 150)
#         self.main_window = main_window
#
#         self.label = QLabel("Выберите на какой этап перейти", self)
#         self.label.setBaseSize(50, 100)
#         self.stages = QComboBox(self)
#         count = 1
#         while count <= main.NumberStage:
#             self.stages.addItem(str(count))
#             count += 1
#
#         self.checkbox = QCheckBox("Подтвердить переход", self)
#
#         self.transitionButton = QPushButton("Перейти", self)
#         self.transitionButton.clicked.connect(self.move_to_stage)
#
#         self.revokeButton = QPushButton("Отмена", self)
#         self.revokeButton.clicked.connect(self.cancel_move)
#
#         self.buttons_layout = QHBoxLayout()
#         self.buttons_layout.addWidget(self.revokeButton)
#         self.buttons_layout.addWidget(self.transitionButton)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.stages)
#         layout.addWidget(self.checkbox)
#         layout.addLayout(self.buttons_layout)
#         self.setLayout(layout)
#
#     def move_to_stage(self):
#         if self.checkbox.isChecked():
#             if self.stages.currentIndex() == 0:
#                 main.start_first_stage(self.main_window)
#             elif self.stages.currentIndex() == 1:
#                 main.start_second_stage(self.main_window)
#             elif self.stages.currentIndex() == 2:
#                 main.start_third_stage(self.main_window)
#             elif self.stages.currentIndex() == 3:
#                 main.start_fourth_stage(self.main_window)
#             self.close()
#
#     def cancel_move(self):
#         self.close()
