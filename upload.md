### sever  code
```
import socket
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',9000))
sock.listen(2)
print('waiting connnect...')
conn,addr = sock.accept()
while True:	
	filename = 'C:/Users/redhat/test.txt'#接收的文件路径
	print('I want to get the file %s!' % filename)
	conn.send(filename.encode('utf-8'))
	str1 = conn.recv(1024)
	str2 = str1.decode('utf-8')#接收握手信息、判断
	if str2 == 'no':
		print('The file %s is not exit' % filename)
	else:
		conn.send(b'I am ready!')
		temp = filename.split('/')#去除特殊符号/
		myname = 'my_' + temp[len(temp)-1]
		size = 1024
		with open(myname,'wb') as f:
			while True:
				data = conn.recv(size)
				f.write(data)
				if len(data) < size:
					break
	conn.close()
	print('The download file is %s !' % myname)
sock.close()
```



### client  code
```
import socket
import os
#定义发送文件的方法
def sendfile(sock):
	str1 = sock.recv(1024)
	filename = str1.decode('utf-8')
	print('the sever request my file: %s' , filename)
	if os.path.exists(filename):
	#调用os方法判断文件是否存在
	#存在发送握手信息‘yes’准备传输，不存在返回握手信息‘no’
		print('I have %s ,begin to download!' % filename)
		sock.send(b'yes')#发送握手信息
		sock.recv(1024)
		size = 1024
		with open(filename, 'rb') as f:
			while True:
				data = f.read(size)
				sock.send(data)
				if len(data) < size:
					break
		print('%s is download sucessfully!' % filename)
	else:
		print('Sorry ,I have bo %s' % filename)
		sock.send(b'no')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9000))
while True:
	sendfile(sock)
sock.close()
```


