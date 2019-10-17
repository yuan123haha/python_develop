# Author:haha

import socketserver,json,os,hashlib

class MyFtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.user_path = self.authentication()
            cmd_path=self.user_path
            while True:
                try:
                    f=open(self.user_path+'userinfo','r')
                    self.userfile_info=json.load(f)

                    cmd_info=self.request.recv(1024).decode()
                    data_info=json.loads(cmd_info)
                    cmd=data_info['method']
                    if cmd=='q':
                        break
                    elif hasattr(self,'_%s'%cmd):
                        func=getattr(self,'_%s'%cmd)
                        cmd_path=func(data_info,cmd_path)
                    else:
                        print('cmd[%s] does not exist!'%cmd)
                    f.close()
                except ConnectionResetError as e:
                    print('error:',e)
                    break

    def authentication(self):
        while True:
            login_data=self.request.recv(1024)
            login_dict=json.loads(login_data.decode())
            if login_dict['cmd']=='login':#判断是否是登录口令
                flag_dict=self.login(login_dict)
                if flag_dict['flag_info']=='true':
                    user_path='../userfile/%s/'%login_dict['account']
                    return user_path
                else:
                    continue
            else:
                flag_dict=self.register(login_dict)
                if len(flag_dict)==1:
                    continue
                user_path = '../userfile/%s/' % login_dict['account']
                return user_path

    def login(self,login_dict):
        user_file = '../userfile/%s' % login_dict['account']
        flag_dict = {}
        if os.path.isdir(user_file):  # 判断是否存在该用户
            f = open('../userfile/%s/userinfo' % login_dict['account'], 'r')
            user_dict = json.load(f)

            db_pswd = user_dict['pswd']
            if db_pswd == login_dict['pswd']:  # 判断用户输入密码是否正确
                flag_dict['flag_info'] = 'true'
                flag_dict['user_path']=login_dict['account']
            else:
                print("user[%s]'s pswd is error!" % login_dict['account'])
                flag_dict['flag_info'] = "user[%s]'s pswd is error!" % login_dict['account']
            f.close()
        else:
            print('account[%s] dose not exist' % login_dict['account'])
            flag_dict['flag_info'] = 'account[%s] dose not exist' % login_dict['account']
        self.request.send(json.dumps(flag_dict).encode())
        return flag_dict

    def register(self,register_dict):
        flag_dict={}
        if os.path.isdir('../userfile/%s' % register_dict['account']):
            flag_dict['flag_info']='account[%s] exist!'%register_dict['account']

        else:
            os.makedirs('../userfile/%s' % register_dict['account'])
            f = open('../userfile/%s/userinfo' % register_dict['account'], 'w')
            user_dict={}
            user_dict['pswd'] = register_dict['pswd']
            user_dict['space']=0
            user_dict['residue_space']=10000000
            json.dump(user_dict,f)

            flag_dict['flag_info']='register ok,welcome'
            flag_dict['user_path']=register_dict['account']
            f.close()
        self.request.send(json.dumps(flag_dict).encode())
        return flag_dict

    def _cd(self,data_info,cmd_path):
        #data_info['cd_path']='
        res_dict={}
        if data_info['cd_path']:
            path_file_list=data_info['cd_path'].split('/')
            for i in path_file_list:
                if i==''
        else:
            cmd_path=self.user_path
            res_dict['cmd_path']=cmd_path
        self.request.send(json.dumps(res_dict).encode())


    def _put(self,data_info,cmd_path):
        recv_data = {}
        if data_info['filesize']<self.userfile_info['residue_space']:
            recv_data['space']=True
            # if os.path.isfile(self.user_path+data_info['filename']) and os.stat(self.user_path+data_info['filename'])!=data_info['filesize']:#存在同名文件，是否续传
            #     recv_data['isContinue']=True
            # else:recv_data['isContinue']=False
        else:
            recv_data['space']=False
            self.request.send(json.dumps(recv_data).encode())
            return cmd_path
        if os.path.isfile(cmd_path+data_info['filename']):
            os.remove(cmd_path+data_info['filename'])
        self.request.send(json.dumps(recv_data).encode())
        f=open(cmd_path+data_info['filename'],'wb')
        m_file=hashlib.sha256()
        res_size=0
        while data_info['filesize']!=res_size:
            if data_info['filesize']-res_size>1024:
                size=1024
            else:
                size=data_info['filesize']-res_size
            res_data=self.request.recv(size)
            # print('res_data:',res_data)
            m_file.update(res_data)
            f.write(res_data)
            receive_size=len(res_data)
            res_size+=receive_size
        else:
            print('receive done!')
            print('server_file_m:',m_file.hexdigest())
            self.request.send(m_file.hexdigest().encode())
            f.close()
            return cmd_path

    def _get(self,data_info,cmd_path):
        file_info={}
        if os.path.isfile(cmd_path+data_info['filename']):
            file_info['file_isExist_info']='file[%s] does exist!'%data_info['filename']
            file_info['filesize']=os.stat(cmd_path+data_info['filename']).st_size
            self.request.send(json.dumps(file_info).encode())
            print(self.request.recv(1024).decode())
            f=open(cmd_path+data_info['filename'],'rb')
            m_server_file=hashlib.sha256()
            for line in f:
                m_server_file.update(line)
                self.request.send(line)
            self.request.send(m_server_file.hexdigest().encode())
            f.close()
        else:
            file_info['file_isExist_info']='file[%s] does not exist!'%data_info['filename']
            self.request.send(json.dumps(file_info).encode())
        return cmd_path


if __name__ == '__main__':
    host,port='localhost',1234
    server=socketserver.ThreadingTCPServer((host,port),MyFtpHandler)
    server.serve_forever()

