from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel


class Title(QLabel):
    def __init__(self):
        super().__init__("turbo_typer")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setOffset(2.5, 2.5)
        self.setGraphicsEffect(shadow)

class Icon(QLabel):
    def __init__(self):
        super().__init__()
        icon = QPixmap("turbotyper/resources/img/icon-0.png").scaled(180, 150)
        self.setPixmap(icon)
