# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import UserModel, Base
import hashlib
import chat


engine = create_engine("mysql+pymysql://root:tmc010928@localhost:3306/flask", echo=False)
session = sessionmaker(bind=engine)
session = session()


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 741)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 80, 300, 331))
        self.widget.setStyleSheet("background-color: rgba(235, 235, 235, 235);\n"
                                  "border-radius: 15px")
        self.widget.setObjectName("widget")
        self.user_name = QtWidgets.QLineEdit(self.widget)
        self.user_name.setEnabled(True)
        self.user_name.setGeometry(QtCore.QRect(30, 80, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                     "border-radius: 0px;\n"
                                     "border: 1px solid rgba(0, 0, 0, 0);\n"
                                     "border-bottom-color: rgba(1, 1, 1, 1);\n"
                                     "padding-bottom: -3px;\n"
                                     "color: rgba(1, 1, 1, 1);")
        self.user_name.setDragEnabled(False)
        self.user_name.setClearButtonEnabled(False)
        self.user_name.setObjectName("user_name")
        self.sign_in = QtWidgets.QPushButton(self.widget)
        self.sign_in.setGeometry(QtCore.QRect(30, 250, 241, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.sign_in.setFont(font)
        self.sign_in.setStyleSheet("QPushButton#sign_in{\n"
                                   "background-color:rgba(2,65,118,255);\n"
                                   "color:rgba(255,255,255,200);\n"
                                   "border-radius:5px;\n"
                                   "}\n"
                                   "QPushButton#sign_in:hover{\n"
                                   "background-color:rgba(2,65,118,150);\n"
                                   "color:rgba(255,255,255,200);\n"
                                   "border-radius:5px;\n"
                                   "}\n"
                                   "QPushButton#sign_in:pressed{\n"
                                   "padding-left:5px;\n"
                                   "padding-top:5px;\n"
                                   "background-color:rgba(2,65,118,100);\n"
                                   "}")
        self.sign_in.setObjectName("sign_in")
        self.user_passwd = QtWidgets.QLineEdit(self.widget)
        self.user_passwd.setEnabled(True)
        self.user_passwd.setGeometry(QtCore.QRect(30, 160, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.user_passwd.setFont(font)
        self.user_passwd.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                       "border-radius: 0px;\n"
                                       "border: 1px solid rgba(0, 0, 0, 0);\n"
                                       "border-bottom-color: rgba(1, 1, 1, 1);\n"
                                       "padding-bottom: -3px;\n"
                                       "color: rgba(1, 1, 1, 1);")
        self.user_passwd.setDragEnabled(False)
        self.user_passwd.setClearButtonEnabled(False)
        self.user_passwd.setObjectName("user_passwd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # 输入密码后按回车键执行登录操作
        self.user_passwd.returnPressed.connect(self.login)
        # 单击“登录”按钮执行登录操作
        self.sign_in.clicked.connect(self.login)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
        """
        登入
        :return:
        """
        user_name = self.user_name.text()
        user_passwd = self.user_passwd.text()

        if user_name != "" and user_passwd != "":
            passwd = hashlib.md5(user_passwd.encode()).hexdigest()
            result = session.query(UserModel).filter(UserModel.user_name == user_name).first()
            if result and result.user_passwd == passwd:
                chat_ui = chat.Ui_MainWindow(user_name)  # 创建主窗体对象
                chat_ui.show()  # 显示主窗体
                MainWindow.hide()  # 隐藏当前的登录窗体
            else:
                self.user_name.setText("")  # 清空用户名文本
                self.user_passwd.setText("")  # 清空密码文本框
                QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入用户名和密码！', QMessageBox.Ok)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_name.setPlaceholderText(_translate("MainWindow", "用户名："))
        self.sign_in.setText(_translate("MainWindow", "登入"))
        self.user_passwd.setPlaceholderText(_translate("MainWindow", "密码："))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建 PyQt 设计的窗体对象
    ui.setupUi(MainWindow)  # 调用 PyQt 窗体的方法对窗体对象进行初始化
    MainWindow.show()
    sys.exit(app.exec_())  # 程序关闭时退出进程

