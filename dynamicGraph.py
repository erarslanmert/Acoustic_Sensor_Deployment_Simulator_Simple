from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

sensor=['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10']

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle("Your Title Here", color="b", size="10pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "10px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        for sens in sensor:
            self.plot(hour, temperature_1, sens, 'r')


    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen)

        """self.graphWidget = pg.PlotWidget()
        self.graphWidget.setYRange(0,100)
        self.setCentralWidget(self.graphWidget)
        a=[]
        b=[]
        c=[]
        for i in range(100):
            a.append(i/10)
            c.append(55)
            if i == 47:
                b.append(67)
            elif i==48:
                b.append(33)
            else:
                b.append(50)
        self.x = a
        self.y = b
        self.z = c

        self.graphWidget.setBackground('white')

        pen = pg.mkPen(color=(255, 0, 0))
        pen_2 = pg.mkPen(color=(0, 255, 255))

        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        self.data_line_2 = self.graphWidget.plot(self.x, self.y, pen=pen_2)

        # ... init continued ...
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()


    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 0.1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(self.y[-1])  # Add a new random value.

        self.data_line.setData(self.x, self.y)
        self.data_line_2.setData(self.x, self.z )# Update the data."""




app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())