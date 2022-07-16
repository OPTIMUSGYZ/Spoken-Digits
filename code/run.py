import os
import sys
import time
import threading
from PySide6.QtCore import QTimer

import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow

from MainUI import Ui_MainWindow
from runSupport import sd, recordAudio, trimAudio, generateMelSpec, createModel, predict
import runSupport as rs


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRecord.clicked.connect(self.buttonClicked)
        self.duration = 4
        self.seconds = self.duration - 1
        timer = QTimer(self)
        timer.start(1000)
        self.timerStart = False
        timer.timeout.connect(self.timeout)
        self.predict = False
        self.recording = np.empty(0)
    def buttonClicked(self):
        self.timerStart = True
        self.seconds = self.duration
        self.recording = recordAudio(48000, self.duration, './temp/')
        self.predict = True
    def timeout(self):
        if self.seconds > 0 and self.timerStart:
            self.seconds -= 1
            self.ui.lcdOut.display(self.seconds)
        elif self.predict:
            self.timerStart = False
            self.predict = False
            trimAudio(48000, './temp/', self.recording)
            img = generateMelSpec('./temp/', './temp/')
            model = createModel(256, 0.00049, 7)
            p = str(predict(model, img))
            self.ui.lcdOut.display(p)
        else:
            self.timerStart = False



# Create the Qt Application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Run the main Qt loop
sys.exit(app.exec())
