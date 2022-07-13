import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import runSupport as rs
from MainUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRecord.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        rs.recordAudio(48000, 3, './temp/')
        img = rs.generateMelSpec('./temp/', './temp/')
        model = rs.createModel(256, 0.00049, 7)
        p = str(rs.predict(model, img))
        self.ui.lblOut.setText(p)
        print(p)


# Create the Qt Application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Run the main Qt loop
sys.exit(app.exec())
