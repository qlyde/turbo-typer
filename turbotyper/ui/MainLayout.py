from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from turbotyper.ui.Game import Accuracy, Game, Timer, Wpm
from turbotyper.ui.Heading import Icon, Title
from turbotyper.ui.Quote import Quote
from turbotyper.ui.ResetBtn import ResetBtn
from turbotyper.ui.TypeBox import TypeBox


class MainLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        headingLo = QHBoxLayout()
        headingLo.addWidget(Title())
        headingLo.addStretch(1)
        headingLo.addWidget(Icon())

        timer = Timer()
        wpm = Wpm()
        accuracy = Accuracy()
        game = Game(timer, wpm, accuracy)

        quote = Quote(game)
        quoteLo = QHBoxLayout()
        quoteLo.addStretch(1)
        quoteLo.addLayout(quote, 13)
        quoteLo.addStretch(1)

        typebox = TypeBox(quote, game) # to start game
        resetBtn = ResetBtn(typebox, game) # to end game
        typeboxLo = QHBoxLayout()
        typeboxLo.addStretch(1)
        typeboxLo.addWidget(typebox, 12)
        typeboxLo.addWidget(resetBtn, 1)
        typeboxLo.addStretch(1)

        gameLo = QHBoxLayout()
        gameLo.addStretch(1)
        gameLo.addWidget(timer, 1)
        gameLo.addStretch(11)
        gameLo.addWidget(wpm, 1)
        gameLo.addStretch(1)

        self.addLayout(headingLo)
        self.addLayout(quoteLo)
        self.addSpacing(30)
        self.addLayout(typeboxLo)
        self.addSpacing(5)
        self.addLayout(gameLo)
        self.addStretch(1)
