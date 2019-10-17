# Author:haha
import time

print(time.time())#得到当前时间的时间戳
#输出：1565966794.21425
print(time.timezone)#utc时间与本地时间的差值（时间戳）
#输出：-28800
print(time.altzone)#utc时间与夏令时间的差值（时间戳）
#输出：-32400
print(time.localtime())#返回本地时间的struct_time对象格式
#输出：time.struct_time(tm_year=2019, tm_mon=8, tm_mday=16, tm_hour=22, tm_min=53, tm_sec=29, tm_wday=4, tm_yday=228, tm_isdst=0)
print(time.gmtime())#返回utc时间的struct_time对象格式
#输出：time.struct_time(tm_year=2019, tm_mon=8, tm_mday=16, tm_hour=14, tm_min=58, tm_sec=3, tm_wday=4, tm_yday=228, tm_isdst=0)
print(time.asctime())#将struct_time对象格式转换成本地时间格式：Fri Aug 16 23:00:14 2019
#输出：Fri Aug 16 23:00:14 2019
print(time.ctime())#将时间戳转换成本地时间格式：Fri Aug 16 23:00:14 2019
#输出：Fri Aug 16 23:00:14 2019
string_struct=time.strptime('2019/8/16 23:04','%Y/%m/%d %H:%M')#将日期字符串转成struct时间对象格式
print(string_struct)
#输出：time.struct_time(tm_year=2019, tm_mon=8, tm_mday=16, tm_hour=23, tm_min=4, tm_sec=0, tm_wday=4, tm_yday=228, tm_isdst=-1)
print(time.strftime('%Y/%m/%d %H:%M',string_struct))#将struct时间对象转成日期字符串
#输出：2019/08/16 23:04
print(time.mktime(string_struct))#将struct时间对象转成时间戳
#输出：1565967840.0
