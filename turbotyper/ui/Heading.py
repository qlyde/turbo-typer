from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel


class Title(QLabel):
    def __init__(self, title, *args, **kwargs):
        super(Title, self).__init__(title, *args, **kwargs)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setOffset(2.5, 2.5)
        self.setGraphicsEffect(shadow)

class Icon(QLabel):
    def __init__(self, icon, *args, **kwargs):
        super(Icon, self).__init__(*args, **kwargs)
        pm = QPixmap(f"{icon}").scaledToHeight(150)
        self.setPixmap(pm)
