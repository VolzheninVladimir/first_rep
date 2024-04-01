import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QFileDialog, QWidget




class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

    def show_menu(self):
        self.menu = menu_window()
        self.menu.button_load.clicked.connect(self.load_image)
        self.menu.button_exit.clicked.connect(self.exit_window)
        self.menu.show()

    def show_image(self, file_path):
        self.image = image_window(file_path)
        self.image.show()

    def exit_window(self):
        sys.exit()

    def load_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.jpg *.png)")
        file_name = file_dialog.getOpenFileName()
        self.show_image(str(file_name[0]))


class menu_window(QMainWindow):
    def __init__(self):
        super(menu_window, self).__init__()
        uic.loadUi('window.ui', self)


class image_window(QMainWindow):
    def __init__(self, file_path):
        super(image_window,self).__init__()
        self.setWindowTitle("Photo Viewer")
        self.pixmap = QPixmap(file_path)
        self.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())

        self.label = QLabel(self)

        self.pixmap = QPixmap(file_path)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show_menu()
    sys.exit(app.exec())