import sys

from PyQt5.QtWidgets import QApplication

from turbotyper.consts import Const
from turbotyper.ui.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(open(Const.STYLES).read())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
