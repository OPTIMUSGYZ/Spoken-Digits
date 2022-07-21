import os
import sys

import numpy as np
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from MainUI import Ui_MainWindow
from runSupport import recordAudio, trimAudio, generateMelSpec, createModel, predict, write


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
        self.sampleRate = 48000

    def buttonClicked(self):
        self.timerStart = True
        self.seconds = self.duration
        self.recording = recordAudio(self.sampleRate, self.duration, '/temp/')
        self.predict = True

    def timeout(self):
        if self.seconds > 0 and self.timerStart:
            self.seconds -= 1
            self.ui.lcdOut.display(self.seconds)
        elif self.predict:
            self.timerStart = False
            self.predict = False
            write(os.path.join("./temp/orgOut.wav"), self.sampleRate, self.recording)
            trimAudio('/temp/')
            img = generateMelSpec('/temp/', '/temp/')
            model = createModel(256, 0.00049, 7)
            p = predict(model, img)
            if p == -1:
                self.ui.lcdOut.display('F')
            self.ui.lcdOut.display(p)
        else:
            self.timerStart = False


# Create the Qt Application
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Run the main Qt loop
sys.exit(app.exec())
