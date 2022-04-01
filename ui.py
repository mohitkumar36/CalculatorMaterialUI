from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.coutOpenPara = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 510)
        MainWindow.setStyleSheet("background-color: rgb(19, 48, 40);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.secLabel = QtWidgets.QLabel(self.centralwidget)
        self.secLabel.setGeometry(QtCore.QRect(0, 0, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.secLabel.setFont(font)
        self.secLabel.setStyleSheet("padding-right: 20px;\n"
                                "color: rgb(157, 223, 219);\n"
                                "background-color: rgb(22, 75, 55);")
        self.secLabel.setText("")
        self.secLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.secLabel.setObjectName("secLabel")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(0, 40, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.mainLabel.setFont(font)
        self.mainLabel.setStyleSheet("padding-right: 15px;\n"
                                "background-color: rgb(22, 75, 55);\n"
                                "border-bottom-right-radius: 20px;\n"
                                "border-bottom-left-radius: 20px;\n"
                                "color: rgb(157, 223, 219);")
        self.mainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear())
        self.clearButton.setEnabled(True)
        self.clearButton.setGeometry(QtCore.QRect(170, 430, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clearButton.setAutoFillBackground(False)
        self.clearButton.setStyleSheet("color: #333;\n"
                                "border: 2px solid #555;\n"
                                "border-radius: 35px;\n"
                                "border-style: outset;\n"
                                "padding: 5px;\n"
                                "color: rgb(192, 223, 219);\n"
                                "background-color: rgb(8, 60, 63);")
        self.clearButton.setFlat(False)
        self.clearButton.setObjectName("clearButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.sevenButton.setFont(font)
        self.sevenButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sevenButton.setStyleSheet("color: #333;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;")
        self.sevenButton.setFlat(False)
        self.sevenButton.setObjectName("sevenButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(250, 270, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.minusButton.setFont(font)
        self.minusButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minusButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.minusButton.setFlat(False)
        self.minusButton.setObjectName("minusButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.oneButton.setFont(font)
        self.oneButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.oneButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.oneButton.setFlat(False)
        self.oneButton.setObjectName("oneButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.equal())
        self.equalButton.setGeometry(QtCore.QRect(250, 430, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.equalButton.setFont(font)
        self.equalButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.equalButton.setStyleSheet("color: #333;\n"
"background-color: rgb(188, 218, 227);\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;")
        self.equalButton.setFlat(False)
        self.equalButton.setObjectName("equalButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("÷"))
        self.divideButton.setGeometry(QtCore.QRect(250, 110, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.divideButton.setFont(font)
        self.divideButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.divideButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.divideButton.setFlat(False)
        self.divideButton.setObjectName("divideButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.fourButton.setFont(font)
        self.fourButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fourButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.fourButton.setFlat(False)
        self.fourButton.setObjectName("fourButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(10, 430, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.zeroButton.setFont(font)
        self.zeroButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.zeroButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.zeroButton.setFlat(False)
        self.zeroButton.setObjectName("zeroButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.percentage())
        self.percentButton.setGeometry(QtCore.QRect(170, 110, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.percentButton.setFont(font)
        self.percentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.percentButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.percentButton.setFlat(False)
        self.percentButton.setObjectName("percentButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("x"))
        self.multiplyButton.setGeometry(QtCore.QRect(250, 190, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiplyButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.multiplyButton.setFlat(False)
        self.multiplyButton.setObjectName("multiplyButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.decimal())
        self.decimalButton.setGeometry(QtCore.QRect(90, 430, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.decimalButton.setFont(font)
        self.decimalButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.decimalButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.decimalButton.setFlat(False)
        self.decimalButton.setObjectName("decimalButton")
        self.acButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.allClear())
        self.acButton.setGeometry(QtCore.QRect(10, 110, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.acButton.setFont(font)
        self.acButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.acButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(12, 255, 154)")
        self.acButton.setFlat(False)
        self.acButton.setObjectName("acButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(250, 350, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.plusButton.setFont(font)
        self.plusButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.plusButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.plusButton.setFlat(False)
        self.plusButton.setObjectName("plusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(90, 270, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.fiveButton.setFont(font)
        self.fiveButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fiveButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.fiveButton.setFlat(False)
        self.fiveButton.setObjectName("fiveButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(90, 190, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.eightButton.setFont(font)
        self.eightButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.eightButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.eightButton.setFlat(False)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(170, 190, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.nineButton.setFont(font)
        self.nineButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.nineButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.nineButton.setFlat(False)
        self.nineButton.setObjectName("nineButton")
        self.paranButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.paranthesis())
        self.paranButton.setGeometry(QtCore.QRect(90, 110, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.paranButton.setFont(font)
        self.paranButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.paranButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background-color: rgb(97, 218, 255);")
        self.paranButton.setFlat(False)
        self.paranButton.setObjectName("paranButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(170, 350, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.threeButton.setFont(font)
        self.threeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.threeButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.threeButton.setFlat(False)
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(90, 350, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.twoButton.setFont(font)
        self.twoButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.twoButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.twoButton.setFlat(False)
        self.twoButton.setObjectName("twoButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(170, 270, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.sixButton.setFont(font)
        self.sixButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sixButton.setStyleSheet("color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 35px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color: rgb(192, 223, 219);\n"
"background-color: rgb(8, 60, 63);")
        self.sixButton.setFlat(False)
        self.sixButton.setObjectName("sixButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self, pressed):
        if self.mainLabel.text() == "0":
            self.mainLabel.setText(pressed)
        else:
                if self.mainLabel.text()[-1] in "÷x-+" and pressed in "÷x-+":
                        self.mainLabel.setText(self.mainLabel.text()[:-1] + pressed)
                else:
                        self.mainLabel.setText(self.mainLabel.text() + pressed)    

    def clear(self):
        self.mainLabel.setText(self.mainLabel.text()[:-1])

    def allClear(self):
        self.mainLabel.setText("0")
        self.secLabel.setText("")

    def percentage(self):
        screen = self.mainLabel.text()
        self.mainLabel.setText(str(int(screen) / 100))

    def paranthesis(self):
        if self.mainLabel.text() == "0":
                self.mainLabel.setText("(")
                self.coutOpenPara += 1
        else:
                if self.coutOpenPara and self.mainLabel.text()[-1].isdigit():
                        self.mainLabel.setText(self.mainLabel.text() + ")")
                        self.coutOpenPara -= 1
                elif self.coutOpenPara and self.mainLabel.text()[-1] == ")":
                        self.mainLabel.setText(self.mainLabel.text() + ")")
                        self.coutOpenPara -= 1
                else:
                        self.mainLabel.setText(self.mainLabel.text() + "(")
                        self.coutOpenPara += 1
        

    def equal(self):
        screen = self.mainLabel.text()
        try:
            tmp = screen.replace("÷", "/")
            tmp = tmp.replace("x", "*")
            answer = eval(tmp)
            self.mainLabel.setText(str(answer))
            self.secLabel.setText(screen)
        except:
            self.mainLabel.setText("ERROR")
            self.secLabel.setText("")

    def decimal(self):
        screen = self.mainLabel.text()
        flag = True #true for we can add decimal
        operations = "+-*/%"
        for c in screen:
            if c in operations:
                flag = True
            elif c == ".":
                flag = False
        if flag:
            self.mainLabel.setText(screen + ".")    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.mainLabel.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.divideButton.setText(_translate("MainWindow", "÷"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.multiplyButton.setText(_translate("MainWindow", "×"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.acButton.setText(_translate("MainWindow", "AC"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.paranButton.setText(_translate("MainWindow", "( )"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.sixButton.setText(_translate("MainWindow", "6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
