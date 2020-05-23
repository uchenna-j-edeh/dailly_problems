import os
print(os.__file__)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class CustomDialog(QDialog):
    def __init__(self, *args, **kwargs):
        supper(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Hello!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App") 
        
        #self.setCentralWidget(tabs)
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)
        #dlg = QDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()