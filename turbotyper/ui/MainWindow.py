from PyQt5.QtWidgets import QMainWindow, QWidget
from turbotyper.ui.MainLayout import MainLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        window = QWidget()
        window.setLayout(MainLayout())
        self.setCentralWidget(window)

        self.setFixedSize(1280, 720)
        self.setWindowTitle("turbo_typer")
