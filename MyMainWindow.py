from PyQt6.QtWidgets import QMainWindow

from HeatControlWidget import HeatControlWidget

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)


        self.setWindowTitle("Graph")

        self.setCentralWidget(HeatControlWidget(self))
        #self.setCentralWidget(GraphWidget(self))


        self.setMinimumSize(1280, 720)

