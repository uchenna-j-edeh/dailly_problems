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

        layout = QHBoxLayout()
        
        for i in ['red', 'blue', 'green', 'yellow', 'orange']:
            layout.addWidget(Color(i))        

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()