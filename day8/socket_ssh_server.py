# Author:haha
import socket,os

server=socket.socket()
server.bind(('localhost',6666))
server.listen()
while True:
    con,addr=server.accept()
    print('已连接：',addr)
    while True:
        cmd_data = con.recv(1024)
        print('接收指令：',cmd_data.decode())
        if not cmd_data:
            print('客服端以断开')
            break
        cmd_res=os.popen(cmd_data.decode()).read()#运行命令
        if len(cmd_res)==0:#有可能会报错，就造一个cmd_res数据，保证通话继续
            cmd_res='执行结果为空'
        cmd_res_size=len(cmd_res)
        print('cmd_res_size:',cmd_res_size)
        con.send(str(cmd_res_size).encode('utf-8'))#返回执行结果的长度
        print('cmd_res:',cmd_res)
        # client_ack=con.recv(1024)#如果连续发送的数据发生粘包，就使用这种处理方法
        # print('client_ack:',client_ack.decode())
        con.send(cmd_res.encode('utf-8'))

server.close()