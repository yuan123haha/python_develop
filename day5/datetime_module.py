# Author:haha
import datetime

print(datetime.datetime.now())#返回格式化日期格式
#输出：2019-08-17 00:32:25.011494
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
#输出：2019-08-20 00:32:25.011494
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
#输出：2019-08-14 00:32:25.011494
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
#输出：2019-08-17 03:32:25.011494
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
#输出：2019-08-17 01:02:25.011494
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))#时间替换，将小时替换为2，分钟变为3
#输出：2019-08-17 02:03:25.011494