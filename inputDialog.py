# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import calculateParameters as Cp
import mainWindow as Mw
import threading
import itertools
import discardTool as Dt
from PyQt5.QtCore import Qt
import generateMap as Gm


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 550)
        Dialog.setStyleSheet("background-color: #EDFFFE")
        Dialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 500, 341, 32))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet("background-color: rgb(227, 216, 188);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 361, 471))
        self.frame.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(160, 70, 181, 22))
        self.comboBox.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["<Select Element/Event>", "Sensor Post", "Launcher Point", "Impact Point"])
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 171, 181, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 220, 181, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 120, 181, 22))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked=lambda: getInfo())
        self.pushButton.setGeometry(QtCore.QRect(80, 270, 93, 28))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame, clicked =lambda: self.discardElement())
        self.pushButton_2.setGeometry(QtCore.QRect(190, 270, 93, 28))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 320, 341, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(4, 5, 331, 131))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.questionFinish)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.cancelDialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEdit_5.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)

        temp_sensor_coord=[]
        temp_cumulative_sensor=[]
        cum_sensor_coord=[]
        last_sensor_float=[]
        last_sensor_coord=[]
        temp_launch_coord=[]
        temp_cumulative_launch=[]
        cum_launch_coord=[]
        last_launch_float=[]
        last_launch_coord=[]
        temp_impact_coord=[]
        temp_cumulative_impact=[]
        cum_impact_coord=[]
        last_impact_float=[]
        last_impact_coord=[]

        self.comboBox.activated[str].connect(self.onSelected_1)
        self.lineEdit.textChanged.connect(self.lineActive)
        self.lineEdit_2.textChanged.connect(self.lineActive_2)
        self.lineEdit_5.textChanged.connect(self.lineActive_5)


        def getInfo():

            global last_sensor_coord, last_launch_coord, last_impact_coord

            # printing the form information

            if self.comboBox.currentText() == "Sensor Post":

                temp_sensor_coord.append(float(self.lineEdit.text()))
                temp_sensor_coord.append(float(self.lineEdit_2.text()))
                temp_cumulative_sensor.append(temp_sensor_coord)
                cum_sensor_coord.append(str(temp_cumulative_sensor[-1]))

                j = 0
                for i in cum_sensor_coord:
                    a = cum_sensor_coord[j].split(', ')
                    a[0] = float(a[0].replace('[', ''))
                    a[-1] = float(a[-1].replace(']', ''))
                    last_sensor_float.append(a)
                    j = j + 1
                last_sensor_coord = list(
                    last_sensor_float for last_sensor_float,
                                          _ in itertools.groupby(last_sensor_float))
                temp_sensor_coord.pop(-1)
                temp_sensor_coord.pop(0)
                Cp.actual_sensor_coord.append(last_sensor_coord[-1])
                Cp.actual_sensor_coord = list(
                    Cp.actual_sensor_coord for Cp.actual_sensor_coord,
                                               _ in itertools.groupby(Cp.actual_sensor_coord))

                Cp.name_sensor.append(str(self.lineEdit_5.text()))


            elif self.comboBox.currentText() == "Launcher Point":

                temp_launch_coord.append(float(self.lineEdit.text()))
                temp_launch_coord.append(float(self.lineEdit_2.text()))
                temp_cumulative_launch.append(temp_launch_coord)
                cum_launch_coord.append(str(temp_cumulative_launch[-1]))
                j = 0
                for i in cum_launch_coord:
                    a = cum_launch_coord[j].split(', ')
                    a[0] = float(a[0].replace('[', ''))
                    a[-1] = float(a[-1].replace(']', ''))
                    last_launch_float.append(a)
                    j = j + 1
                last_launch_coord = list(last_launch_float for last_launch_float,
                                                               _ in itertools.groupby(last_launch_float))
                temp_launch_coord.pop(-1)
                temp_launch_coord.pop(0)
                Cp.actual_launch_coord.append(last_launch_coord[-1])
                Cp.actual_launch_coord = list(
                    Cp.actual_launch_coord for Cp.actual_launch_coord, _ in itertools.groupby(Cp.actual_launch_coord))

                Cp.name_launch.append(str(self.lineEdit_5.text()))

            elif self.comboBox.currentText() == "Impact Point":

                temp_impact_coord.append(float(self.lineEdit.text()))
                temp_impact_coord.append(float(self.lineEdit_2.text()))
                temp_cumulative_impact.append(temp_impact_coord)
                cum_impact_coord.append(str(temp_cumulative_impact[-1]))

                j = 0
                for i in cum_impact_coord:
                    a = cum_impact_coord[j].split(', ')
                    a[0] = float(a[0].replace('[', ''))
                    a[-1] = float(a[-1].replace(']', ''))
                    last_impact_float.append(a)
                    j = j + 1
                last_impact_coord = list(last_impact_float for last_impact_float,
                                                               _ in itertools.groupby(last_impact_float))
                temp_impact_coord.pop(-1)
                temp_impact_coord.pop(0)
                Cp.actual_impact_coord.append(last_impact_coord[-1])
                Cp.actual_impact_coord = list(
                Cp.actual_impact_coord for Cp.actual_impact_coord, _ in itertools.groupby(Cp.actual_impact_coord))

                Cp.name_impact.append(str(self.lineEdit_5.text()))


            elif self.comboBox.currentIndex() == 0:
                print("Please select element to add")

            self.showSummary()

            if Cp.name_sensor or Cp.name_impact or Cp.name_launch:
                self.pushButton_2.setEnabled(True)
            else:
                self.pushButton_2.setDisabled(True)

            self.pushButton.setDisabled(True)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_5.clear()

    def questionFinish(self):
        msg = QMessageBox()
        msg.setWindowFlags(Qt.WindowStaysOnTopHint)
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you want to complete the mission ?")
        msg.setWindowTitle("Question")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.accepted.connect(self.okDialog)
        retval = msg.exec_()

    def okDialog(self):
        Cp.ok=1


    def cancelDialog(self):
        Cp.ok=0
        Cp.actual_sensor_coord.clear()
        Cp.actual_impact_coord.clear()
        Cp.actual_launch_coord.clear()
        Cp.name_launch.clear()
        Cp.name_impact.clear()
        Cp.name_sensor.clear()

    def discardElement(self):
        Dt.showDiscardTool()
        self.showSummary()

    def showSummary(self):
        self.label_10.setText("\n"" Last Element Added: {0} \n".format(
            self.comboBox.currentText()) + "\n"" Number of Added Sensor Element:  " +
                              str(len(Cp.actual_sensor_coord))
                              + "\n" + "\n" " Number of Added Launch Event:  "
                              + str(len(Cp.actual_launch_coord)) +
                              "\n" + "\n" " Number of Added Impact Event: "
                              + str(len(Cp.actual_impact_coord)))

    def lineActive(self, text):
        if len(text) >= 1:
            self.lineEdit_2.setEnabled(True)
        else:
            self.lineEdit_2.setDisabled(True)

    def lineActive_2(self,text):
        if len(text) >= 1:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setDisabled(True)

    def lineActive_5(self,text):
        if len(text) >= 1:
            self.lineEdit.setEnabled(True)
        else:
            self.lineEdit.setDisabled(True)


    def onSelected_1(self,val):
        if val == "Sensor Post":
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_5.clear()
            self.lineEdit_5.setEnabled(True)
        elif val == "Launcher Point":
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_5.clear()
            self.lineEdit_5.setEnabled(True)
        elif val == "Impact Point":
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_5.clear()
            self.lineEdit_5.setDisabled(False)
        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_5.clear()
            self.lineEdit.setDisabled(True)
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_5.setDisabled(True)
            self.pushButton.setDisabled(True)
            self.pushButton_2.setDisabled(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Manual Coordinate Input Dialog"))
        self.label.setText(_translate("Dialog", "Select Element to Add"))
        self.label_2.setText(_translate("Dialog", "Enter Latitude"))
        self.label_3.setText(_translate("Dialog", "Enter Longitude"))
        self.label_8.setText(_translate("Dialog", "Enter Mission Information"))
        self.label_9.setText(_translate("Dialog", "Assign Name"))
        self.pushButton.setText(_translate("Dialog", "Add Element +"))
        self.pushButton_2.setText(_translate("Dialog", "Discard Element -"))
        self.label_10.setText(_translate("Dialog", "\n"
                                                   " Last Element Added:\n"
                                                   "\n"
                                                   " Number of Added Sensor Element:\n"
                                                   "\n"
                                                   " Number of Added Firing Event:\n"
                                                   "\n"
                                                   " Number of Added Impact Event:"))


def showInputDialog():
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()

