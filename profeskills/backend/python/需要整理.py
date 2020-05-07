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
import urllib.request
import psutil
import time
import requests
import os
from xml.dom import minidom
import re
import xml.etree.ElementTree as ET
import subprocess

# # date = "2018-04-20 15:42:54"
# date = "2020-05-07 11:03:18"
#
#
# #转换成时间数组
# timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
#
# #1).转换成时间戳
# timestamp = time.mktime(timeArray)
# print(int(timestamp))
# print(int(time.time()) - int(timestamp))
# log_dir = 'ss'
# b = 'tensorboard --logdir={} --port=8010 --host=0.0.0.0'.format(log_dir)
# print(b)
# log_path = os.path.join('vislogpath', 'log.log')
# print(log_path)
# print(time.localtime(time.time()))
# localtime = time.localtime(time.time())
# nowt = str(localtime.tm_year) + str(localtime.tm_mon) + str(localtime.tm_mday)
# print(nowt)
# bdir = '/home/xuwei/data/train/'
# print(str(time.time()))
# iu = str(int(time.time()))
# localtime = time.localtime(time.time())
# nowt = str(localtime.tm_year) + str(localtime.tm_mon) + str(localtime.tm_mday) + str(localtime.tm_hour)
# # datadir = bdir + "algo" + "/" + nowt + "/data/train_imgs/"
# # s = datadir.replace('train_imgs', 'train_anns')
# # a = datadir.replace('train_imgs', 'eval_anns')
# # d = datadir.replace('train_imgs', 'eval_imgs')
# # data = datadir.replace('data/train_imgs', 'vislog')
# datadir = bdir + 'algo' + "/" + nowt + iu + "/imgdata/"
#
# train_imgs = datadir + "train_imgs/"
# train_anns = datadir + 'train_anns/'
# eval_anns = datadir + 'eval_anns/'
# eval_imgs = datadir + 'eval_imgs/'
# vislog = datadir.replace('imgdata', 'vislog')
# print(train_imgs)
# print(train_anns)
# print(eval_anns)
# print(eval_imgs)
# print(vislog)
# ls1 = [('/data/输电通道隐患检测/2020-04-11/开发测试用数据集12/thumbnails/58761.jpg', 0.7623594999313354),
#        ('/data/输电通道隐患检测/2020-04-10/开发测试用数据集10/thumbnails/58761.jpg', 0.7623594999313354),
#        ('/data/输电通道隐患检测/2020-04-14/开发测试用数据集96/thumbnails/58777.jpg', 0.7384615540504456),
#        ('/data/输电通道隐患检测/2020-04-14/开发测试用数据集85/thumbnails/58777.jpg', 0.7384615540504456),
#        ('/data/输电通道隐患检测/2020-04-10/开发测试用数据集9/thumbnails/58777.jpg', 0.7384615540504456),
#        ('/data/输电通道隐患检测/2020-04-14/开发测试用数据集85/thumbnails/58768.jpg', 0.7323359847068787),
#        ('/data/输电通道隐患检测/2020-04-10/开发测试用数据集9/thumbnails/58768.jpg', 0.7323359847068787),
#        ('/data/输电通道隐患检测/2020-04-11/开发测试用数据集12/thumbnails/58760.jpg', 0.7090008854866028),
#        ('/data/输电通道隐患检测/2020-04-10/开发测试用数据集10/thumbnails/58760.jpg', 0.7090008854866028),
#        ('/data/输电通道隐患检测/2020-04-14/开发测试用数据集85/thumbnails/58775.jpg', 0.7069896459579468),
#        ('/data/输电通道隐患检测/2020-04-10/开发测试用数据集9/thumbnails/58758.jpg', 0.7014157772064209),
#        ('/data/输电通道隐患检测/2020-04-11/开发测试用数据集12/thumbnails/58759.jpg', 0.6877801418304443),
#        ('/data/输电通道隐患检测/2020-04-10/开发测试用数据集10/thumbnails/58759.jpg', 0.6877801418304443),
#        ('/data/输电通道隐患检测/2020-04-14/开发测试用数据集85/thumbnails/58766.jpg', 0.6479170322418213),
#        ('/data/输电通道隐患检测/2020-04-15/222/thumbnails/DJI_0085.jpg', 0.6014866232872009),
#        ('/data/输电通道隐患检测/2020-04-15/6/thumbnails/DJI_0085.jpg', 0.6014866232872009)]
#
# # for i in ls1:
# #        print(i[1])
# # # ls1.sort([i[1] for i in ls1])
# # print([i[1] for i in ls1].sort())
# # print(ls1.sort())
# # print(sorted(ls1))
# new_list = []
# for item in ls1:
#     new_list.append(item[::-1])
# print(new_list)
# print(sorted(new_list, reverse=True)[:1])
# res = subprocess.check_output('ls .', shell=True)
# pid = ['COMMAND     PID  USER   FD   TYPE    DEVICE SIZE/OFF NODE NAME\n', 'tensorboa 45189 xuwei    3u  IPv4 136244799      0t0  TCP *:8010 (LISTEN)\n']
# print(pid[1])
# print(pid[1].split(' '))
# print(pid[1].split(' ')[1])
# print(type(pid[1].split(' ')[1]))
# print(type(int(pid[1].split(' ')[1])))
# os.system('C:\\Users\\Administrator\\Desktop\\look')
# with open(r'C:\Users\Administrator\Desktop\dingdign\log.log', 'r', encoding='utf-8') as f:
#     x = f.read()
#     if len(re.findall(r'Training has finished!', x)):
#         print(0)
#     pattern = re.compile(r'(?<=Start Epoch )\d+\.?\d*')
#     # for i in f.readlines(-1):
#     #        pattern = re.compile(r'(?<=Start Epoch )\d+\.?\d*')
#     #        pattern.findall(string)
#     #        if re.compile(^Start Epoch$, i):
#     #               j = i.split("Start Epoch")[-1]
#     #               print(re.findall(r'\d', j))
#     #        if pattern.findall(i):
#     print(pattern.findall(x)[-1])
#     # print(pattern.search(x))
"""import re


log_file = ''
log_buff = ''
with open(log_file, 'r') as f:
    log_buff = f.read(-1)

pattern1 = re.compile(r'Total epochs of the training set is: \d+')
total_epoch = int(re.compile(r'\d+').findall(pattern1.findall(log_buff)[0])[0])

pattern2 = re.compile(r'Start Epoch \d+ ...')
now_epoch = int(re.compile(r'\d+').findall(pattern1.findall(log_buff)[-1])[0])

print(total_epoch, now_epoch)"""
#
# if not os.path.exists("f:/666"):
#     os.mkdir("f:/666")
# class XmlNode():
#     def __init__(self, x_dom, root):
#         self.diff = 0
#         self.dom = x_dom
#         self.root = root
#
#     def single_node(self, name, text, c_node=None):
#         # root 根节点
#         # name 子节点名称
#         # text 子节点内容
#         # c_node 父节点
#         # 用DOM对象创建元素子节点
#         # 用父节点对象添加元素子节点
#         # 设置该节点内容
#         node = self.dom.createElement(name)
#         if c_node is None:
#             self.root.appendChild(node)
#         else:
#             c_node.appendChild(node)
#         name_text = self.dom.createTextNode(text)
#         node.appendChild(name_text)
#
#     def file_node(self, folder, file_name, path):
#         # 创建folder、filename、path节点
#         # root 根节点
#         # folder 文件夹名
#         # file_name 文件名
#         # path 文件绝对路径
#         self.single_node('folder', folder)
#         self.single_node('filename', file_name)
#         self.single_node('path', path)
#
#     def source_node(self):
#         # 创建source_node节点
#         # root 根节点
#         node = self.dom.createElement('source')
#         self.root.appendChild(node)
#         self.single_node('database', 'Unknown', node)
#
#     def size_node(self, width, height, depth):
#         # 创建size节点
#         # root 根节点
#         # width 图片宽
#         # height 图片高
#         # depth 图片通道
#         node = self.dom.createElement('size')
#         self.root.appendChild(node)
#         self.single_node('width', str(width), node)
#         self.single_node('height', str(height), node)
#         self.single_node('depth', str(depth), node)
#
#     def object_node(self, label, diff, box, score, warn=None):
#         # 创建object节点
#         # root 根节点
#         # lable 类型
#         # diff  困难/简易样本
#         # box 坐标列表
#         # score 预测值
#         # warning 隐患严重等级
#         node = self.dom.createElement('object')
#         self.root.appendChild(node)
#         self.single_node('name', label, node)
#         self.single_node('pose', 'Unspecified', node)
#         self.single_node('truncated', '0', node)
#         self.single_node('difficult', diff, node)
#         if warn is not None:
#             self.single_node('warning', warn, node)
#         else:
#             self.single_node('warning', 'None', node)
#         box_node = self.dom.createElement('bndbox')
#         node.appendChild(box_node)
#         self.single_node('xmin', str(box[0]), box_node)
#         self.single_node('ymin', str(box[1]), box_node)
#         self.single_node('xmax', str(box[2]), box_node)
#         self.single_node('ymax', str(box[3]), box_node)
#         self.single_node('score', str(score), node)
#
#     def fill_text_node(self):
#         root_node = self.dom.documentElement
#         scene = root_node.getElementsByTagName("scene")[0]
#         scene_text_node = scene.childNodes[0]
#         text = scene_text_node.data + '有'
#         objects = root_node.getElementsByTagName("object")
#         for obj in objects:
#             obj_name = obj.getElementsByTagName("name")[0]
#             name_text = obj_name.childNodes[0].data
#             obj_warn = obj.getElementsByTagName("warning")[0]
#             warn_text = obj_warn.childNodes[0].data
#             text = text + warn_text + '预警的' + name_text
#         text_node = root_node.getElementsByTagName("text")[0]
#         text_node.childNodes[0].data = text
#
#     def save(self, path):
#         """
#         :param path: xml 路径
#         :return:
#         """
#         try:
#             with open(path, 'w', encoding='UTF-8') as f:
#                 # writexml()
#                 # 第一个参数是目标文件对象
#                 # 第二个参数是根节点的缩进格式
#                 # 第三个参数是其他子节点的缩进格式
#                 # 第四个参数制定了换行格式
#                 # 第五个参数制定了xml内容的编码。
#                 self.dom.writexml(f, indent='', addindent='\t',
#                                   newl='\n', encoding='UTF-8')
#                 return path
#         except Exception as err:
#             print('错误信息：{0}'.format(err))
#             return None
#
#
# class XmlParser(object):
#
#     def __init__(self, path):
#         self.tree = ET.parse(path)
#
#     @property
#     def data(self):
#         data = {}
#         data['name'] = self.tree.findall('filename')[0].text
#         data['annotations'] = []
#         obj_list = self.tree.findall('object')
#         for obj in obj_list:
#             frame_data = [float(box.text)
#                           for box in obj.findall('bndbox')[0].getchildren()]
#             data['annotations'].append({
#                 'tag': obj.findall('name')[0].text,
#                 'frame': {
#                     'x': frame_data[0],
#                     'y': frame_data[1],
#                     'width': frame_data[2] - frame_data[0],
#                     'height': frame_data[3] - frame_data[1]
#                 }
#             })
#         return data
#
# def save_xml(image_id):
#     """根据图像 id 生成 xml 文件
#
#     Arguments:
#         image_id {int} -- 图像数据 ID
#
#     Returns:
#         str -- xml 文件路径
#     """
#     image: ImageData = ImageData.query.get(image_id)
#
#     # 创建DOM树对象
#     dom = minidom.Document()
#     root_node = dom.createElement('annotation')
#     dom.appendChild(root_node)
#     xml = XmlNode(dom, root_node)
#
#     # 图像目录路径、文件名、目录名称
#     image_abs_path = os.path.join(STATIC_FOLDER, image.path)
#     image_dir, image_name = os.path.split(image_abs_path)
#     image_folder = image_dir.split('/')[-1]
#
#     # 填充 xml 数据
#     xml.file_node(image_folder, image_name, image_abs_path)
#     xml.single_node('difficult', '0')
#     xml.source_node()
#     xml.size_node(image.width, image.height, image.depth)
#     xml.single_node('segmented', '0')
#     xml.single_node('text', '场景描述节点')
#     xml.single_node('scene', '场景节点')
#     for annotation in image.annotations:
#         box = (
#             int(annotation.pos_x),
#             int(annotation.pos_y),
#             int(annotation.pos_x + annotation.width),
#             int(annotation.pos_y + annotation.height),
#         )
#         xml.object_node(annotation.tag.name, '0', box, annotation.score)
#     xml.fill_text_node()
#
#     return xml.save(os.path.join(STATIC_FOLDER, image.xml_path))


