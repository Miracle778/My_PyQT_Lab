# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI2_tree.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1123, 675))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget.setObjectName("treeWidget")
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        # 生成键值树
        self.Generate(self.treeWidget)
        self.treeWidget.clicked.connect(self.onClicked)

        self.horizontalLayout.addWidget(self.treeWidget)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget_2.setObjectName("treeWidget_2")
        # 生成值项
        # self.GenerateValue(self.treeWidget_2,self.treeWidget)

        self.horizontalLayout.addWidget(self.treeWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yiitao_UI2"))
        # self.treeWidget.headerItem().setText(0, _translate("MainWindow", "key"))
        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.treeWidget.setSortingEnabled(False)
        # self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "root"))
        # self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "chilid1"))
        # self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "child2"))
        # self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "root2"))
        # self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "name"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "value"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "type"))
        self.menu.setTitle(_translate("MainWindow", "增加"))
        self.menu_2.setTitle(_translate("MainWindow", "修改"))
        self.menu_3.setTitle(_translate("MainWindow", "删除"))
        self.menu_4.setTitle(_translate("MainWindow", "查找"))

    def CreteValueTree(self,value_list):
        # 生成前先删除
        while self.treeWidget_2.takeTopLevelItem(0):
            pass
        for i in range(len(value_list)):
            tmpNode = QTreeWidgetItem(self.treeWidget_2)
            for j in range(3):
                # 有些b‘字节串显示会出错
                tmpNode.setText(j,str(value_list[i][j]))


    def Generate(self,tree):
        # 生成键值树
        tree.setColumnCount(1)
        tree.setHeaderLabels(['Key'])
        root = []
        root_key = ['HKEY_CLASSES_ROOT',
                    'HKEY_CURRENT_USER',
                    'HKEY_LOCAL_MACHINE',
                    'HKEY_USERS',
                    'HKEY_CURRENT_CONFIG']
        # 根节点设置
        for i in range(5):
            tmp = QTreeWidgetItem(tree)
            root.append(tmp)
            root[i].setText(0,root_key[i])

        # test
        child1 = QTreeWidgetItem(root[0])
        # root[0].addChild(child1)
        child1.setText(0,'child')
        child2 = QTreeWidgetItem(child1)
        child2.setText(0,'child2')

        # 用parent == None做判断终止条件
        # print(root[0].parent())


    def onClicked(self):
        currentNode = self.treeWidget.currentItem()
        # test
        # print(currentNode.text(0))
        # path = self.getPath(currentNode)
        # print(path)

        root_index,sub_path = self.getPath(currentNode)
        key_list = self.GenerateKey(root_index,sub_path,0)
        value_list = self.GenerateKey(root_index,sub_path,1)
        print(key_list,'\n',value_list)
        self.CreateKeyTree(currentNode,key_list)
        self.CreteValueTree(value_list)

    def CreateKeyTree(self,currentNode,key_list):
        # 生成前先删除
        currentNode.takeChildren()
        for i in key_list:
            tmpNode = QTreeWidgetItem(currentNode)
            tmpNode.setText(0,i)
        return


    def getPath(self,Qtreeitem):
        # 获取注册表路径
        abspath = []
        while Qtreeitem.parent() != None:
            abspath.append(Qtreeitem.text(0))
            Qtreeitem = Qtreeitem.parent()
        # 根的index
        index = self.treeWidget.indexOfTopLevelItem(Qtreeitem)
        abspath.reverse()
        path_str = '\\'.join(abspath)
        # print(type(path_str))
        return (index,path_str)

    def GenerateKey(self,index,sub_path,flag = 0):
        # 遍历注册表键值,flag = 0枚举键 = 1 枚举值
        import winreg
        root_key = [winreg.HKEY_CLASSES_ROOT,
                    winreg.HKEY_CURRENT_USER,
                    winreg.HKEY_LOCAL_MACHINE,
                    winreg.HKEY_USERS,
                    winreg.HKEY_CURRENT_CONFIG]

        # 设置权限，否则不能改
        try:
            key = winreg.OpenKey(root_key[index],
                                sub_path,
                                0,
                                winreg.KEY_ALL_ACCESS)
            key_list = []
            i = 0
            if flag == 0:
                while 1:
                    name = winreg.EnumKey(key,i)
                    key_list.append(name)
                    i += 1
            elif flag == 1:
                while 1:
                    name,value,type = winreg.EnumValue(key,i)
                    key_list.append((name,value,type))
                    i += 1

        except WindowsError:
            pass
        # except Exception as e:
        #     return e

        try:
            key_list.sort()
            return key_list
        except Exception as e:
            return



# from Yiitao_Scan_ui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())