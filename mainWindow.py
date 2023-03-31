import itertools
import json
import time

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtGui import QPixmap,QMovie
from PyQt5.QtWidgets import QLabel, QMessageBox, QFileDialog
import inputDialog as Id
import analyzeTool as At
import calculateParameters as Cp
import nameSensor as Ns
import nameImpact as Ni
import nameLauncher as Nl
import discardTool as Dt
import threading
import time
import generateMap as Gm
import tableDialog as Td
import os
import animation
import csv
import table_csv



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Networked CASTLE MDT (Mission Deployment Tool)")
        MainWindow.setWindowTitle("Networked CASTLE MDT (Mission Deployment Tool ver_01.21)")
        MainWindow.setMinimumSize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 224);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QLabel(MainWindow)
        self.label1.setPixmap(self.pixmap1)
        self.label1.resize(self.pixmap1.width(), self.pixmap1.height())
        self.label1.move(30, 20)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openInput())
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 181, 28))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: #FFE4BB")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openMapMission())
        self.pushButton_2.setGeometry(QtCore.QRect(80, 160, 181, 28))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: #FFE4BB")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openAnalysis())
        self.pushButton_3.setGeometry(QtCore.QRect(80, 200, 181, 28))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: #FFE4BB")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.questionResult())
        self.pushButton_4.setGeometry(QtCore.QRect(80, 240, 181, 28))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: #FFE4BB")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 290, 211, 521))
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 441))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.listWidget2 = QtWidgets.QListWidget(self.frame)
        self.listWidget2.setGeometry(QtCore.QRect(10, 29, 191, 441))
        self.listWidget2.setStyleSheet("background-color: #FFFFFF;")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.listWidget2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget2.setLineWidth(50)
        self.listWidget2.setObjectName("listWidget2")
        self.listWidget2.setFont(font)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame, clicked = lambda: Td.createTable())
        self.pushButton_5.setGeometry(QtCore.QRect(40, 480, 61, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.warningReset())
        self.pushButton_6.setGeometry(QtCore.QRect(110, 480, 61, 28))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 80, 1191, 741))
        self.frame_2.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(2, 2, 1211, 751))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 211, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        Gm.createMainMap(self.horizontalLayout)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(17, 79, 26, 26))
        self.pushButton_10.setStyleSheet("background-color: rgba(0, 0, 0, 50);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_0 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 0, 1200, 750))
        self.pushButton_0.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.locateSensor())
        self.pushButton_11.setGeometry(QtCore.QRect(15, 170, 40, 40))
        self.pushButton_11.setStyleSheet("background-color: #ffffff;")
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_11.setTabletTracking(False)
        self.pushButton_11.setAutoFillBackground(True)
        self.pushButton_11.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_sensor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setToolTip('Set Sensor Post Point')
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.locateLauncher())
        self.pushButton_12.setGeometry(QtCore.QRect(15, 210, 40, 40))
        self.pushButton_12.setStyleSheet("background-color: #ffffff;")
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_12.setAutoFillBackground(True)
        self.pushButton_12.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon_artillery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setToolTip('Set Firing Point')
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.locateImpact())
        self.pushButton_13.setGeometry(QtCore.QRect(15, 250, 40, 40))
        self.pushButton_13.setStyleSheet("background-color: #ffffff;")
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_13.setAutoFillBackground(True)
        self.pushButton_13.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon_impact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setToolTip('Set impact Point')
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(40, 65, 80, 80))
        self.pushButton_14.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openDiscard())
        self.pushButton_15.setGeometry(QtCore.QRect(55, 170, 40, 40))
        self.pushButton_15.setStyleSheet("background-color: #ffffff;")
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_15.setAutoFillBackground(True)
        self.pushButton_15.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("cancelicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setAutoDefault(False)
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setToolTip('Discard Element')
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.readytoAnalyze())
        self.pushButton_16.setGeometry(QtCore.QRect(55, 210, 40, 40))
        self.pushButton_16.setStyleSheet("background-color: #ffffff;")
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_16.setAutoFillBackground(True)
        self.pushButton_16.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon5)
        self.pushButton_16.setAutoDefault(False)
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setToolTip('Confirm')
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.questionFinish())
        self.pushButton_18.setGeometry(QtCore.QRect(55, 250, 40, 40))
        self.pushButton_18.setStyleSheet("background-color: #ffffff;")
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_18.setAutoFillBackground(True)
        self.pushButton_18.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("finish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon7)
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setToolTip('Finalize the Mission')
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(15, 310, 80, 320))
        self.listWidget.setStyleSheet("background-color: #FFFFFF;")
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(100)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(font)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(110, 130, 111, 51))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setLineWidth(2)
        self.label_10.setMidLineWidth(1)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(110, 190, 111, 71))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setLineWidth(2)
        self.label_11.setMidLineWidth(1)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(110, 270, 99, 110))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setLineWidth(2)
        self.label_12.setMidLineWidth(1)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(110, 315, 99, 70))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_13.setLineWidth(2)
        self.label_13.setMidLineWidth(1)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_17.setGeometry(QtCore.QRect(90, 225, 80, 80))
        self.pushButton_17.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("arrow1.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon6)
        self.pushButton_17.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_17.setFlat(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.saveMisson())
        self.pushButton_19.setGeometry(QtCore.QRect(1135, 82, 40, 40))
        self.pushButton_19.setStyleSheet("background-color: #ffffff;")
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_19.setAutoFillBackground(True)
        self.pushButton_19.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon7)
        self.pushButton_19.setAutoDefault(False)
        self.pushButton_19.setFlat(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setToolTip('Save Mission')
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.importMission())
        self.pushButton_20.setGeometry(QtCore.QRect(1135, 135, 40, 40))
        self.pushButton_20.setStyleSheet("background-color: #ffffff;")
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_20.setAutoFillBackground(True)
        self.pushButton_20.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon8)
        self.pushButton_20.setAutoDefault(False)
        self.pushButton_20.setFlat(False)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setToolTip('Import Mission File')


        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_18.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_19.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_14.hide()
        self.pushButton_17.hide()
        self.label_13.hide()
        self.pushButton_16.setDisabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.pushButton_4.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.movie = QMovie("mousecircle.gif")
        self.label_12.setMovie(self.movie)
        self.movie.start()

    def animate(self):
        self.pushButton_20.hide()
        self.pushButton_19.hide()
        self.pushButton_18.hide()
        self.pushButton_17.hide()
        self.pushButton_16.hide()
        self.pushButton_15.hide()
        self.pushButton_14.hide()
        self.pushButton_13.hide()
        self.pushButton_12.hide()
        self.pushButton_11.hide()
        self.pushButton_10.hide()
        self.pushButton_0.hide()
        self.listWidget.hide()
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setEnabled(True)
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().deleteLater()
        animation.press_it(self.horizontalLayout)

    def saveMisson(self):
        file_filter = 'Text File (*.txt)'
        response = QFileDialog.getSaveFileName(
            parent=None,
            caption='Select a data file',
            directory='mission.txt',
            filter=file_filter,
            initialFilter='Text File (*.txt)'
        )

        file1 = open(response[0], "w")
        file1.writelines(str(Cp.name_sensor) + '\n' + str(Cp.actual_sensor_coord) + '\n'
                        + str(Cp.name_launch) + '\n' + str(Cp.actual_launch_coord) + '\n'
                         + str(Cp.name_impact) + '\n'  + str(Cp.actual_impact_coord))
        file1.close()

    def importMission(self):
        file_filter = 'Text File (*.txt)'
        response = QFileDialog.getOpenFileName(
            parent=None,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Text File (*.txt)'
        )

        try:
            with open(response[0]) as f:
                lines = f.readlines()
            i = 0
            for line in lines:
                line = line.replace(']', '')
                line = line.replace('[', '')
                line = line.replace("'", '')
                line = line.replace('\n', '')
                if i == 0:
                    Cp.name_sensor = list(line.split(", "))
                elif i == 1:
                    temp_s = list(line.split(", "))
                    t_s = []
                    t_ss = []
                    for s in temp_s:
                        s = float(s)
                        t_s.append(s)
                    while True:
                        t_ss.append(t_s[0])
                        t_ss.append(t_s[1])
                        Cp.actual_sensor_coord.append(t_ss)
                        t_s.pop(0)
                        t_s.pop(0)
                        t_ss = []
                        if len(t_s) == 0:
                            break

                elif i == 2:
                    Cp.name_launch = list(line.split(", "))
                elif i == 3:
                    temp_l = list(line.split(", "))
                    t_l = []
                    t_ll = []
                    for l in temp_l:
                        l = float(l)
                        t_l.append(l)
                    while True:
                        t_ll.append(t_l[0])
                        t_ll.append(t_l[1])
                        Cp.actual_launch_coord.append(t_ll)
                        t_l.pop(0)
                        t_l.pop(0)
                        t_ll = []
                        if len(t_l) == 0:
                            break
                elif i == 4:
                    Cp.name_impact = list(line.split(", "))
                elif i == 5:
                    temp_i = list(line.split(", "))
                    t_i = []
                    t_ii = []
                    for k in temp_i:
                        k = float(k)
                        t_i.append(k)
                    while True:
                        t_ii.append(t_i[0])
                        t_ii.append(t_i[1])
                        Cp.actual_impact_coord.append(t_ii)
                        t_i.pop(0)
                        t_i.pop(0)
                        t_ii = []
                        if len(t_i) == 0:
                            break
                i = i + 1

            for j in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(j).widget().deleteLater()
            Gm.updateSeconder(self.horizontalLayout)
            self.pushButton_0.hide()
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setEnabled(True)
        except FileNotFoundError:
            pass
        for i in Cp.name_sensor:
            self.listWidget2.addItem(i + '  ' + str(Cp.actual_sensor_coord[Cp.name_sensor.index(i)]))
        for j in Cp.name_launch:
            self.listWidget2.addItem(j + '  ' + str(Cp.actual_launch_coord[Cp.name_launch.index(j)]))
        for m in Cp.name_impact:
            self.listWidget2.addItem(m + '  ' + str(Cp.actual_impact_coord[Cp.name_impact.index(m)]))

    def updateMap(self):
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().deleteLater()
        Gm.createUpdatedMap(self.horizontalLayout)

    def openDiscard(self):
        Dt.showDiscardTool()
        self.listWidget.clear()
        self.listWidget.addItems(Cp.name_sensor)
        self.listWidget.addItems(Cp.name_launch)
        self.listWidget.addItems(Cp.name_impact)

    def readyNext(self):
        self.pushButton_3.setEnabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_16.setDisabled(True)
        self.pushButton_18.setDisabled(True)
        self.pushButton_19.setEnabled(True)
        self.listWidget.clear()
        for i in Cp.name_sensor:
            self.listWidget2.addItem(i + '  ' + str(Cp.actual_sensor_coord[Cp.name_sensor.index(i)]))
        for j in Cp.name_launch:
            self.listWidget2.addItem(j + '  ' + str(Cp.actual_launch_coord[Cp.name_launch.index(j)]))
        for m in Cp.name_impact:
            self.listWidget2.addItem(m + '  ' + str(Cp.actual_impact_coord[Cp.name_impact.index(m)]))

    def readytoAnalyze(self):
        self.pushButton_0.hide()
        self.pushButton_17.hide()
        self.label_13.hide()
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_16.setDisabled(True)
        self.updateMap()
        if len(Cp.actual_sensor_coord) > 0 and len(Cp.actual_launch_coord) > 0 and len(Cp.actual_impact_coord) > 0:
            self.pushButton_18.setEnabled(True)
        else:
            self.pushButton_18.setDisabled(True)

    def checkIfClickedSensor(self):
        a = len(Cp.actual_sensor_coord)
        while True:
            if a<len(Cp.actual_sensor_coord):
                self.pushButton_10.show()
                self.pushButton_0.show()
                self.pushButton_14.hide()
                self.label_10.hide()
                self.label_11.hide()
                self.label_12.hide()
                self.pushButton_17.show()
                self.label_13.show()
                self.pushButton_16.setEnabled(True)
                self.listWidget.clear()
                self.listWidget.addItems(Cp.name_sensor)
                self.listWidget.addItems(Cp.name_launch)
                self.listWidget.addItems(Cp.name_impact)
                if len(Cp.actual_sensor_coord) == 0 and len(Cp.actual_launch_coord) == 0 and len(
                        Cp.actual_impact_coord) == 0:
                    self.pushButton_15.setDisabled(True)
                    break
                else:
                    break
            else:
                if Cp.joker_constant==0:
                    self.pushButton_11.setDisabled(True)
                    self.pushButton_12.setDisabled(True)
                    self.pushButton_13.setDisabled(True)
                    break
                else:
                    pass

    def checkIfClickedLauncher(self):
        a = len(Cp.actual_launch_coord)
        while True:
            if a<len(Cp.actual_launch_coord):
                self.pushButton_10.show()
                self.pushButton_0.show()
                self.pushButton_14.hide()
                self.label_10.hide()
                self.label_11.hide()
                self.label_12.hide()
                self.pushButton_17.show()
                self.label_13.show()
                self.pushButton_16.setEnabled(True)
                self.listWidget.clear()
                self.listWidget.addItems(Cp.name_sensor)
                self.listWidget.addItems(Cp.name_launch)
                self.listWidget.addItems(Cp.name_impact)
                if len(Cp.actual_sensor_coord) == 0 and len(Cp.actual_launch_coord) == 0 and len(
                        Cp.actual_impact_coord) == 0:
                    self.pushButton_15.setDisabled(True)
                    break
                else:
                    break
            else:
                if Cp.joker_constant == 0:
                    self.pushButton_11.setDisabled(True)
                    self.pushButton_12.setDisabled(True)
                    self.pushButton_13.setDisabled(True)
                    break
                else:
                    pass
    def checkIfClickedImpact(self):
        a = len(Cp.actual_impact_coord)
        while True:
            if a<len(Cp.actual_impact_coord):
                self.pushButton_10.show()
                self.pushButton_0.show()
                self.pushButton_14.hide()
                self.label_10.hide()
                self.label_11.hide()
                self.label_12.hide()
                self.pushButton_17.show()
                self.label_13.show()
                self.pushButton_16.setEnabled(True)
                self.listWidget.clear()
                self.listWidget.addItems(Cp.name_sensor)
                self.listWidget.addItems(Cp.name_launch)
                self.listWidget.addItems(Cp.name_impact)
                if len(Cp.actual_sensor_coord) == 0 and len(Cp.actual_launch_coord) == 0 and len(
                        Cp.actual_impact_coord) == 0:
                    self.pushButton_15.setDisabled(True)
                    break
                else:
                    break
            else:
                if Cp.joker_constant == 0:
                    self.pushButton_11.setDisabled(True)
                    self.pushButton_12.setDisabled(True)
                    self.pushButton_13.setDisabled(True)
                    break
                else:
                    pass

    def locateSensor(self):
        Cp.joker_constant=1
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_0.show()
        k=len(Cp.name_sensor)
        l=len(Cp.actual_sensor_coord)
        Ns.showNameDialog()
        if k<len(Cp.name_sensor):
            self.pushButton_0.hide()
            self.pushButton_10.hide()
            self.pushButton_14.show()
            self.label_10.show()
            self.label_11.show()
            self.label_12.show()
            t1=threading.Thread(target=self.checkIfClickedSensor)
            t1.start()
        else:
            self.pushButton_11.setEnabled(True)
            self.pushButton_12.setEnabled(True)
            self.pushButton_13.setEnabled(True)
            self.pushButton_10.show()
            self.pushButton_0.hide()
            Cp.joker_constant=0
            if len(Cp.actual_sensor_coord)>0 or len(Cp.actual_launch_coord)>0 or len(Cp.actual_impact_coord)>0:
                self.pushButton_15.setEnabled(True)
            else:
                pass

    def locateLauncher(self):
        Cp.joker_constant=2
        self.pushButton_11.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_0.show()
        k = len(Cp.name_launch)
        l = len(Cp.actual_launch_coord)
        Nl.showNameDialog()
        if k < len(Cp.name_launch):
            self.pushButton_0.hide()
            self.pushButton_10.hide()
            self.pushButton_14.show()
            self.label_10.show()
            self.label_11.show()
            self.label_12.show()
            t2=threading.Thread(target=self.checkIfClickedLauncher)
            t2.start()
        else:
            self.pushButton_12.setEnabled(True)
            self.pushButton_11.setEnabled(True)
            self.pushButton_13.setEnabled(True)
            self.pushButton_10.show()
            self.pushButton_0.hide()
            Cp.joker_constant=0
            if len(Cp.actual_sensor_coord)>0 or len(Cp.actual_launch_coord)>0 or len(Cp.actual_impact_coord)>0:
                self.pushButton_15.setEnabled(True)
            else:
                pass

    def locateImpact(self):
        Cp.joker_constant=3
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_0.show()
        k = len(Cp.name_impact)
        l = len(Cp.actual_impact_coord)
        Ni.showNameDialog()
        if k < len(Cp.name_impact):
            self.pushButton_0.hide()
            self.pushButton_10.hide()
            self.pushButton_14.show()
            self.label_10.show()
            self.label_11.show()
            self.label_12.show()
            t3=threading.Thread(target=self.checkIfClickedImpact)
            t3.start()
        else:
            self.pushButton_13.setEnabled(True)
            self.pushButton_11.setEnabled(True)
            self.pushButton_12.setEnabled(True)
            self.pushButton_10.show()
            self.pushButton_0.hide()
            Cp.joker_constant=0
            if len(Cp.actual_sensor_coord)>0 or len(Cp.actual_launch_coord)>0 or len(Cp.actual_impact_coord)>0:
                self.pushButton_15.setEnabled(True)
            else:
                pass

    def openMapMission(self):
        Cp.resetAll()
        self.pushButton_0.hide()
        self.pushButton.setDisabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_20.setDisabled(True)

    def openInput(self):
        self.pushButton_0.hide()
        self.pushButton_2.setDisabled(True)
        k=len(Cp.name_sensor)
        l=len(Cp.name_launch)
        m=len(Cp.name_impact)
        self.pushButton.setDisabled(True)
        self.pushButton_20.setDisabled(True)
        Id.showInputDialog()
        if k<len(Cp.name_sensor) and l<len(Cp.name_launch) and m<len(Cp.name_impact):
            self.pushButton_3.setEnabled(True)
            for j in reversed(range(self.horizontalLayout.count())):
                self.horizontalLayout.itemAt(j).widget().deleteLater()
            Gm.updateSeconder(self.horizontalLayout)
        else:
            self.pushButton.setEnabled(True)
            self.pushButton_0.show()
            pass
        for i in Cp.name_sensor:
            self.listWidget2.addItem(i + '  ' + str(Cp.actual_sensor_coord[Cp.name_sensor.index(i)]))
        for j in Cp.name_launch:
            self.listWidget2.addItem(j + '  ' + str(Cp.actual_launch_coord[Cp.name_launch.index(j)]))
        for m in Cp.name_impact:
            self.listWidget2.addItem(m + '  ' + str(Cp.actual_impact_coord[Cp.name_impact.index(m)]))

    def openAnalysis(self):
        self.pushButton_0.hide()
        self.pushButton_3.setDisabled(True)
        At.showAnalyzeTool()
        if len(Cp.event_array)>0:
            self.pushButton_4.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setDisabled(True)
            pass

    def warningReset(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Do you want to reset all missions and events ?  If you click 'Yes', they are going to be permanently deleted !")
        msg.setWindowTitle("WARNING")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.accepted.connect(self.resetMission)
        retval = msg.exec_()

    def questionFinish(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you want to complete the mission ?")
        msg.setWindowTitle("Question")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.accepted.connect(self.readyNext)
        retval = msg.exec_()

    def questionResult(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Do you want to calculate and animate the results of events ? That process may take up to few minutes, please be patient !")
        msg.setWindowTitle("Question")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.accepted.connect(table_csv.initiateTable)
        msg.accepted.connect(self.animate)
        retval = msg.exec_()


    def resetMission(self):
        Cp.resetAll()
        Cp.joker_constant=0
        self.pushButton_10.show()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_14.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_18.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_19.setDisabled(True)
        self.pushButton_20.setEnabled(True)
        self.pushButton_20.show()
        self.pushButton_19.show()
        self.pushButton_18.show()
        self.pushButton_16.show()
        self.pushButton_15.show()
        self.pushButton_13.show()
        self.pushButton_12.show()
        self.pushButton_11.show()
        self.pushButton_10.show()
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_0.show()
        self.listWidget.show()
        self.listWidget.clear()
        self.listWidget2.clear()
        Gm.last_list.clear()
        Gm.last_list_float.clear()
        Gm.cumulative_coordinates.clear()
        Gm.temp_coordinates.clear()
        Gm.temp_cumulative.clear()
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().deleteLater()
        Gm.createMainMap(self.horizontalLayout)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Networked CASTLE MDT (Mission Deployment Tool ver_0.0.1)"))
        self.pushButton.setText(_translate("MainWindow", "Create Mission - Manual Input"))
        self.pushButton_2.setText(_translate("MainWindow", "Create Mission - On the Map"))
        self.pushButton_3.setText(_translate("MainWindow", "Create Event"))
        self.pushButton_4.setText(_translate("MainWindow", "Calculate and Show Results"))
        self.label.setText(_translate("MainWindow", "The Mission Summary"))
        self.pushButton_5.setText(_translate("MainWindow", "Table View"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_10.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("Form", "<CLICK> this icon to mark the coordinate"))
        self.label_11.setText(_translate("Form", "After placing circle marker, please <CLICK> on the circle icon that is replaced into the map"))
        self.label_13.setText(_translate("Form","<CLICK> this button to verify and visualize the selected coordinates"))


