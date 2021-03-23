from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel


class Game:
    def __init__(self, timer, wpm, accuracy):
        self.timer = timer
        self.wpm = wpm
        self.accuracy = accuracy
        self.started = False
        self.stopped = False

    def begin(self):
        self.timer.begin()
        self.wpm.begin()
        #self.accuracy.begin()
        self.started = True

    def reset(self):
        self.timer.reset()
        self.wpm.reset()
        #self.accuracy.reset()
        self.started = False

    def finish(self):
        self.timer.finish()
        self.wpm.finish()
        #self.accuracy.finish()
        self.stopped = True
        self.timer.setText(f"Done! {self.timer.text()}")

class Timer(QLabel):
    def __init__(self, *args, **kwargs):
        super(Timer, self).__init__("00:00", *args, **kwargs)
        self._seconds = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self._update)

    def _update(self):
        self._seconds += self._timer.interval() / 1000
        m = int(self._seconds // 60)
        s = int(self._seconds % 60)
        self.setText(f"{m:02}:{s:02}")

    def begin(self):
        self._timer.start(500) # update every half second

    def reset(self):
        self.setText("00:00")
        self._seconds = 0
        self._timer.stop()

    def finish(self):
        self._timer.stop()

class Wpm(QLabel):
    def __init__(self, *args, **kwargs):
        super(Wpm, self).__init__("0 wpm", *args, **kwargs)
        self._correct = 0
        self._seconds = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self._update)

    def _update(self):
        self._seconds += self._timer.interval() / 1000
        wpm = round((self._correct / 5) / (self._seconds / 60))
        self.setText(f"{wpm} wpm")

    def begin(self):
        self._timer.start(100) # update every tenth of a second

    def reset(self):
        self.setText("0 wpm")
        self._correct = 0
        self._seconds = 0
        self._timer.stop()

    def finish(self):
        self._timer.stop()

    def addCorrect(self, chars):
        self._correct += chars

class Accuracy(QLabel):
    def __init__(self, *args, **kwargs):
        super(Accuracy, self).__init__(*args, **kwargs)
