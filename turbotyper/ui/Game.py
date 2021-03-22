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

    def finish(self):
        self.timer.finish()
        self.wpm.finish()
        #self.accuracy.finish()
        self.started = False

    def stop(self):
        self.timer.stop()
        self.wpm.stop()
        #self.accuracy.stop()
        self.stopped = True
        self.timer.setText(f"Done! {self.timer.text()}")

class Timer(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("00:00")
        self._seconds = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self._update)

    def _update(self):
        self._seconds += self._timer.interval() // 1000
        m = self._seconds // 60
        s = self._seconds % 60
        self.setText(f"{m:02}:{s:02}")

    def begin(self):
        self._timer.start(1000) # update every second

    def finish(self):
        self.setText("00:00")
        self._seconds = 0
        self._timer.stop()

    def stop(self):
        self._update()
        self._timer.stop()

class Wpm(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("0 wpm")
        self.correct = 0
        self._seconds = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self._update)

    def _update(self):
        self._seconds += self._timer.interval() // 1000
        wpm = round((self.correct / 5) / (self._seconds / 60))
        self.setText(f"{wpm} wpm")

    def begin(self):
        self._timer.start(2000) # update every 2 seconds

    def finish(self):
        self.setText("0 wpm")
        self.correct = 0
        self._seconds = 0
        self._timer.stop()

    def stop(self):
        self._update()
        self._timer.stop()

class Accuracy(QLabel):
    def __init__(self):
        super().__init__()
