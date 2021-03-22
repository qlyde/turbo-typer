from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class TypeBox(QLineEdit):
    def __init__(self, quote, game):
        super().__init__()
        self.quote = quote
        self._game = game

        self.setPlaceholderText("type here...")
        self.setFocus()

    def keyPressEvent(self, event):
        if not self._game.stopped:
            # start game on first keypress
            if not self._game.started:
                self._game.begin()

            if event.key() == Qt.Key.Key_Space:
                self.quote.submit(self.text())
                self.clear()
            else:
                super(TypeBox, self).keyPressEvent(event)
                self.quote.notify(self.text())
