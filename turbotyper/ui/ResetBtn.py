from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton
from turbotyper.consts import Const


class ResetBtn(QPushButton):
    def __init__(self, typebox, quote, game, *args, **kwargs):
        super(ResetBtn, self).__init__(*args, **kwargs)
        self._typebox = typebox
        self._quote = quote
        self._game = game

        self.setFixedSize(50, 50)
        self.setIcon(QIcon(Const.RESET))
        self.setIconSize(QSize(40, 40))
        self.clicked.connect(self._onClick)

    def _onClick(self):
        self._game.stopped = False
        self._game.reset() # reset timer, wpm, accuracy
        self._quote.reset() # regenerate quote
        self._typebox.clear() # clear typebox
        self._typebox.setFocus() # activate typebox
