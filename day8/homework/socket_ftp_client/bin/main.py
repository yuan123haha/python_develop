# Author:haha

import socket,os,json,hashlib

class TcpClient(object):
    def __init__(self,host,port):
        self.conn=self.connect(host,port)


    def login(self,obj):
        while True:
            choose_cmd=input('l(login)/r(register):')
            m = hashlib.sha256()
            if choose_cmd=='l':#登录
                account=input('your username:').strip()
                pswd=input('your passwd:').strip()
                if len(account)>0 and len(pswd)>0:
                    m.update(pswd.encode())
                    login_dict={
                        'cmd':'login',
                        'account':account,
                        'pswd':m.hexdigest()
                    }
                    obj.send(json.dumps(login_dict).encode())
                    login_res_dict=json.loads(obj.recv(1024).decode())
                    if login_res_dict['flag_info']=='true':
                        print('account[%s] welcome!'%account)
                        return login_res_dict['user_path']
                    else:
                        print(login_res_dict['flag_info'])
            elif choose_cmd=='r':#注册
                account = input('your username:').strip()
                pswd = input('your passwd:').strip()
                if len(account) > 0 and len(pswd) > 0:
                    m.update(pswd.encode())
                    register_dict = {
                        'cmd': 'register',
                        'account': account,
                        'pswd': m.hexdigest()
                    }
                    obj.send(json.dumps(register_dict).encode())
                    register_stat=json.loads(obj.recv(1024).decode())
                    print(register_stat['flag_info'])
                    if len(register_stat)==1:
                        continue
                    return register_stat['user_path']
            else:
                print('input error!')

    def connect(self,host,port):
        client=socket.socket()
        client.connect((host,port))
        self.run(client)

    def help(self):
        msg='''
        cd
        pwd
        ls
        put filename
        get filename
        
        '''
        print('cmd_info:',msg)

    def run(self,obj):
        while True:
            server_cmd_path=self.login(obj)
            while True:
                cmd_value=input('%s>'%server_cmd_path).strip()
                if not cmd_value:continue
                elif cmd_value=='q':
                    cmd_dict={
                        'method':'q'
                    }
                    obj.send(json.dumps(cmd_dict).encode())
                    break
                cmd_split=cmd_value.split()
                if hasattr(self, '_%s'%cmd_split[0]):
                    func=getattr(self, '_%s'%cmd_split[0])
                    func(cmd_split,obj)
                else:
                    print('cmd[%s] does not exist!'%cmd_split[0])
                    self.help()

    def _get(self,cmd_split,obj):
        get_file_path='../data/'
        if len(cmd_split) == 2:
            filename = cmd_split[1].split('/')[-1]
            cmd_dict={
                'method':'get',
                'filename':filename
            }
            obj.send(json.dumps(cmd_dict).encode('utf-8'))
            rece_info=json.loads(obj.recv(1024).decode())
            if len(rece_info)==1:
                print(rece_info['file_isExist_info'])
                return
            filesize=int(rece_info['filesize'])
            if os.path.isfile(get_file_path+filename):
                os.remove(get_file_path+filename)
            obj.send('ok,you can...'.encode())
            f=open(get_file_path+filename,'wb')
            m_client_file=hashlib.sha256()
            receive_size=0
            while filesize!=receive_size:
                if filesize-receive_size>1024:
                    size=1024
                else:
                    size=filesize-receive_size
                res_data=obj.recv(size)
                f.write(res_data)
                res_size=len(res_data)
                receive_size+=res_size
                m_client_file.update(res_data)
            else:
                print('receive done!m_client_file:',m_client_file.hexdigest())
                print('m_server_file:',obj.recv(1024).decode())
        else:
            print('input error!')

    def _put(self,cmd_split,obj):
        if len(cmd_split) == 2:
            if os.path.isfile(cmd_split[1]):
                filesize = os.stat(cmd_split[1]).st_size
                filename=cmd_split[1].split('/')[-1]
                file_data = {
                    'method':'put',
                    'filesize': filesize,
                    'filename': filename
                }
                obj.send(json.dumps(file_data).encode('utf-8'))
                server_stat=json.loads(obj.recv(1024).decode())
                if server_stat['space']:
                    # if server_stat['isContinue']:
                    #     pass
                    # else:
                    m_file=hashlib.sha256()
                    f = open(cmd_split[1], 'rb')
                    for line in f:
                        obj.send(line)
                        m_file.update(line)
                    print('put done! the m_file:',m_file.hexdigest())
                    server_file_m=obj.recv(1024).decode()
                    print('server_file_m',server_file_m)
                else:
                    print('residue_space is not enoght!')
                    return
            else:
                print('filename[%s] does not exist!', cmd_split[1])
                return
        else:
            print('input error!')
            return

    # def _cd(self,cmd_split,obj):
    #     cmd_dict={'method':'cd'}
    #     if len(cmd_split)==2:
    #         cmd_dict['cd_path']=cmd_split[1]
    #         cd_pathfile_list=cmd_split[1].split('/')
    #         if len(cd_pathfile_list[0]):
    #     elif len(cmd_split)==1:
    #         cmd_dict['cd_path']=None
    #     else:
    #         print('input error!')
    #         return


if __name__ == '__main__':
    tcp_client=TcpClient('localhost',1234)
#put ../data/初级开发组上传作品-最新.docx
#get 团队介绍.docx