# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI2_tree.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# 2018/12/6 line 226 至添加工具栏获取值，待实现写入注册表

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import time
import winreg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 680)
        # self.MainWindow.setVisible(False)
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

        # 生成根键值树
        self.Generate(self.treeWidget)
        self.treeWidget.clicked.connect(self.onClicked)

        self.horizontalLayout.addWidget(self.treeWidget)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget_2.setObjectName("treeWidget_2")
        # 生成值项
        # self.GenerateValue(self.treeWidget_2,self.treeWidget)

        self.horizontalLayout.addWidget(self.treeWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        # 工具栏
        addAction = QAction("增加", MainWindow)
        editAction = QAction("修改",MainWindow)
        deleteAction = QAction("删除",MainWindow)
        # findAction = QAction("查询",MainWindow)
        defenceAction = QAction("冰河检测",MainWindow)
        DefenceAction = QAction("添加防护",MainWindow)
        removeDefenceAction = QAction('解除防护',MainWindow)
        RunCheckAction = QAction('启动项修复',MainWindow)

        addAction.triggered.connect(self.on_addAction_triggered)
        editAction.triggered.connect(self.on_editAction_triggered)
        deleteAction.triggered.connect(self.on_deleteAction_triggered)
        # findAction.triggered.connect(self.on_findAction_triggered)
        defenceAction.triggered.connect(self.defenceBH)
        DefenceAction.triggered.connect(self.Defence)
        removeDefenceAction.triggered.connect(self.removeDefence)
        RunCheckAction.triggered.connect(self.RunCheck)

        # MainWindow对象才有addToolBar等
        toolbar = MainWindow.addToolBar('aa')
        toolbar.addAction(addAction)
        toolbar.addAction(editAction)
        toolbar.addAction(deleteAction)
        # toolbar.addAction(findAction)
        toolbar.addAction(defenceAction)
        toolbar.addAction(DefenceAction)
        toolbar.addAction(removeDefenceAction)
        toolbar.addAction(RunCheckAction)

        # 防护与解除防护退出线程信号量
        self.flags = 0


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yiitao_Registry"))
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
        # self.menu.setTitle(_translate("MainWindow", "增加"))
        # self.menu_2.setTitle(_translate("MainWindow", "修改"))
        # self.menu_3.setTitle(_translate("MainWindow", "删除"))
        # self.menu_4.setTitle(_translate("MainWindow", "查找"))



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

        # # test
        # child1 = QTreeWidgetItem(root[0])
        # # root[0].addChild(child1)
        # child1.setText(0,'child')
        # child2 = QTreeWidgetItem(child1)
        # child2.setText(0,'child2')

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

    def on_addAction_triggered(self):
        currNode = self.treeWidget.currentItem()

        name,okPressed = QInputDialog.getText(self.MainWindow,
                                              "name",
                                              "name:",
                                              QLineEdit.Normal,
                                              "")
        if okPressed:
            value,okPressed = QInputDialog.getText(self.MainWindow,
                                                   'value',
                                                   'value:',
                                                   QLineEdit.Normal,
                                                   '')
            # 测试错误 传参str 与 b 不能转换，测试用type重名
            # try:
            #     print(type(value))
            # except Exception as e:
            #     print(e)

            if okPressed:
                type,okPressed = QInputDialog.getText(self.MainWindow,
                                                      'type',
                                                      'type:',
                                                      QLineEdit.Normal,
                                                      '')
        root_index,sub_key = self.getPath(currNode)
        try:
            self.operateRegisty(root_index,sub_key,0,(name,value,type))
        except Exception as e:
            print('add函数: ',e)

    def operateRegisty(self,index,sub_path,flag,arg=None):
        #flag  0,1,2 add,edit,delete
        import winreg
        root_key = [winreg.HKEY_CLASSES_ROOT,
                    winreg.HKEY_CURRENT_USER,
                    winreg.HKEY_LOCAL_MACHINE,
                    winreg.HKEY_USERS,
                    winreg.HKEY_CURRENT_CONFIG]
        type_list = {}
        try:
            key = winreg.OpenKey(root_key[index],
                                sub_path,
                                0,
                                winreg.KEY_ALL_ACCESS)
            if flag == 0:
                winreg.SetValueEx(key,arg[0],0,int(arg[2]),arg[1])
            elif flag == 1:
                winreg.DeleteValue(key,arg[3])
                winreg.SetValueEx(key,arg[0],0,int(arg[2]),arg[1])
            elif flag == 2:
                # print(arg[0])
                winreg.DeleteValue(key,arg[0])
        except Exception as e:
            print('操作注册表函数：',e)




    def on_editAction_triggered(self):
        try:
            keyCurrNode = self.treeWidget.currentItem()
            valueCurrNode = self.treeWidget_2.currentItem()
            old_name = valueCurrNode.text(0)
            name, okPressed = QInputDialog.getText(self.MainWindow,
                                                   "name",
                                                   "name:",
                                                   QLineEdit.Normal,
                                                   "")
            if okPressed:
                value, okPressed = QInputDialog.getText(self.MainWindow,
                                                        'value',
                                                        'value:',
                                                        QLineEdit.Normal,
                                                        '')
                if okPressed:
                    type, okPressed = QInputDialog.getText(self.MainWindow,
                                                           'type',
                                                           'type:',
                                                           QLineEdit.Normal,
                                                           '')
            root_index,sub_key = self.getPath(keyCurrNode)
            self.operateRegisty(root_index,sub_key,1,(name,value,type,old_name))
        except Exception as e:
            print('edit函数: ',e)
    def on_deleteAction_triggered(self):
        try:
            keyCurrNode = self.treeWidget.currentItem()
            valueCurrNode = self.treeWidget_2.currentItem()
            old_name = valueCurrNode.text(0)
            root_index,sub_key = self.getPath(keyCurrNode)
            self.operateRegisty(root_index,sub_key,2,(old_name,))

        except Exception as e:
            print('删除函数:',e)
    # def on_findAction_triggered(self):
    #     pass

    def defenceBH(self):
        import winreg
        default = {'name':'',
                   'value':"%SystemRoot%\\system32\\NOTEPAD.EXE %1",
                   'type':winreg.REG_EXPAND_SZ}
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,
                             r"txtfile\\shell\\open\\command",
                             0,
                             winreg.KEY_ALL_ACCESS)
        value,reg_type = winreg.QueryValueEx(key,'')
        if value == default['value'] and reg_type == default['type']:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('冰河检测')
            msgBox.setText("没中冰河病毒")
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('冰河检测')
            msgBox.setText("txt关联应用被修改，可能中冰河病毒\n\t已恢复为默认值")
            winreg.SetValueEx(key,default['name'],0,default['type'],default['value'])
            msgBox.exec_()

    def Defence(self):
        try:
            keyCurrNode = self.treeWidget.currentItem()
            valueCurrNode = self.treeWidget_2.currentItem()
            value_name = valueCurrNode.text(0)
            root_index,sub_key = self.getPath(keyCurrNode)
            import winreg
            root_key = [winreg.HKEY_CLASSES_ROOT,
                        winreg.HKEY_CURRENT_USER,
                        winreg.HKEY_LOCAL_MACHINE,
                        winreg.HKEY_USERS,
                        winreg.HKEY_CURRENT_CONFIG]
            key = winreg.OpenKey(root_key[root_index],
                                 sub_key,
                                 0,
                                 winreg.KEY_ALL_ACCESS)
            value,reg_type = winreg.QueryValueEx(key,value_name)
            default = {'name':value_name,
                       'value':value,
                       'type':reg_type}
            #   加线程监听
            self.flags = 1
            t = threading.Thread(target=self.Listen,args=(default,key))
            t.start()
            # t.join()
            # time.sleep(5)


        except Exception as e:
            print("防护函数:",e)

    def Listen(self,default,key):
        while self.flags == 1:

            try:
                value,reg_type = winreg.QueryValueEx(key,default['name'])
                if value != default['value'] or reg_type != default['type']:
                    # 线程里不让MessageBox,错误
                    # msgBox = QMessageBox()
                    # msgBox.setWindowTitle("防护注册表")
                    winreg.SetValueEx(key,default['name'],0,default['type'],default['value'])
                    print("检测到有程序正在修改注册表\n\t已恢复默认值")
                    # exec_阻塞进程错误
                    # msgBox.exec()
            except Exception as e:
                print("Listen线程",e)
                # msgBox = QMessageBox()
                # msgBox.setWindowTitle("防护注册表")
                winreg.SetValueEx(key, default['name'], 0, default['type'], default['value'])
                print("检测到有程序正在修改注册表\n\t已恢复默认值")
                # msgBox.exec_()

            time.sleep(3)


    def removeDefence(self):
        try:
            keyCurrNode = self.treeWidget.currentItem()
            valueCurrNode = self.treeWidget_2.currentItem()
            value_name = valueCurrNode.text(0)
            root_index,sub_key = self.getPath(keyCurrNode)
            root_key = [winreg.HKEY_CLASSES_ROOT,
                        winreg.HKEY_CURRENT_USER,
                        winreg.HKEY_LOCAL_MACHINE,
                        winreg.HKEY_USERS,
                        winreg.HKEY_CURRENT_CONFIG]
            key = winreg.OpenKey(root_key[root_index],
                                sub_key,
                                0,
                                winreg.KEY_ALL_ACCESS)
            self.flags = 0

        except Exception as e:
            print("解除防护函数:",e)

    def RunCheck(self):
        # 开机自启项检查
        path = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'

        defaut = {'':(None,1),'ctfmon':('C:\\WINDOWS\\system32\\ctfmon.exe',1)}
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                path,
                                0,
                                winreg.KEY_ALL_ACCESS)
            # 返回(name,value,type)列表
            value_list = self.GenerateKey(1,path,1)
            print(value_list)
            for value in value_list:
                # name不对，直接删除
                if value[0] not in defaut.keys():
                    winreg.DeleteValue(key,value[0])
                    print('启动项删除成功')
                #named对，值、类型不对修复
                elif value[1] != defaut[value[0]][0] or value[2] != defaut[value[0]][1]:
                    winreg.SetValueEx(key,value[0],
                                      0,
                                      defaut[value[0]][1],
                                      defaut[value[0]][0])
                    print('启动项修复')
            Msg = QMessageBox()
            Msg.setWindowTitle('启动项检查')
            Msg.setText('启动项修复完成')
            Msg.exec_()

        except Exception as e:
            print(e)



# from Yiitao_Scan_ui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # mainWindow.setVisible(False)

    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())