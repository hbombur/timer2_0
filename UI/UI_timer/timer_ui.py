import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(400, 300)
        main_window.setStyleSheet("background-color: rgb(173, 203, 181);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_game = QtWidgets.QPushButton(self.centralwidget)
        self.btn_game.setGeometry(QtCore.QRect(125, 130, 150, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btn_game.setFont(font)
        self.btn_game.setStyleSheet("background-color: rgb(124, 195, 152);")
        self.btn_game.setObjectName("btn_game")
        self.btn_watch_youtube = QtWidgets.QPushButton(self.centralwidget)
        self.btn_watch_youtube.setGeometry(QtCore.QRect(125, 170, 150, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_watch_youtube.setFont(font)
        self.btn_watch_youtube.setStyleSheet("background-color: rgb(124, 195, 152);")
        self.btn_watch_youtube.setObjectName("btn_watch_youtube")
        self.lbl_greeting = QtWidgets.QLabel(self.centralwidget)
        self.lbl_greeting.setGeometry(QtCore.QRect(0, 80, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lbl_greeting.setFont(font)
        self.lbl_greeting.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_greeting.setObjectName("lbl_greeting")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Таймер 2.0"))
        self.btn_game.setText(_translate("MainWindow", "Играть"))
        self.btn_watch_youtube.setText(_translate("MainWindow", "Смотреть YouTube"))
        self.lbl_greeting.setText(_translate("MainWindow", "Привет, Дружище!!!"))

async def init_ui():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(main_window)
    main_window.show()
    return app






