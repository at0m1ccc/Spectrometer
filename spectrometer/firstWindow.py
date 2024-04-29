from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import SecondWindow


class FIOInput(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.fio = None

    def initUI(self):
        self.setWindowTitle('1 Этап: Инициация лаборанта')
        self.setFixedSize(1010, 640)

        self.label = QLabel('Введите свое ФИО', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self)
        self.messageLabel = QLabel('', self)

        self.applyButton = QPushButton('Применить', self)
        self.applyButton.clicked.connect(self.applyFIO)

        self.nextButton = QPushButton('Вперед', self)
        self.nextButton.clicked.connect(self.nextStage)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.applyButton)
        self.buttonLayout.addWidget(self.nextButton)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.layout.addLayout(self.buttonLayout)
        self.layout.addWidget(self.messageLabel)

        self.setLayout(self.layout)
        self.show()

    def applyFIO(self):
        if self.lineEdit.text() != '':
            self.fio = self.lineEdit.text()
            self.messageLabel.setText('ФИО применено: ' + self.fio)
        else:
            self.messageLabel.setText('Сначала введите фио!')

    def nextStage(self):
        if self.lineEdit.text() == '' and self.fio is None:
            self.messageLabel.setText('Сначала введите фио!')
            return
        elif self.lineEdit.text() is not None and self.fio is None:
            self.fio = self.lineEdit.text()

        self.label.close()
        self.lineEdit.close()
        self.messageLabel.close()
        self.applyButton.close()
        self.nextButton.close()
        SecondWindow.SpectrometerInput(self)
