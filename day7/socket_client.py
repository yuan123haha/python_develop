# Author:haha

import socket

client=socket.socket()#声明socket类型，同时生成socket连接对象
client.connect(('192.168.110.128',1234))
while True:
    input_data=input('>').strip()
    if len(input_data)==0:continue
    client.send(input_data.encode('utf-8'))
    data=client.recv(1024)
    print('rece:',data.decode())
client.close()