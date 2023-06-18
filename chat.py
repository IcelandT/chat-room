# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import sys
import threading
from PyQt5.QtWidgets import *
import socket
import cv2
import re
import time
import qrc.picture
import qrc.res
import qrc.text
import qrc.user


class Ui_MainWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self)

        self.user_name = name

        # ----------------------
        #     socket config
        # ----------------------
        self.host = "127.0.0.1"
        self.port = 9989
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.tcp_client.connect((self.host, self.port))
            self.tcp_client.send(f'name={self.user_name}'.encode("utf-8"))
        except Exception as e:
            print('TCP连接失败 =>', e)
            self.tcp_client.close()
            sys.exit(0)

        self.threading = list()

        self.start_work()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 773)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 10, 1271, 701))
        self.widget.setStyleSheet("background-color: rgb(39, 42, 55);\n"
                                  "border-radius: 20px")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/user/test/user.png"))
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(100, 30, 891, 641))
        self.widget_2.setStyleSheet("background-color: rgb(50, 54, 68);\n"
                                    "border-radius: 12px")
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 580, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    color: rgba(235, 235, 235, 245);\n"
                                    "    background-color: rgb(66, 70, 86);\n"
                                    "    border-radius: 15px;\n"
                                    "    padding: 10px\n"
                                    "}\n"
                                    "QLineEdit:focus{\n"
                                    "    border: 1px solid gray;\n"
                                    "}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(710, 580, 41, 41))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                                      "background-color:rgba(0,0,0,0);\n"
                                      "color:rgba(255,255,255,200);\n"
                                      "border-radius:5px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:hover{\n"
                                      "background-color:rgba(25,25,25,55);\n"
                                      "color:rgba(255,255,255,200);\n"
                                      "border-radius:5px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:pressed{\n"
                                      "padding-left:5px;\n"
                                      "padding-top:5px;\n"
                                      "background-color:rgba(2,65,118,100);\n"
                                      "}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/test/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(36, 36))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 580, 41, 41))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
                                        "background-color:rgba(0,0,0,0);\n"
                                        "color:rgba(255,255,255,200);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "QPushButton#pushButton_2:hover{\n"
                                        "background-color:rgba(25,25,25,55);\n"
                                        "color:rgba(255,255,255,200);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "QPushButton#pushButton_2:pressed{\n"
                                        "padding-left:5px;\n"
                                        "padding-top:5px;\n"
                                        "background-color:rgba(2,65,118,100);\n"
                                        "}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/text/test/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 851, 541))
        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(13)
        self.textBrowser.setFont(font2)
        self.textBrowser.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 580, 71, 41))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
                                        "background-color:rgba(0,0,0,0);\n"
                                        "color:rgba(255,255,255,200);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "QPushButton#pushButton_3:hover{\n"
                                        "background-color:rgba(25,25,25,55);\n"
                                        "color:rgba(255,255,255,200);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "QPushButton#pushButton_3:pressed{\n"
                                        "padding-left:5px;\n"
                                        "padding-top:5px;\n"
                                        "background-color:rgba(2,65,118,100);\n"
                                        "}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/test/response-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.send_message)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(1020, 30, 221, 641))
        self.widget_3.setStyleSheet("background-color: rgb(50, 54, 68);\n"
                                    "border-radius: 12px")
        self.widget_3.setObjectName("widget_3")
        self.on_line_user = QtWidgets.QTextBrowser(self.widget_3)
        self.on_line_user.setGeometry(QtCore.QRect(15, 10, 192, 621))
        self.on_line_user.setObjectName("on_line_user")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(15, 10, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(1, 1))
        self.label_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_2.setBaseSize(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.online_user_nums = QtWidgets.QLabel(self.widget_3)
        self.online_user_nums.setGeometry(QtCore.QRect(90, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.online_user_nums.setFont(font)
        self.online_user_nums.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.online_user_nums.setText("")
        self.online_user_nums.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1342, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.camera)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "在线人数: "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "来聊点什么吧~"))

    def camera(self):
        """
        open camera
        :return:
        """
        cap = cv2.VideoCapture(0)
        # 创建窗口
        cv2.namedWindow('Camera')

        while True:
            ret, frame = cap.read()
            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) == ord('q'):
                break
            if cv2.waitKey(1) == ord('c'):
                cv2.imwrite('photo.jpg', frame)

        # 释放摄像头和窗口
        cap.release()
        cv2.destroyAllWindows()

    def send_message(self):
        """
        发送消息
        :return:
        """
        message = self.lineEdit.text()
        self.lineEdit.clear()

        # 发送信息
        if message:
            self.tcp_client.send(f"{self.user_name}: {message}".encode("utf-8"))

    def receive_message(self):
        """
        获取广播信息并且在界面上显示
        :return:
        """
        while True:
            recv_data = self.tcp_client.recv(1024)
            message = recv_data.decode("utf-8")
            if "9000" in message and message.split(":")[0] == "9000":
                self.get_online_user_nums(message)
            else:
                self.textBrowser.append(message)

    def get_online_user_nums(self, message):
        """
        获取在线人数
        :return:
        """
        online_user_nums_list = re.findall("'name': '(.*?)'", message)
        online_user_nums = len(online_user_nums_list)
        self.online_user_nums.setText(str(online_user_nums))

    def start_work(self):
        """
        多线程
        :return:
        """
        t1 = threading.Thread(target=self.receive_message)
        t2 = threading.Thread(target=self.send_message)
        self.threading.append(t1)
        self.threading.append(t2)

        for thread in self.threading:
            thread.setDaemon(True)
            thread.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow(('ice'))  # 创建 PyQt 设计的窗体对象
    ui.setupUi(MainWindow)  # 调用 PyQt 窗体的方法对窗体对象进行初始化
    MainWindow.show()
    sys.exit(app.exec_())  # 程序关闭时退出进程