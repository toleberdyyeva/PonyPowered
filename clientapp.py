from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, \
                            QPushButton, QLabel, QLineEdit, QListWidgetItem, \
                            QTextEdit, QApplication
import sys
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QFont
from socket import socket
import threading
import pickle
import os
from time import time
import hashlib
import copy


def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())


def get_current_ip():
        import socket
        ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
        return ip


SERVER_ADDRESS = get_current_ip()


def accept_broadcast():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind(('', 12345))
        m = s.recvfrom(1024)
        print(m)
        global SERVER_ADDRESS
        SERVER_ADDRESS = m[1][0]
    except:
        pass