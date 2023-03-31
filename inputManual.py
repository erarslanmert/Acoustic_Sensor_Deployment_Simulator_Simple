from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QWidget)
from PyQt5 import QtGui
import userInterface as Ui

class Dialog(QDialog):


    def __init__(self):
        super(Dialog, self).__init__()

        # setting window title
        self.setWindowTitle("Manual Input Dialog")

        self.setFixedSize(400,600)
        # setting geometry to the window
        self.setWindowIcon(QtGui.QIcon("icon_sensor.png"))

        # creating a group box
        self.formGroupBox = QGroupBox("Please Enter Mission Information")
        self.formGroupBox.setStyleSheet(''' font-size: 12px; ''')

        # creating spin box to select age
        self.ageSpinBar = QSpinBox()

        # creating combo box to select degree
        self.degreeComboBox = QComboBox()

        # adding items to the combo box
        self.degreeComboBox.addItems(["Sensor Coordinates", "Launch Coordinates", "Impact Coordinates"])

        # creating a line edit
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit2 = QLineEdit()
        self.nameLineEdit3 = QLineEdit()

        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.buttonBox.setStyleSheet('''background-color: #E3D8BC ; font-size: 14px; ''')

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)



        # creating a vertical layout
        mainLayout = QVBoxLayout()


        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        self.add_button = QPushButton(self.tr("Add Element"))
        self.add_button.setStyleSheet(''' font-size: 10px; ''')
        self.change_button = QPushButton(self.tr("Change element"))
        self.change_button.setStyleSheet('''font-size: 10px; ''')
        self.add_button.setFixedSize(100,30)
        self.change_button.setFixedSize(100,30)
        self.button_container2 = QWidget()
        vlay = QHBoxLayout(self.button_container2)
        vlay.setSpacing(5)

        vlay.addWidget(self.add_button)
        vlay.addWidget(self.change_button)


        mainLayout.addWidget(self.button_container2)
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)


    # get info method called when form is accepted
    def getInfo(self):
        # printing the form information
        print("Degree : {0}".format(self.degreeComboBox.currentText()))
        print("Person Name : {0}".format(self.nameLineEdit.text()))
        print("Person Name : {0}".format(self.nameLineEdit2.text()))
        print("Person Name : {0}".format(self.nameLineEdit3.text()))


        # closing the window
        self.close()

    # creat form method
    def createForm(self):
        # creating a form layout
        layout = QFormLayout()
        layout_sensor = QFormLayout()
        layout_launch = QFormLayout()

        # adding rows

        # for degree and adding combo box
        layout.addRow(QLabel("Mission Element Type"), self.degreeComboBox)

        # for name and adding input text


        # for age and adding spin box


        if str(self.degreeComboBox.currentText()) == "Sensor Coordinates":
            layout_sensor.addRow(QLabel("Enter Sensor Latitude"), self.nameLineEdit)
            layout_sensor.addRow(QLabel("Enter Sensor Longitude"), self.nameLineEdit2)
            self.formGroupBox.setLayout(layout_sensor)
        elif str(self.degreeComboBox.currentText()) == "Launch Coordinates":

            layout_launch.addRow(QLabel("Enter Sensor Latitude"), self.nameLineEdit3)
            self.formGroupBox.setLayout(layout_launch)
        else:
            self.formGroupBox.setLayout(layout)



def showManual():

    dialog = Dialog()
    dialog.show()
    dialog.exec_()

    """def getInfo(self):
        # printing the form information
        print("Element Added : {0}".format(self.comboBox.currentText()))
        print("Element : {0}".format(self.lineEdit.text()))
        print("Element Latitude : {0}".format(self.lineEdit_2.text()))
        print("Element Longitude : {0}".format(self.lineEdit_3.text()))
        print("Speed Parameter : {0}".format(self.comboBox_2.currentText()))
        print("Speed Value m/s : {0}".format(self.lineEdit_4.text()))
        print("Time Parameter : {0}".format(self.comboBox_3.currentText()))
        print("Time Value Seconds : {0}".format(self.lineEdit_5.text()))"""