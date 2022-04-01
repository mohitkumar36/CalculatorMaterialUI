# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)
import del_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(331, 510)
        MainWindow.setStyleSheet(u"background-color: rgb(19, 48, 40);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.secLabel = QLabel(self.centralwidget)
        self.secLabel.setObjectName(u"secLabel")
        self.secLabel.setGeometry(QRect(0, 0, 331, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.secLabel.setFont(font)
        self.secLabel.setStyleSheet(u"padding-right: 25px;\n"
"color: rgb(157, 223, 219);\n"
"background-color: rgb(22, 75, 55);")
        self.secLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.mainLabel = QLabel(self.centralwidget)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setGeometry(QRect(0, 40, 331, 61))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(30)
        self.mainLabel.setFont(font1)
        self.mainLabel.setStyleSheet(u"padding-right: 15px;\n"
"background-color: rgb(22, 75, 55);\n"
"border-bottom-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(157, 223, 219);")
        self.mainLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setEnabled(True)
        self.clearButton.setGeometry(QRect(170, 430, 71, 71))
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearButton.setAutoFillBackground(False)
        self.clearButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.clearButton.setFlat(False)
        self.sevenButton = QPushButton(self.centralwidget)
        self.sevenButton.setObjectName(u"sevenButton")
        self.sevenButton.setGeometry(QRect(10, 190, 71, 71))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(22)
        self.sevenButton.setFont(font2)
        self.sevenButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sevenButton.setStyleSheet(u"color: #333;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;")
        self.sevenButton.setFlat(False)
        self.minusButton = QPushButton(self.centralwidget)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setGeometry(QRect(250, 270, 71, 71))
        self.minusButton.setFont(font2)
        self.minusButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minusButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.minusButton.setFlat(False)
        self.oneButton = QPushButton(self.centralwidget)
        self.oneButton.setObjectName(u"oneButton")
        self.oneButton.setGeometry(QRect(10, 350, 71, 71))
        self.oneButton.setFont(font2)
        self.oneButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.oneButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.oneButton.setFlat(False)
        self.equalButton = QPushButton(self.centralwidget)
        self.equalButton.setObjectName(u"equalButton")
        self.equalButton.setGeometry(QRect(250, 430, 71, 71))
        self.equalButton.setFont(font2)
        self.equalButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.equalButton.setStyleSheet(u"color: #333;\n"
"background-color: rgb(188, 218, 227);\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;")
        self.equalButton.setFlat(False)
        self.divideButton = QPushButton(self.centralwidget)
        self.divideButton.setObjectName(u"divideButton")
        self.divideButton.setGeometry(QRect(250, 110, 71, 71))
        self.divideButton.setFont(font2)
        self.divideButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.divideButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.divideButton.setFlat(False)
        self.fourButton = QPushButton(self.centralwidget)
        self.fourButton.setObjectName(u"fourButton")
        self.fourButton.setGeometry(QRect(10, 270, 71, 71))
        self.fourButton.setFont(font2)
        self.fourButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fourButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.fourButton.setFlat(False)
        self.zeroButton = QPushButton(self.centralwidget)
        self.zeroButton.setObjectName(u"zeroButton")
        self.zeroButton.setGeometry(QRect(10, 430, 71, 71))
        self.zeroButton.setFont(font2)
        self.zeroButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.zeroButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.zeroButton.setFlat(False)
        self.percentButton = QPushButton(self.centralwidget)
        self.percentButton.setObjectName(u"percentButton")
        self.percentButton.setGeometry(QRect(170, 110, 71, 71))
        self.percentButton.setFont(font2)
        self.percentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.percentButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.percentButton.setFlat(False)
        self.multiplyButton = QPushButton(self.centralwidget)
        self.multiplyButton.setObjectName(u"multiplyButton")
        self.multiplyButton.setGeometry(QRect(250, 190, 71, 71))
        self.multiplyButton.setFont(font2)
        self.multiplyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.multiplyButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.multiplyButton.setFlat(False)
        self.decimalButton = QPushButton(self.centralwidget)
        self.decimalButton.setObjectName(u"decimalButton")
        self.decimalButton.setGeometry(QRect(90, 430, 71, 71))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(28)
        self.decimalButton.setFont(font3)
        self.decimalButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.decimalButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.decimalButton.setFlat(False)
        self.acButton = QPushButton(self.centralwidget)
        self.acButton.setObjectName(u"acButton")
        self.acButton.setGeometry(QRect(10, 110, 71, 71))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(22)
        font4.setBold(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.acButton.setFont(font4)
        self.acButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.acButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(12, 255, 154)")
        self.acButton.setFlat(False)
        self.plusButton = QPushButton(self.centralwidget)
        self.plusButton.setObjectName(u"plusButton")
        self.plusButton.setGeometry(QRect(250, 350, 71, 71))
        self.plusButton.setFont(font2)
        self.plusButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.plusButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.plusButton.setFlat(False)
        self.fiveButton = QPushButton(self.centralwidget)
        self.fiveButton.setObjectName(u"fiveButton")
        self.fiveButton.setGeometry(QRect(90, 270, 71, 71))
        self.fiveButton.setFont(font2)
        self.fiveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fiveButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.fiveButton.setFlat(False)
        self.eightButton = QPushButton(self.centralwidget)
        self.eightButton.setObjectName(u"eightButton")
        self.eightButton.setGeometry(QRect(90, 190, 71, 71))
        self.eightButton.setFont(font2)
        self.eightButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.eightButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.eightButton.setFlat(False)
        self.nineButton = QPushButton(self.centralwidget)
        self.nineButton.setObjectName(u"nineButton")
        self.nineButton.setGeometry(QRect(170, 190, 71, 71))
        self.nineButton.setFont(font2)
        self.nineButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.nineButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.nineButton.setFlat(False)
        self.paranButton = QPushButton(self.centralwidget)
        self.paranButton.setObjectName(u"paranButton")
        self.paranButton.setGeometry(QRect(90, 110, 71, 71))
        self.paranButton.setFont(font2)
        self.paranButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.paranButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.paranButton.setFlat(False)
        self.threeButton = QPushButton(self.centralwidget)
        self.threeButton.setObjectName(u"threeButton")
        self.threeButton.setGeometry(QRect(170, 350, 71, 71))
        self.threeButton.setFont(font2)
        self.threeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.threeButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.threeButton.setFlat(False)
        self.twoButton = QPushButton(self.centralwidget)
        self.twoButton.setObjectName(u"twoButton")
        self.twoButton.setGeometry(QRect(90, 350, 71, 71))
        self.twoButton.setFont(font2)
        self.twoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.twoButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.twoButton.setFlat(False)
        self.sixButton = QPushButton(self.centralwidget)
        self.sixButton.setObjectName(u"sixButton")
        self.sixButton.setGeometry(QRect(170, 270, 71, 71))
        self.sixButton.setFont(font2)
        self.sixButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sixButton.setStyleSheet(u"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.sixButton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.secLabel.setText("")
        self.mainLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.sevenButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.minusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.oneButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.equalButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.divideButton.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.fourButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.zeroButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.percentButton.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.multiplyButton.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.decimalButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.acButton.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.plusButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.fiveButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.eightButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nineButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.paranButton.setText(QCoreApplication.translate("MainWindow", u"( )", None))
        self.threeButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.twoButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.sixButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
    # retranslateUi

