import os
print(os.__file__)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")     

        layout = QStackedLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('purple'))
        layout.addWidget(Color('orange'))
        layout.addWidget(Color('yellow'))

        #layout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(layout) # sets layout on the widget
        
        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()