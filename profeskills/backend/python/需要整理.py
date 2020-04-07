"""1
git checkout 5km
git pull origin 5km
git checkout xuwei
git merge 5km
有冲突就进冲突文件修改
然后git  add
git commit
在merge就好
"""
import psutil
import time

# 查看内存
mem = psutil.virtual_memory()
total = str(round(mem.total / 1024 / 1024))

# round方法进行四舍五入，然后转换成字符串 字节/1024得到kb 再/1024得到M
used = str(round(mem.used / 1024 / 1024))
use_per = str(round(mem.percent))
free = str(round(mem.free / 1024 / 1024))
print("您当前的内存大小为:" + total + "M")  # 您当前的内存大小为:8076M
print("已使用:" + used + "M(" + use_per + "%)")  # 已使用:5805M(72%)
print("可用内存:" + free + "M")  # 可用内存:2271M


# 查看CPU
# interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率；
print(psutil.cpu_percent(interval=2))
print(psutil.cpu_percent(interval=1))
