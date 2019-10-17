# Author:haha

import socket

server=socket.socket()
server.bind(('localhost',1234))#绑定要监听端口
server.listen(3)#监听,允许多少连接等待
print('开始等待指定端口号连接口号')
while True:
    con,addr=server.accept()#连接进来。。。
    #con就是客户端连过来而在服务器为其生成的一个连接实例
    print(con,addr)
    print('连接进来。。。')
    while True:
        data=con.recv(1024)
        print('recv:',data.decode())
        if not data:
            print('client has closed')
            break
        con.send(data)
server.close()
