from PyQt5.QtWidgets import QLabel
from turbotyper.ui.FlowLayout import FlowLayout


class Word(QLabel):
    def __init__(self, word, *args, **kwargs):
        super(Word, self).__init__(word, *args, **kwargs)
        self.word = word

    def curr(self):
        self.setStyleSheet("background: lightgrey;")

    def warn(self):
        self.setStyleSheet("background: red;")

    def right(self):
        self.setStyleSheet("color: green;")

    def wrong(self):
        self.setStyleSheet("color: red;")

class Quote(FlowLayout):
    def __init__(self, game, *args, **kwargs):
        super(Quote, self).__init__(*args, **kwargs)
        self._game = game
        self._quote = Quote._get()
        self._curr = 0
        self._initUI()

    @staticmethod
    def _get():
        # TODO return a random paragraph
        return "The queen stood. \"And what of my wrath, Lord Stark?\" she asked softly. Her eyes searched his face. \"You should have taken the realm for yourself. It was there for the taking. Jaime told me how you found him on the Iron Throne the day King's Landing fell, and made him yield it up. That was your moment. All you needed to do was climb those steps, and sit. Such a sad mistake.\""

    def _initUI(self):
        for i, word in enumerate(self._quote.split()):
            w = Word(word)
            if i == 0:
                w.curr()
            self.addWidget(w)

    def submit(self, attempt):
        prev = self.itemAt(self._curr).widget()
        if prev.word == attempt:
            prev.right()
            self._game.wpm.addCorrect(len(prev.word) + 1)
        else:
            prev.wrong()

        self._curr += 1
        if self._curr >= self.count():
            self._game.finish()
        else:
            self.itemAt(self._curr).widget().curr()

    def notify(self, attempt):
        curr = self.itemAt(self._curr).widget()
        if not curr.word.startswith(attempt):
            curr.warn()
        else:
            curr.curr()

    def reset(self):
        self._quote = Quote._get()
        self._curr = 0
        for i in range(self.count()):
            self.itemAt(i).widget().deleteLater()
        self._initUI()
