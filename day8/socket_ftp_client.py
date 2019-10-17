# Author:haha
import socket,hashlib
client=socket.socket()
client.connect(('localhost',8888))
m=hashlib.sha256()
while True:
    cmd_data=input('请输入指令：').strip()
    if len(cmd_data)==0:continue#如果输入字符为空，则重新输入
    client.send(cmd_data.encode('utf-8'))
    cmd,filename=cmd_data.split()
    if cmd=='get':
        file_size=client.recv(1024)#接收运行结果的长度
        print('file_size:',int(file_size.decode()))
        client.send('file_size已收到！'.encode('utf-8'))#防止连续接收的数据发生粘包
        receive_size=0
        f=open(filename+'new','wb')
        while receive_size!=int(file_size.decode()):#存在运行结果太长，一次接收不完，则分多次接收，判断接收的长度不等于总长度，则继续接收
            if int(file_size.decode())-receive_size>1024:#判断所剩文件大小是否小于1024，不小于继续接收，小于就只接收剩余大小文件，以便最后一次接收和sha256密码发生粘包
                size=1024
            else:
                size=int(file_size.decode())-receive_size
                print('最后一次size:',size)
            cmd_line = client.recv(size)#一行一行接收，并写入
            f.write(cmd_line)
            receive_data_size=len(cmd_line)
            receive_size+=receive_data_size
            m.update(cmd_line)
        else:
            print('接收完毕')
            receive_m=client.recv(2014).decode()#接收服务端发送的密码
            f.close()
            print('receive_m:',receive_m)
            print('m:',m.hexdigest())#自己的密码

client.close()
#get E:\袁明月\match\上传作品\初级开发组上传作品-最新.docx