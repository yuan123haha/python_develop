# Author:haha
import socketserver

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                print('请求IP：',self.client_address[0])
                self.data=self.request.recv(1024)
                print('recv:',self.data.decode())
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('error:',e)
                break
if __name__ == '__main__':
    host,addr=('localhost'),1234
    server=socketserver.ThreadingTCPServer((host,addr),MyTcpHandler)
    server.serve_forever()