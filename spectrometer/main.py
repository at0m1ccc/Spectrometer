import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstWindow import FIOInput


def main():
    app = QApplication(sys.argv)
    window = FIOInput()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
