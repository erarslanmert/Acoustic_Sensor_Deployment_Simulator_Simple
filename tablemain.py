import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import QtGui
import calculateParameters as Cp

def createTable():
    class YuTextFrame(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('Results of Analysis')
            vbox = QVBoxLayout()

            # add table
            table = QTableWidget(self)
            table.setColumnCount(20)

            table.rowCount()
            # set table header


            # add data
            row = table.rowCount()

            vbox.addWidget(table)
            self.setLayout(vbox)
            self.setGeometry(100, 100, 1205, 781)


        def addTableRow(self, table, row_data):
            row = table.rowCount()
            table.setRowCount(row + 1)
            col = 0
            for item in row_data:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col = col + 1


    app2 = QApplication(sys.argv)
    frame = YuTextFrame()
    frame.show()
    app2.exec_()

