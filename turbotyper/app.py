import sys

from PyQt5.QtWidgets import QApplication

from turbotyper.ui.MainWindow import MainWindow


def main():
    app = QApplication([])
    app.setStyleSheet(open("turbotyper/resources/stylesheet.css").read())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
