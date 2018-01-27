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
