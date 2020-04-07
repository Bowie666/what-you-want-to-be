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

# # 查看内存
# mem = psutil.virtual_memory()
# total = str(round(mem.total / 1024 / 1024))
#
# # round方法进行四舍五入，然后转换成字符串 字节/1024得到kb 再/1024得到M
# used = str(round(mem.used / 1024 / 1024))
# use_per = str(round(mem.percent))
# free = str(round(mem.free / 1024 / 1024))
# print("您当前的内存大小为:" + total + "M")  # 您当前的内存大小为:8076M
# print("已使用:" + used + "M(" + use_per + "%)")  # 已使用:5805M(72%)
# print("可用内存:" + free + "M")  # 可用内存:2271M


# # 查看CPU
# # interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率；
# print(psutil.cpu_percent(interval=2))
# print(psutil.cpu_percent(interval=1))


# 查看磁盘
print(psutil.disk_partitions())
print(str(psutil.disk_usage("/").total / 1024 / 1024))
psutil.disk_partitions()  # 磁盘分区信息 [sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
psutil.disk_usage('/')  # 磁盘使用情况 sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)
psutil.disk_io_counters()  # 磁盘IO sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)

# 查看显卡, 放到服务器上使用
# 简单使用
from pynvml import *

nvmlInit()  # 初始化
print("Driver: ", nvmlSystemGetDriverVersion())  # 显示驱动信息
# >>> Driver: 384.xxx

# 查看设备
deviceCount = nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = nvmlDeviceGetHandleByIndex(i)
    print("GPU", i, ":", nvmlDeviceGetName(handle))
# >>>
# GPU 0 : b'GeForce GTX 1080 Ti'
# GPU 1 : b'GeForce GTX 1080 Ti'

# 查看显存、温度、风扇、电源
handle = nvmlDeviceGetHandleByIndex(0)
info = nvmlDeviceGetMemoryInfo(handle)
print("Memory Total: ", info.total)  # 第二块显卡总的显存大小
print("Memory Free: ", info.free)  # 这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2
print("Memory Used: ", info.used)  # 第二块显卡剩余显存大小

print("Temperature is %d C" % nvmlDeviceGetTemperature(handle, 0))
print("Fan speed is ", nvmlDeviceGetFanSpeed(handle))
print("Power ststus", nvmlDeviceGetPowerState(handle))

# 最后要关闭管理工具
nvmlShutdown()
