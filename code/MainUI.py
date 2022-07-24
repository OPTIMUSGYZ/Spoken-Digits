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
        MainWindow.resize(540, 960)
        MainWindow.setMinimumSize(QSize(540, 960))
        MainWindow.setMaximumSize(QSize(540, 960))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnRecord = QPushButton(self.centralwidget)
        self.btnRecord.setObjectName(u"btnRecord")
        self.btnRecord.setGeometry(QRect(100, 301, 300, 65))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRecord.sizePolicy().hasHeightForWidth())
        self.btnRecord.setSizePolicy(sizePolicy)
        self.btnRecord.setMinimumSize(QSize(0, 0))
        self.btnRecord.setMaximumSize(QSize(540, 960))
        self.btnRecord.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"SF Pro Rounded"])
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.btnRecord.setFont(font)
        self.btnRecord.setFocusPolicy(Qt.NoFocus)
        self.btnRecord.setLayoutDirection(Qt.LeftToRight)
        self.btnRecord.setAutoFillBackground(False)
        self.btnRecord.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 0)\n"
"}")
        self.btnRecord.setIconSize(QSize(0, 0))
        self.btnRecord.setAutoDefault(False)
        self.btnRecord.setFlat(False)
        self.lcdOut = QLCDNumber(self.centralwidget)
        self.lcdOut.setObjectName(u"lcdOut")
        self.lcdOut.setGeometry(QRect(350, 428, 104, 104))
        self.lcdOut.setFrameShape(QFrame.NoFrame)
        self.lcdOut.setFrameShadow(QFrame.Plain)
        self.lcdOut.setSmallDecimalPoint(False)
        self.lcdOut.setDigitCount(1)
        self.lcdOut.setMode(QLCDNumber.Hex)
        self.lcdOut.setSegmentStyle(QLCDNumber.Filled)
        self.lcdOut.setProperty("value", 8.000000000000000)
        self.lcdOut.setProperty("intValue", 8)
        self.lblBackground = QLabel(self.centralwidget)
        self.lblBackground.setObjectName(u"lblBackground")
        self.lblBackground.setEnabled(True)
        self.lblBackground.setGeometry(QRect(0, 0, 540, 960))
        self.lblBackground.setPixmap(QPixmap(u"../code/UIBackground.png"))
        self.lblCountDown = QLabel(self.centralwidget)
        self.lblCountDown.setObjectName(u"lblCountDown")
        self.lblCountDown.setGeometry(QRect(413, 309, 40, 50))
        font1 = QFont()
        font1.setFamilies([u"SF Pro Rounded"])
        font1.setPointSize(60)
        self.lblCountDown.setFont(font1)
        self.lblCountDown.setStyleSheet(u"color: rgb(0,0,0)")
        self.lblCountDown.setAlignment(Qt.AlignCenter)
        self.lblMic = QLabel(self.centralwidget)
        self.lblMic.setObjectName(u"lblMic")
        self.lblMic.setEnabled(True)
        self.lblMic.setGeometry(QRect(414, 311, 36, 46))
        self.lblMic.setText(u"")
        self.lblMic.setTextFormat(Qt.AutoText)
        self.lblMic.setPixmap(QPixmap(u"../code/mic.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.lblBackground.raise_()
        self.btnRecord.raise_()
        self.lcdOut.raise_()
        self.lblCountDown.raise_()
        self.lblMic.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 37))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spoken Digits", None))
#if QT_CONFIG(tooltip)
        self.btnRecord.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnRecord.setText(QCoreApplication.translate("MainWindow", u"Click to Record", None))
#if QT_CONFIG(shortcut)
        self.btnRecord.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.lblBackground.setText("")
        self.lblCountDown.setText("")
    # retranslateUi

