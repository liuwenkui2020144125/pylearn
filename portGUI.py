from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
import socket


def handleCalc():

    info = textEdit.toPlainText()
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((info, 80))
    cmd = 'GET http://info/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        textEdit.appendPlainText(data.decode())
    mysock.close()

app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('信息获取')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("输入网址")
textEdit.move(10, 25)
textEdit.resize(300, 200)

button = QPushButton('获取', window)
button.move(380, 80)

window.show()

button.clicked.connect(handleCalc)

app.exec_()
'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()
'''
