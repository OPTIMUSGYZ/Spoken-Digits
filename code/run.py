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
        self.duration = 3
        self.seconds = self.duration - 1
        timer = QTimer(self)
        timer.start(1000)
        self.timerOn = False
        timer.timeout.connect(self.timeout)
        self.predict = False
        self.recording = np.empty(0)
        self.sampleRate = 48000
        self.recordStart = False
        self.ui.lcdOut.display('')

    def buttonClicked(self):
        self.seconds = self.duration
        self.ui.lcdOut.display('')
        self.timerOn = True
        self.recordStart = True
        self.predict = True

    def timeout(self):
        if self.recordStart:
            self.ui.btnRecord.setText('Stops in...')
            self.ui.lblMic.hide()
            self.recording = recordAudio(self.sampleRate, self.duration, '/temp/')
            self.recordStart = False
        if self.seconds > 0 and self.timerOn:
            self.ui.lblCountDown.setText(str(self.seconds))
            self.seconds -= 1
        elif self.seconds == 0 and self.timerOn:
            self.ui.lblCountDown.setText(str(self.seconds))
            self.ui.btnRecord.setText('Predicting...')
            self.timerOn = False
        elif self.predict:
            self.predict = False
            write(os.path.join("./temp/orgOut.wav"), self.sampleRate, self.recording)
            print("Finished")
            trimAudio('/temp/')
            img = generateMelSpec('/temp/', '/temp/')
            model = createModel(100, 0.0002, 49)
            p = predict(model, img)
            # self.ui.lcdOut.show()
            if p == -1:
                self.ui.lcdOut.display('F')
            self.ui.lcdOut.display(p)
            self.ui.btnRecord.setText('Click to Record')
            self.ui.lblCountDown.setText('')
            self.ui.lblMic.show()
        else:
            self.timerOn = False


# Create the Qt Application
app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Run the main Qt loop
sys.exit(app.exec())
