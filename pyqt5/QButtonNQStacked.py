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

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(layout)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow', 'indigo', 'cyan', 'magenta']):
            btn = QPushButton(str(color))
            btn.pressed.connect( lambda n=n: layout.setCurrentIndex(n))
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pagelayout) # sets layout on the widget
        
        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()