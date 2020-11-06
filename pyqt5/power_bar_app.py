from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar_widget import PowerBar

"""
We don’t need to create a QMainWindow since any widget 
without a parent is a window in it’s own right. 
Our custom PowerBar widget will appear as any normal window.
"""

app = QtWidgets.QApplication([])
# volume = PowerBar(10)
# volume = PowerBar(["#5e4fa2","#3288bd","#66c2a5","#abdda4","#e6f598","#ffffbf","#fee08b","#fdae61","#f46d43","#d53e4f","#9e0142"])
# volume.show()
bar=PowerBar(["#49006a","#7a0177","#ae017e","#dd3497","#f768a1","#fa9fb5","#fcc5c0","#fde0dd","#fff7f3"])
bar.setBarPadding(2)
bar.setBarSolidPercent(0.9)
bar.setBackgroundColor('gray')
bar.show()
app.exec_()