# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading
import qrc.rec
import chat


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 741)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 240, 300, 231))
        self.widget.setStyleSheet("background-color: rgba(235, 235, 235, 235);\n"
                                  "border-radius: 15px")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "border-radius: 0px;\n"
                                    "border: 1px solid rgba(0, 0, 0, 0);\n"
                                    "border-bottom-color: rgba(1, 1, 1, 1);\n"
                                    "padding-bottom: -3px;\n"
                                    "color: rgba(1, 1, 1, 1);")
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                                      "background-color:rgba(2,65,118,255);\n"
                                      "color:rgba(255,255,255,200);\n"
                                      "border-radius:5px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:hover{\n"
                                      "background-color:rgba(2,65,118,150);\n"
                                      "color:rgba(255,255,255,200);\n"
                                      "border-radius:5px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:pressed{\n"
                                      "padding-left:5px;\n"
                                      "padding-top:5px;\n"
                                      "background-color:rgba(2,65,118,100);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 10, 31, 21))
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 捕获回车事件
        self.lineEdit.returnPressed.connect(self.set_user)

        # 捕获点击事件
        self.pushButton.clicked.connect(self.set_user)

    def set_user(self):
        """
        获取名称
        :return:
        """
        # 用户名称
        name = self.lineEdit.text()
        if name:
            c = chat.Ui_MainWindow(name)
            c.show()
            MainWindow_login.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "id："))
        self.pushButton.setText(_translate("MainWindow", "join"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_login = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow_login)  # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow_login.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
