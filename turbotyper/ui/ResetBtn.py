from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton


class ResetBtn(QPushButton):
    def __init__(self, typebox, game):
        super().__init__()
        self._typebox = typebox
        self._game = game

        self.setFixedSize(50, 50)
        self.setIcon(QIcon("turbotyper/resources/img/reset.png"))
        self.setIconSize(QSize(40, 40))

        self.clicked.connect(self._onClick)

    def _onClick(self):
        self._game.stopped = False
        self._game.finish() # reset timer, wpm, accuracy
        self._typebox.quote.reset() # regenerate quote
        self._typebox.clear() # clear typebox
        self._typebox.setFocus() # activate typebox
