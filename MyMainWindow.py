from PyQt6.QtWidgets import QMainWindow
from HeatControlWidget import HeatControlWidget
#from pyqtgraph import PlotWidget, plot
#import pyqtgraph as pg

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.setWindowTitle("Heizungssteuerung")

        self.setCentralWidget(HeatControlWidget(self))
        self.setMinimumSize(1280, 720)