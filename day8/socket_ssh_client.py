# Author:haha
import socket
client=socket.socket()
client.connect(('localhost',6666))
while True:
    cmd_data=input('请输入指令：').strip()
    if len(cmd_data)==0:continue#如果输入字符为空，则重新输入
    client.send(cmd_data.encode('utf-8'))
    cmd_res_size=client.recv(1024)#接收运行结果的长度
    print('cmd_res_size:',int(cmd_res_size.decode()))
    # client.send('cmd_res_size已收到！'.encode('utf-8'))#防止连续接收的数据发生粘包
    receive_size=0
    while receive_size!=int(cmd_res_size.decode()):#存在运行结果太长，一次接收不完，则分多次接收，判断接收的长度不等于总长度，则继续接收
        cmd_res = client.recv(1024)
        print('运行结果如下：', cmd_res.decode())
        receive_data_size=len(cmd_res.decode())
        receive_size+=receive_data_size

    else:print('接收完毕')


client.close()