# base_dir = os.getcwd()
# print(os.getcwd())
# str = 'cp {0}/config.cfg ./\npython voc_label.py\n{0}/darknet detector train {0}/cfg/voc.data {0}/cfg/yolov3-voc.cfg darknet53.conv.74 -gpus '.format(base_dir)
# print(str)

# 保存网页图片路径
# urllib.request.urlretrieve('https://upload-images.jianshu.io/upload_images/3980862-5825acffe2b3a3f4.png?imageMogr2/auto-orient/strip|imageView2/2/w/793/format/webp', 'f:/7.jpg')

# 图片地址
# st = int(time.time())
# url = 'https://dss0.baidu.com/73F1bjeh1BF3odCf/it/u=2777493483,1706022420&fm=85&s=3FC2F75FFF4366CE584D2CE403005072'
# html = requests.get(url)
# # 将图片保存到D盘
# with open("/data/home/xuwei/1.jpg","wb")as f:
#     f.write(html.content)
# et = int(time.time())
# print(et - st)

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

#
# # 查看磁盘
# print(psutil.disk_partitions())
# print(str(psutil.disk_usage("/").total / 1024 / 1024))
# psutil.disk_partitions()  # 磁盘分区信息 [sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
# psutil.disk_usage('/')  # 磁盘使用情况 sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)
# psutil.disk_io_counters()  # 磁盘IO sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)
#
# # 查看显卡, 放到服务器上使用
# # 简单使用
# from pynvml import *
#
# nvmlInit()  # 初始化
# print("Driver: ", nvmlSystemGetDriverVersion())  # 显示驱动信息
# # >>> Driver: 384.xxx
#
# # 查看设备
# deviceCount = nvmlDeviceGetCount()
# for i in range(deviceCount):
#     handle = nvmlDeviceGetHandleByIndex(i)
#     print("GPU", i, ":", nvmlDeviceGetName(handle))
# # >>>
# # GPU 0 : b'GeForce GTX 1080 Ti'
# # GPU 1 : b'GeForce GTX 1080 Ti'
#
# # 查看显存、温度、风扇、电源
# handle = nvmlDeviceGetHandleByIndex(0)
# info = nvmlDeviceGetMemoryInfo(handle)
# print("Memory Total: ", info.total)  # 第二块显卡总的显存大小
# print("Memory Free: ", info.free)  # 这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2
# print("Memory Used: ", info.used)  # 第二块显卡剩余显存大小
#
# print("Temperature is %d C" % nvmlDeviceGetTemperature(handle, 0))
# print("Fan speed is ", nvmlDeviceGetFanSpeed(handle))
# print("Power ststus", nvmlDeviceGetPowerState(handle))
#
# # 最后要关闭管理工具
# nvmlShutdown()
