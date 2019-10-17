# Author:haha
import socket,os,hashlib

server=socket.socket()
server.bind(('localhost',8888))
server.listen()
while True:
    con,addr=server.accept()
    print('已连接：',addr)
    while True:
        data=con.recv(1024).decode()
        cmd,filename= data.split()
        m=hashlib.sha256()
        print('接收指令：',cmd)
        if not data:
            print('客服端以断开')
            break
        if os.path.isfile(filename):
            f=open(filename,'rb')
            file_size=os.stat(filename).st_size
            con.send(str(file_size).encode('utf-8'))
            print('file_size:',file_size)
            con.recv(1024)
            for line in f:
                con.send(line)
                m.update(line)
            con.send(m.hexdigest().encode('utf-8'))
            print('sha256加密码：',m.hexdigest())
            f.close()
server.close()