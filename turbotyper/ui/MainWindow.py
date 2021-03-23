from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from turbotyper.consts import Const
from turbotyper.ui.Game import Accuracy, Game, Timer, Wpm
from turbotyper.ui.Heading import Icon, Title
from turbotyper.ui.Quote import Quote
from turbotyper.ui.ResetBtn import ResetBtn
from turbotyper.ui.TypeBox import TypeBox


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self._initUI()

    def _initUI(self):
        headingLo = QHBoxLayout()
        headingLo.addWidget(Title(Const.TITLE))
        headingLo.addStretch(1)
        headingLo.addWidget(Icon(Const.ICON))

        timer = Timer()
        wpm = Wpm()
        accuracy = Accuracy()
        game = Game(timer, wpm, accuracy)

        quote = Quote(game)
        quoteLo = QHBoxLayout()
        quoteLo.addStretch(1)
        quoteLo.addLayout(quote, 13)
        quoteLo.addStretch(1)

        typebox = TypeBox(quote, game)
        resetBtn = ResetBtn(typebox, quote, game)
        typeboxLo = QHBoxLayout()
        typeboxLo.addStretch(1)
        typeboxLo.addWidget(typebox, 12)
        typeboxLo.addWidget(resetBtn, 1)
        typeboxLo.addStretch(1)
        typebox.setFocus() # activate typebox on launch

        gameLo = QHBoxLayout()
        gameLo.addStretch(1)
        gameLo.addWidget(timer, 1)
        gameLo.addStretch(11)
        gameLo.addWidget(wpm, 1)
        gameLo.addStretch(1)

        lo = QVBoxLayout()
        lo.addLayout(headingLo)
        lo.addLayout(quoteLo)
        lo.addSpacing(30)
        lo.addLayout(typeboxLo)
        lo.addSpacing(5)
        lo.addLayout(gameLo)
        lo.addStretch(1)

        window = QWidget()
        window.setLayout(lo)
        self.setCentralWidget(window)
        self.setFixedSize(Const.WIDTH, Const.HEIGHT)
        self.setWindowTitle(Const.TITLE)
