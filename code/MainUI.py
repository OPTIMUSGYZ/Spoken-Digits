# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 640)
        MainWindow.setMinimumSize(QSize(360, 640))
        MainWindow.setMaximumSize(QSize(360, 640))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(71, 30, 218, 43))
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 370, 111, 31))
        self.label.setAlignment(Qt.AlignCenter)
        self.btnRecord = QPushButton(self.centralwidget)
        self.btnRecord.setObjectName(u"btnRecord")
        self.btnRecord.setGeometry(QRect(140, 270, 80, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRecord.sizePolicy().hasHeightForWidth())
        self.btnRecord.setSizePolicy(sizePolicy)
        self.btnRecord.setMinimumSize(QSize(80, 50))
        self.btnRecord.setMaximumSize(QSize(80, 50))
        self.btnRecord.setBaseSize(QSize(0, 0))
        self.btnRecord.setLayoutDirection(Qt.LeftToRight)
        self.btnRecord.setAutoFillBackground(False)
        self.btnRecord.setIconSize(QSize(0, 0))
        self.lcdOut = QLCDNumber(self.centralwidget)
        self.lcdOut.setObjectName(u"lcdOut")
        self.lcdOut.setGeometry(QRect(210, 330, 111, 101))
        self.lcdOut.setFrameShape(QFrame.NoFrame)
        self.lcdOut.setFrameShadow(QFrame.Plain)
        self.lcdOut.setSmallDecimalPoint(False)
        self.lcdOut.setDigitCount(1)
        self.lcdOut.setMode(QLCDNumber.Hex)
        self.lcdOut.setSegmentStyle(QLCDNumber.Filled)
        self.lcdOut.setProperty("value", 0.000000000000000)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 360, 37))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spoken Digits", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">Spoken Digits</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Prediction:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btnRecord.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnRecord.setText(QCoreApplication.translate("MainWindow", u"Record", None))
#if QT_CONFIG(shortcut)
        self.btnRecord.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

