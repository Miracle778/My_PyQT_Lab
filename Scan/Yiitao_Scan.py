#coding=utf-8

#WlAN网卡名字'Intel(R) Dual Band Wireless-AC 7265'

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Yiitao_Scan_ui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())