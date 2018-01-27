from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QListWidget, \
                            QPushButton, QLabel, QLineEdit, QListWidgetItem, \
                            QTextEdit, QTabWidget, QHBoxLayout, \
                            QApplication, QGridLayout
import sys
from socket import socket
from threading import Thread, Timer
import pickle
import os
import time
import database
import hashlib
from random import randint
import copy


def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())


def broadcast():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        s.sendto('this is testing'.encode('utf-8'),('255.255.255.255',12345))
        import time
        time.sleep(1)


def get_current_ip():
        import socket
        ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
        return ip


class User(QWidget):
    first = 1

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainlayout = QVBoxLayout()
        deletegroup = QGroupBox('Delete users')
        addgroup = QGroupBox('Add users')
        deletelay = QVBoxLayout()
        addlay = QVBoxLayout()
        self.list = QListWidget()
        self.refreshusers()
        self.delbtn = QPushButton('Delete user', self)
        self.delbtn.clicked.connect(self.delete)
        deletelay.addWidget(self.list)
        deletelay.addWidget(self.delbtn)
        deletegroup.setLayout(deletelay)
        loglay = QGridLayout()
        loglabel = QLabel('Login: ')
        self.logline = QLineEdit(self)
        loglay.addWidget(loglabel, 0, 0)
        loglay.addWidget(self.logline, 0, 1)
        passlabel1 = QLabel('Password: ')
        passlabel2 = QLabel('Repeat password: ')
        self.passline1 = QLineEdit(self)
        self.passline1.setEchoMode(QLineEdit.Password)
        self.passline2 = QLineEdit(self)
        self.passline2.setEchoMode(QLineEdit.Password)
        self.addstatus = QLabel()
        loglay.addWidget(passlabel1, 1, 0)
        loglay.addWidget(self.passline1, 1, 1)
        loglay.addWidget(passlabel2, 2, 0)
        loglay.addWidget(self.passline2, 2, 1)
        loglay.addWidget(self.addstatus)
        addlay.addLayout(loglay)
        addbtn = QPushButton('Add user')
        addbtn.clicked.connect(self.adduser)
        addlay.addWidget(addbtn)
        addgroup.setLayout(addlay)
        mainlayout.addWidget(deletegroup)
        mainlayout.addWidget(addgroup)
        self.setLayout(mainlayout)

    def refreshusers(self):
        self.list.clear()
        self.userlist = database.selectall()
        for i in self.userlist:
            a = QListWidgetItem(i[0])
            self.list.addItem(a)

    def delete(self):
        for i in self.list.selectedItems():
            a = i.text()
        database.deletebyname(a)
        self.refreshusers()

    def adduser(self):
        password1 = self.passline1.text()
        password2 = self.passline2.text()
        if password1 == password2:
            login = self.logline.text()
            password = hashlib.md5(password1.encode('utf-8')).hexdigest()
            database.insertuser(login, password)
            self.refreshusers()
            self.passline1.setText('')
            self.passline2.setText('')
            self.logline.setText('')
            self.addstatus.setText("<font color='blue'>User added</font>")
        else:
            self.addstatus.setText("<font color='red'>Check password</font>")
