from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import generateMap as Gm
import inputManual as Im
import main


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Networked CASTLE Mission Deployment Tool")
        self.initWindow()
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.move(30, 20)



    def initWindow(self):
        self.setWindowTitle(self.tr("Networked CASTLE MDT - Mission Deployment Tool"))
        self.setFixedSize(1600,900)
        self.buttonUI()


    def buttonUI(self):
        button1 = QtWidgets.QPushButton(self.tr("Create Mission - Manual Input"), clicked=lambda: click1())
        button2 = QtWidgets.QPushButton(self.tr("Create Mission - On The Map"))
        button3 = QtWidgets.QPushButton(self.tr("Analyze The Mission"))
        button4 = QtWidgets.QPushButton(self.tr("Animate The Mission"))

        button1.setFixedSize(300, 50)
        button2.setFixedSize(300, 50)
        button3.setFixedSize(300, 50)
        button4.setFixedSize(300, 50)

        button1.setStyleSheet("background-color: #E3D8BC ;font-size:18px;font-family:Calibri;")
        button2.setStyleSheet("background-color: #E3D8BC ;font-size:18px;font-family:Calibri;")
        button3.setStyleSheet("background-color: #E3D8BC ;font-size:18px;font-family:Calibri;")
        button4.setStyleSheet("background-color: #E3D8BC ;font-size:18px;font-family:Calibri;")

        button3.setDisabled(True)
        button4.setDisabled(True)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)

        button_container = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(button_container)
        vlay.setSpacing(10)
        vlay.addStretch()
        vlay.addWidget(button1)
        vlay.addWidget(button2)
        vlay.addWidget(button3)
        vlay.addWidget(button4)
        vlay.addStretch()
        lay.addWidget(button_container)
        Gm.createMainMap(lay)

        def click1():

            button1.setDisabled(True)
            button2.setDisabled(True)
            Im.showManual()




    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)
        painter.drawRect(437, 98, 1053, 704)
        painter.drawRect(436, 97, 1055, 706)

