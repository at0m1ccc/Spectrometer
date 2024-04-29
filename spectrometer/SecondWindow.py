from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import firstWindow


class SpectrometerInput(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.spectrometerName = None
        self.initUI()

    def initUI(self):
        self.parent.setWindowTitle('2 Этап: Выбор названия спектрометра')

        self.labLabel = QLabel(f'Лаборант {self.parent.fio}', self)
        self.label = QLabel('Введите название спектрометра', self)
        self.lineEdit = QLineEdit(self)

        self.backButton = QPushButton('Назад', self)
        self.backButton.clicked.connect(self.goBack)

        self.applyButton = QPushButton('Применить', self)
        self.applyButton.clicked.connect(self.applyName)

        self.nextButton = QPushButton('Вперед', self)
        self.nextButton.clicked.connect(self.nextStage)

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

    def goBack(self):
        # self.closeAllWidgets()
        self.close()
        firstWindow.FIOInput()

    def applyName(self):
        self.parent.spectrometerName = self.lineEdit.text()
        self.labLabel.setText(f'Лаборант {self.parent.fio}\nСпектрометр: {self.parent.spectrometerName}')

    def nextStage(self):
        self.parent.spectrometerName = self.lineEdit.text()
        # Код для инициации следующего этапа
        self.labLabel.setText(f'Переход к следующему этапу с названием спектрометра: {self.parent.spectrometerName}')

    def closeAllWidgets(self):
        self.labLabel.close()
        self.label.close()
        self.lineEdit.close()
        self.backButton.close()
        self.applyButton.close()
        self.nextButton.close()
