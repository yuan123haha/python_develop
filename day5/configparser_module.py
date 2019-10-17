# Author:haha

import configparser

config=configparser.ConfigParser()
config.read('example.ini')
print(config.sections())#打印除default外的其他节点
print(config['bitbucket.org']['user'])#打印指定节点下的数据
print(config.defaults())#打印default下面的配置数据
print('bitbucket.org' in config)#判断指定数据是否在config中
print(config.options('bitbucket.org'))#打印指定节点的子列表+default下的key值数据
#输出：['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
print(config.items('bitbucket.org'))#打印指定节点+default下的数据
#输出：[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]
print(config.get('bitbucket.org','user'))#打印指定节点下指定key值的value数据
#输出：hg
print(config.getint('topsecret.server.com','host port'))#打印指定节点下指定key值的value int数据
#输出：50022

#修改数据
config.set('bitbucket.org','user','haha')#修改指定节点的指定key值的value值，没有就创建
print(config.has_option('bitbucket.org','user'))#判断指定节点是否包含指定key值
print(config.add_section('bitbucket.org'))#添加指定节点
print(config.has_section('bitbucket.org'))#判断有无指定节点，没有就创建
config.remove_section('bitbucket.org')#删除指定节点
config.remove_option('bitbucket.org','user')#删除指定节点的指定key栏数据
config.write(open('example.ini','w'))#覆盖原来的文件