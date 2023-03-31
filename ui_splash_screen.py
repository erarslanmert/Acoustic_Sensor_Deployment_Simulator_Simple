# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenXOZdTu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(340, 357)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
                                            "    border-radius: 150px;\n"
                                            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(190, 0, 0, 0), stop:0.750 rgba(190, 0, 0, 255));\n"
                                            "}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 301, 301))
        self.circularBg.setStyleSheet("QFrame{\n"
                                      "    border-radius: 150px;\n"
                                      "    background-color: rgba(255, 110, 110, 120);\n"
                                      "}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
                                     "    border-radius: 135px;\n"
                                     "    background-color: rgb(236, 236, 236)\n"
                                     "}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 211, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelLoadingInfo = QtWidgets.QLabel(self.layoutWidget)
        self.labelLoadingInfo.setMinimumSize(QtCore.QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelLoadingInfo.setFont(font)
        self.labelLoadingInfo.setStyleSheet("QLabel{\n"
                                            "    border-radius: 10px;    \n"
                                            "    background-color: rgb(93, 93, 154);\n"
                                            "    color: #FFFFFF;\n"
                                            "    margin-left: 40px;\n"
                                            "    margin-right: 40px;\n"
                                            "}")
        self.labelLoadingInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoadingInfo.setObjectName("labelLoadingInfo")
        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)
        self.labelTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
                                      "color: rgb(0, 0, 0)")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
                                           "color: rgb(0, 0, 0)")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("background-color: none;\n"
                                        "color:rgb(231, 231, 231)")
        self.labelCredits.setText("")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.gridLayout.addWidget(self.labelCredits, 4, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelLoadingInfo.setText(_translate("SplashScreen", "opening..."))
        self.labelTitle.setText(_translate("SplashScreen",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Networked CASLTE</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mission Deployment Tool</span></p></body></html>"))
        self.labelPercentage.setText(_translate("SplashScreen",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">        0</span><span style=\" font-size:16pt; vertical-align:super;\">%</span></p></body></html>"))



