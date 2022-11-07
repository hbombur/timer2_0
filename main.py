from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def win_init(app):
    available_screen_width = app.primaryScreen().availableGeometry().width()
    available_screen_height = app.primaryScreen().availableGeometry().height()
    scr_width = 350
    scr_height = 200
    scr_shift_x = int((available_screen_width / 2) - (scr_width / 2))
    scr_shift_y = int((available_screen_height / 2) - (scr_height / 2))
    return scr_shift_x, scr_shift_y, scr_width, scr_height


def timer():
    app = QApplication(sys.argv)
    scr_shift_x, scr_shift_y, scr_width, scr_height = win_init(app)
    window = QMainWindow()

    window.setWindowTitle("Таймер 2.0")
    window.setGeometry(scr_shift_x, scr_shift_y, scr_width, scr_height)

    btn_game = QtWidgets.QPushButton(window)
    btn_game.setText("Играть")
    print(btn_game.width())
    print(scr_width)
    print(scr_height)
    print(int(3.9))
    x = (scr_width/2 - btn_game.width()/2)
    y = (scr_height/3) - 20
    btn_game.move(int(x), int(y))
    btn_game.width()

    btn_youtube = QtWidgets.QPushButton(window)
    btn_youtube.setText("Смотреть YouTube")
    btn_youtube.move(int(scr_width/2) - int(btn_game.width()/2), int(scr_height/3*2) + 20)
    btn_youtube.width()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    timer()