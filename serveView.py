
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from socket import *
IP = ''
PORT = 8888
BUFFLEN = 512


#开启客户端
def startServe(self):
	info = textEdit.toPlainText()
	listenSocket = socket(AF_INET,SOCK_STREAM)
	listenSocket.bind((IP,PORT))
	listenSocket.listen(8)
	print(f'客户端启动成功，在 {PORT} 端口等待客户端连接...')
	dataSocket,addr = listenSocket.accept()
	print(f'接受一个客户端', addr)
	while True:
		recved = dataSocket.recv(BUFFLEN)
		if not recved:
			break
			info = recved.decode()
			print(f'收到对方信息：{info}')
			dataSocket.send(f'服务端收到信息：{info}'.encode())
			QMessageBox.about(window, '收到信息：', f'''tip1:\n{info}\n''')
	dataSocket.close()
	listenSocket.close()


def startClient():
	IP = '127.0.0.1'
	SERVER_PORT = 50000
	BUFFLEN = 1024
	dataSocket = socket(AF_INET, SOCK_STREAM)
	dataSocket.connect((IP, SERVER_PORT))
	while True:
		toSend = input('>>>')
		if toSend == 'exit':
			break
		dataSocket.send(toSend.encode())
		recved = dataSocket.recv(BUFFLEN)
		if not recved:
			break

		print(recved.decode())

	dataSocket.close()


app = QApplication([])
window = QMainWindow()
window.resize(500, 300)
window.move(300, 310)
window.setWindowTitle('服务端')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("等待客户端启动")
textEdit.move(10, 25)
textEdit.resize(300, 100)

button = QPushButton('打开服务器', window)
button.move(380, 80)
button.clicked.connect(startServe)


button = QPushButton('打开客户端', window)
button.move(380, 160)
button.clicked.connect(startClient)


window.show()
app.exec_()

