from mainWindow import *
from inputDialog import *
from generateMap import *
from calculateParameters import *
from analyzeTool import *
from animation import *
import sys
import tablemain as tb
import threading
# --------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

