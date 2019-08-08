# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Yiitao_Scan_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    threads = []
    open_port = []
    close_port = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 50, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 50, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 101, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 210, 251, 181))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 110, 111, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(560, 120, 61, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 110, 31, 41))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(700, 120, 71, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 210, 91, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(560, 210, 201, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(450, 300, 121, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(630, 300, 121, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 400, 111, 41))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(60, 410, 91, 31))
        # self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(202, 410, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 350, 81, 21))
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(630, 350, 46, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Scan)
        # self.pushButton_2.clicked.connect(self.Sort)
        self.pushButton_3.clicked.connect(self.Clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yiitao_Scan"))
        self.label.setText(_translate("MainWindow", "本地主机名"))
        self.label_2.setText(_translate("MainWindow", "本地主机IP"))
        self.label_3.setText(_translate("MainWindow", "开放端口报告"))
        self.label_4.setText(_translate("MainWindow", "扫描端口区间"))
        self.label_5.setText(_translate("MainWindow", "到"))
        self.label_6.setText(_translate("MainWindow", "输入IP地址"))
        self.radioButton.setText(_translate("MainWindow", "connect扫描"))
        self.radioButton_2.setText(_translate("MainWindow", "SYN扫描"))
        self.pushButton.setText(_translate("MainWindow", "开始扫描"))
        # self.pushButton_2.setText(_translate("MainWindow", "排序"))
        self.pushButton_3.setText(_translate("MainWindow", "清空"))
        self.label_7.setText(_translate("MainWindow", "线程数"))

    def Connect(self,ipaddr,port,port_right,blank,pid):
        #多线程
        for i in range(port,port_right+1,blank):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((ipaddr,i))
                self.open_port.append(i)
                self.textEdit.append('{}:open'.format(i))
            except:
                self.close_port.append(i)
                # self.textEdit.append('{}:close'.format(i))
                # if blank == 1:
                #     self.textEdit.append('{}:close'.format(i))
            finally:
                sock.close()

        if self.spinBox.value() == pid + 1:
            self.textEdit.append('扫描结束')
        return


    def Scan_connect(self,ipaddr,port_left,port_right):
        thread_num = self.spinBox.value()
        for i in range(thread_num):
            t = threading.Thread(target=self.Connect,args=(ipaddr,port_left+i,port_right,thread_num,i))
            self.threads.append(t)
        for i in range(thread_num):
            self.threads[i].start()
        # for i in threads:
        #     i.join()


    def Scan_SYN(self,ipaddr,port_left,port_right):
        pass

    def Scan(self):
        ipaddr = self.lineEdit_5.text()
        ip_list = ipaddr.split('.')

        #验证ip合法性
        if len(ip_list) != 4:
            self.lineEdit_5.setText("ip地址不合法,请重新输入")
            return
        if len(ip_list) == 4:
            for i in ip_list:
                try:
                    temp = int(i)
                except:
                    self.lineEdit_5.setText("ip地址不合法,请重新输入")
                    return
                if temp > 255 or temp < 0:
                    self.lineEdit_5.setText("ip字段超出范围")
                    return

         #验证port
        try:
            port_left = int(self.lineEdit_3.text())
            port_right = int(self.lineEdit_4.text())
        except:
            self.textEdit.setText("端口输入不合法")
            return
        if port_left < 0 or port_right > 65535:
            self.textEdit.setText("端口没在范围")
            return

        # addr = (ipaddr,port_left)   #带端口的地址


        if self.radioButton.isChecked():            #connect扫描
            self.Scan_connect(ipaddr,port_left,port_right)

        if self.radioButton_2.isChecked():
            self.Scan_SYN(ipaddr,port_left,port_right)

        # print(len(self.open_port))

    # def Sort(self):
    #     str_format = '{}:open'
    #     str = ''
    #     for i in sort(self.open_port):
    #         str = str + (str_format.format(i))
    #     self.textEdit.setText(str)

    def Clear(self):
        self.open_port = []
        self.close_port = []
        self.textEdit.setText('')
