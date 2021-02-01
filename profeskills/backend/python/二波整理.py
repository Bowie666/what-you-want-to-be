#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from Crypto.Cipher import AES
import base64
import time
import gzip
from hashlib import md5
import sys
import io
from xml.dom.minidom import parse
from xml.dom import minidom
import shutil
import json
# from PIL import Image

from datetime import datetime, timedelta
import os
import re
import requests
import glob

# coding:utf-8
# import cv2
# import imageio
# from scipy import misc
from PIL import Image
from matplotlib import pyplot as plt
import rsa
import redis


# from concurrent.futures import ThreadPoolExecutor
# thread_pool = ThreadPoolExecutor(4)

# date_day = time.strftime("%Y%m%d")  # 20210120
# que_name = "fcm_video_name@127.0.0.1@" + date_day

# r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# # vpath = "/SDXL/FCMUpload/99000843024138/202101/"
# vpath = r"C:\Users\Administrator\Desktop\video"

# for pa in os.listdir(vpath):
# 	ppa = pa.split('.')
# 	if ppa[1] == 'mp4':
# 		old_path = os.path.join(vpath, pa)
# 		# 把视频文件复制几次  比如 原来有5个mp4文件 复制3次 就成了15个视频
# 		for ti in range(500):
# 			new_path = os.path.join(vpath, f'{ppa[0]}{ti}.{ppa[1]}')
# 			shutil.copy(old_path, new_path)


# # for i in range(1000):
# j = 0
# for pa in os.listdir(vpath):
#     if pa.split('.')[-1] == "mp4":
#         # print(pa, type(pa))
#         r.rpush(que_name, pa)
#         j += 1
# print(j)


# while True:
#     date_day = time.strftime("%Y%m%d")
#     que_name = "fcm_video_name@127.0.0.1@"+date_day
#     data = r.rpop(que_name)
#     # print(data, type(data))  # b'ZYA20201000000053_20201209073023_23.mp4' <class 'bytes'>
#     if not data:
#         time.sleep(5)
#         continue
#     data_split = data.split("_")
#     deviceID = data_split[0]
#     date_time = data_split[1][:12]
#     path = date_time[:6]
#     video_path = os.path.join("/data/SDXL/FCMUpload", deviceID, path, data)# /data/SDXL/FCMUpload/deviceID/202101/deviceID_
#     print({str([date_time, deviceID, video_path]):int(date_time)})

# def cou(n):
#     while n>0:
#         yield n
#         n -= 1

# c = cou(5)
# # print(c)
# print(c.__next__())
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# print(time.time())
# from concurrent.futures import ThreadPoolExecutor
# thread_pool = ThreadPoolExecutor(4)

# def dect(imgpath, detect_url):
#     headers = {"accept": "application/json"}

#     with open(imgpath, "rb") as f:
#         video = f.read()

#     ann_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

#     data = {
#         "push_url": "http://192.168.0.120:20723/vid",
#     }

#     files = {"video": (os.path.basename(imgpath), video, 'video/mp4')}
#     resp = requests.post(detect_url, headers=headers, data=data, files=files)
#     result = resp.json()

# videoPath = r"C:\Users\Administrator\Desktop\video"
# video_count = os.listdir(videoPath)
# detect_url = "http://192.168.0.120:9009/api/dance/analysis"

# i = 1
# for vi in video_count:
#     video_abs = os.path.join(videoPath, vi)
#     thread_pool.submit(dect, video_abs, detect_url)
#     i += 1
#     print(i)


# url = "http://192.168.0.114:20601/api/models?detail=true"
# resp = requests.get(url)
# model_data = resp.json()

# for mod in model_data["models"]:
#     print(mod["api_name"])



# print(ra)
# # -------------------------base64 begin-------------------
# s = "你好"

# bs = base64.b64encode(s.encode("utf-8")) # 将字符为unicode编码转换为utf-8编码
# print(bs) # 得到的编码结果前带有 b

# bbs = str(base64.b64decode(bs), "utf-8")
# print(bbs) # 解码

# bs = str(base64.b64encode(s.encode("utf-8")), "utf-8")
# print(bs) # 去掉编码结果前的 b

# bbs = str(base64.b64decode(bs), "utf-8")
# print(bbs) # 解码
# # -------------------------base64 end-------------------


# # -----------------------base
# gallui = b'HAz8dmtABxxYb19q2JzEmjYtzLX31QrM3B7lKGbhaeT/wd9meooh2dfUcQdpw1vXsp9GRfjPLEKjJas2PyL/Ra4DiOZ/oGoez1s7RoOtCflbp3mamegQh7TboVSGgP/ci+xnMTgrHRVwLYZMYro+QVyXMFmMujS/H5rSAwUMJpM='
# msg = 'MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBAJ/RJOOoRGHHbTH4wxdIThgi3E0GxDXQq7NfYFLe7GOeHa/EvxqyqYxT3Hg5V12B0IwzPrVsXNyxKaqzQf3UJe8j56p9gicF/OIz3iw0XLhUGWx81iFs1f9CbEsgks5NUlzyDKdc/rsFGmvbcNahGB+CwuFYiSFjG2KNpOmkCAhjAgMBAAECgYEAnJm5hgKqDw31Z9QUhsnpDCmMqUWKGhmBReCdaFbcV7jl6gfmIukSzliWXpABlbTQf7DvL6MhU3eeFpBUh77L83vrgkOyLEfLkBUrnhBuTRVojb+ytBLHaQsv4RZxIyPoNesZb8O7xYb3ABqPWAQYtJJXV/nCfP+scAxd9b7y7eECQQDh8ieJUVsEQYUVlm5YFTCFFndzZeV+X0sWui4PwSrpiGnVkQiz3scec/zwg8o9e8ONsW6QPRg+YyS+461WX+Z7AkEAtRMvi4+uig1bYJVmci7vrAlASJbpSX3fQOhmR26V1vurQ0PvGhoSXL3koWcSCT5jfMpKG8lp4qCIBAFidS71OQJBAMMJwU8rxyF5XWQxIrcuM1/u8NXQU7YulCbeN/yphl1ov9L3C0gZOlDzVphXazB/sWKSkxo3YsIX2xRcfLheuBkCQHpwlba+GlyZOY+ulk5hdIkU3FX5TZf3OC4wt3BX05RCKwVZ+2Tf+kih0uZcxrJfcHBibQgrAqFOwYpL0WLBtOkCQQDHlYgH9lpoM0ytJZb/EJNaa0maBB57YvP4wcc7uYLnQ0/epMxYPnlS48BLBPq3dAzRxZu7CgjpPOAUv28+oh9Z'

# # bs = base64.b64encode(gallui.encode("utf-8"))
# # print(bs)
# bbs = str(base64.b64decode(gallui))
# print(bbs) # 解码
# pk = str(base64.b64decode(msg), "utf-8")
# print(pk)
# # ----------------------------end




# gallui = 'HAz8dmtABxxYb19q2JzEmjYtzLX31QrM3B7lKGbhaeT/wd9meooh2dfUcQdpw1vXsp9GRfjPLEKjJas2PyL/Ra4DiOZ/oGoez1s7RoOtCflbp3mamegQh7TboVSGgP/ci+xnMTgrHRVwLYZMYro+QVyXMFmMujS/H5rSAwUMJpM='

# msg = 'MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBAJ/RJOOoRGHHbTH4wxdIThgi3E0GxDXQq7NfYFLe7GOeHa/EvxqyqYxT3Hg5V12B0IwzPrVsXNyxKaqzQf3UJe8j56p9gicF/OIz3iw0XLhUGWx81iFs1f9CbEsgks5NUlzyDKdc/rsFGmvbcNahGB+CwuFYiSFjG2KNpOmkCAhjAgMBAAECgYEAnJm5hgKqDw31Z9QUhsnpDCmMqUWKGhmBReCdaFbcV7jl6gfmIukSzliWXpABlbTQf7DvL6MhU3eeFpBUh77L83vrgkOyLEfLkBUrnhBuTRVojb+ytBLHaQsv4RZxIyPoNesZb8O7xYb3ABqPWAQYtJJXV/nCfP+scAxd9b7y7eECQQDh8ieJUVsEQYUVlm5YFTCFFndzZeV+X0sWui4PwSrpiGnVkQiz3scec/zwg8o9e8ONsW6QPRg+YyS+461WX+Z7AkEAtRMvi4+uig1bYJVmci7vrAlASJbpSX3fQOhmR26V1vurQ0PvGhoSXL3koWcSCT5jfMpKG8lp4qCIBAFidS71OQJBAMMJwU8rxyF5XWQxIrcuM1/u8NXQU7YulCbeN/yphl1ov9L3C0gZOlDzVphXazB/sWKSkxo3YsIX2xRcfLheuBkCQHpwlba+GlyZOY+ulk5hdIkU3FX5TZf3OC4wt3BX05RCKwVZ+2Tf+kih0uZcxrJfcHBibQgrAqFOwYpL0WLBtOkCQQDHlYgH9lpoM0ytJZb/EJNaa0maBB57YvP4wcc7uYLnQ0/epMxYPnlS48BLBPq3dAzRxZu7CgjpPOAUv28+oh9Z -----END RSA PRIVATE KEY-----'
# #  = "北京"
# # print(msg.encode(encoding = "utf-8"))#unicode编码转换为utf-8编码
# prikeyp = msg.encode(encoding = "utf-8").decode(encoding = "utf-8")  #unicode编码转换为utf-8编码，再转化为unicode编码+
# galluid = gallui.encode(encoding = "utf-8").decode(encoding = "utf-8")
# print(galluid)

# privkey = rsa.PrivateKey.load_pkcs1(prikeyp)
# uid = rsa.decrypt(galluid, privkey)



# gallui = 'HAz8dmtABxxYb19q2JzEmjYtzLX31QrM3B7lKGbhaeT/wd9meooh2dfUcQdpw1vXsp9GRfjPLEKjJas2PyL/Ra4DiOZ/oGoez1s7RoOtCflbp3mamegQh7TboVSGgP/ci+xnMTgrHRVwLYZMYro+QVyXMFmMujS/H5rSAwUMJpM='

# pubkeyp = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCf0STjqERhx20x+MMXSE4YItxNBsQ10KuzX2BS3uxjnh2vxL8asqmMU9x4OVddgdCMMz61bFzcsSmqs0H91CXvI+eqfYInBfziM94sNFy4VBlsfNYhbNX/QmxLIJLOTVJc8gynXP67BRpr23DWoRgfgsLhWIkhYxtijaTppAgIYwIDAQAB'

# pubkeyp = base64.b64decode(pubkeyp.encode())
# prikeyp = base64.b64decode(prikeyp.encode())

# # galluid = base64.b64decode(gallui)
# # base64.b64decode(b64_sign)
# print(pubkeyp.decode('gbk'))
# print(prikeyp)

# privkey = rsa.PrivateKey.load_pkcs1(prikeyp)

# uid = rsa.decrypt(gallui, privkey)
# print(uid)
# import base64
# from M2Crypto import BIO, RSA
 
# with open("public_key.pem", 'r') as f:
#     pubkey = f.read()
# with open("private_key.pem", 'r') as f:
#     prikey = f.read()
 
# # 加密
# text = "ABCDEF".encode('utf-8')  # 明文
# pub_bio = BIO.MemoryBuffer(pubkey.encode('utf-8'))  # 公钥字符串
# pub_rsa = RSA.load_pub_key_bio(pub_bio)  # 加载公钥
# secret = pub_rsa.public_encrypt(text, RSA.pkcs1_padding)  # 公钥加密
# sign = base64.b64encode(secret)  # 密文base64编码
# print(sign)
 
# # 解密
# b64_sign = "uhBqhevT0E5+WT++HX+pGzSy7YGskBQODuvoV+hf0k8cSyXG/GuAT4LKYaCiT9qiEGlbWxCIH51Qt1s0y2X56TbNja93AbzXiFWzsC2H6vwo3ZFcoj+YqUBsax+Gad0I6NME9lalpKsPtWqi4W/b3VbG5Mx+WBJ+L17GR7ZvWMo=" # base64密文
# cipher = base64.b64decode(b64_sign)  # base64解码
# pri_bio = BIO.MemoryBuffer(prikey.encode('utf-8'))  # 加载私钥
# pri_rsa = RSA.load_key_bio(pri_bio)
# plain = pri_rsa.private_decrypt(cipher, RSA.pkcs1_padding)  # 解密



# url = "http://192.168.0.114:20601/api/models?detail=true"
# resp = requests.get(url)
# model_data = resp.json()

# for mod in model_data["models"]:
#     print(mod["api_name"])
# str_time = '2020-11-17-02-21'

# struc_time = datetime.strptime(str_time, "%Y-%m-%d-%H-%M")
# struc_time = struc_time - timedelta(hours=8)
# strft_time = struc_time.strftime("%Y-%m-%dT%H:%M:%S.%f")

# print(strft_time)
# https://58.58.111.158:21054/api/upload?imageUrl=http://58.58.236.70:8000/upload/99000843117536/202008/99000843117536_20200813000030_2_res.jpg&dataType=4&comment=测试 ， 。中文标点符号&token=emh5YXBpOnpoeUB6eTkxMSM=
# https://58.58.111.158:21054/api/upload?imageUrl=http://58.58.236.70:8000/upload/99000843117536/202008/99000843117536_20200813000030_2_res.jpg&dataType=4&alarmType=2&comment=&token=emh5YXBpOnpoeUB6eTkxMSM=
# imgurl = "http://58.58.236.70:8000/upload/99000843117536/202008/99000843117536_20200813.jpg"
# comment = "测试 ， 。中文标点符号"
# # comment = "1"
# url = f"https://58.58.111.158:21054/api/upload?imageUrl={imgurl}&dataType=4&comment={comment}&token=emh5YXBpOnpoeUB6eTkxMSM="
# print(url)
# resp = requests.get(url, verify=False)
# print(resp.content)
# print(0 is None)


# # url = "https://58.58.111.158:21054/api/deviceList?token=emh5YXBpOnpoeUB6eTkxMSM="
# url = "https://58.58.111.158:21054/api/filterList?place=山东&from=0&size=20&token=emh5YXBpOnpoeUB6eTkxMSM="
# # url = "https://58.58.111.158:21054/api/filterList?deviceId=99000843075029&token=emh5YXBpOnpoeUB6eTkxMSM=&place=山东"
# # https://58.58.111.158:21054/api/deviceList?from=12&size=12&token=emh5YXBpOnpoeUB6eTkxMSM=&deviceId=99000843015645
# headers = {
#     "Content-Type": "application/json",
# }
# data = {
#     "_source": {"excludes": ["blob"]},
#     "track_total_hits": True,
#     "from": 0,
#     "size": 1,
#     "query": {"query_string": {"query": "*"}},
#     "sort": [{"@timestamp": {"order": "desc"}}]
# }

# resp = requests.get(url, headers=headers, verify=False)
# print(resp.json())


# print(9 // 900)
# for i in range(2):
#     print(8*(i))
#     print(8*(i+1))







# jsonpaht = r"C:\Users\Administrator\Desktop\pass"

# aim = r"C:\Users\Administrator\Desktop\paod"

# shutil.copytree(jsonpaht, aim) #oldfile和newfile都只能是文件

# image_path = r"C:\Users\Administrator\Desktop\xmls\198_20200410060104.JPEG"
# # 使用pillow读取图片，获取图片的宽和高
# img_pillow = Image.open(image_path)
# img_width = img_pillow.width # 图片宽度
# img_height = img_pillow.height # 图片高度
# # print("width -> {}, height -> {}".format(img_width, img_height))

# # img_cv = cv2.imread(image_path)
# # img_imageio = imageio.imread(image_path)
# # img_scipy = misc.imread(image_path)
# img_matplot = plt.imread(image_path)

# # print(img_cv.shape)
# # print(img_imageio.shape)
# # print(img_scipy.shape)
# print(img_matplot.shape[0])
# print(img_matplot.shape[1])
# print(img_matplot.shape[2])

# print(int('11000011', 2))
# bo = [{'tag': 'cementmixer', 'score': 1, 'warning': 0, 'reserved': 0, 'frame': {'x': 536.0, 'y': 550.0, 'width': 186.0, 'height': 87.0}, 'segmentation': []}, 
# {'tag': 'cementmixer', 'score': 1, 'warning': 0, 'reserved': 0,  'segmentation': []}]
# for i in bo:
#     i['color'] = "red"
# print(bo)
# path = '/data/data_manage/data/输电通道/2020-10-14/测试数据集/images/9900.jpg'
# folder_path = path.rsplit('/', 1)[0]
# print(folder_path)
# error_file_path = folder_path.replace('/images', '/error.txt')
# print(error_file_path)

# image_name = os.path.basename("/data/data_manage/data/输电通道/2020-10-14/测试数据集/images/9900.jpg")
# print(image_name)
# li = ['192.168.1.99_01_55 29.jpg', '_01_5529.jpg','192.168.1.jpg', 'birdnest.jpg', 'VID_20200417_114049 2.jpg', 'bir_dnest.jpg', '20200417_114049.jpg', '中文.jpg']
# for i in li:
#     filename = i.rsplit('.', 1)[0]
#     if not (re.match(r'[a-zA-Z0-9_]+$', filename) and not re.match(r'[_]', filename)):
#     # if ' ' or '.' in filename:
#         print(filename)

# path = {'ad': {}}
# def pa():
#     """
#     args: eee
#     returns: sdfaf
#     """
#     return 6

# print(help(pa))
# --------------------d当月1号
# datetime.date(datetime.date.today().year,datetime.date.today().month,1)
# #当月1号
# datetime.date.today().replace(day=1)
# #上月1号
# last = (datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1)
# print(datetime.date(datetime.date.today().year,datetime.date.today().month,1))
# print(type(datetime.date(datetime.date.today().year,datetime.date.today().month,1)))
# print(last)
# print(type(last))

# def test(dot):
#     with open(r"C:\Users\Administrator\Desktop\5699999999999.png", "wb")  as target:
#         target.write(dot)

# with open(r"C:\Users\Administrator\Desktop\tt12.jpg", "rb") as fp:
#     test(fp.read())

# paths = "/app/tools/ModelTrain/image"
# print(os.path.basename(paths))
# user_list = ["ad", "b", "c"]
# # print(user_list.index("b"))
# now_user_index = user_list.index("b")
# if (now_user_index + 1) >= len(user_list):
#     next_username = user_list[0]
# else:
#     next_username = user_list[now_user_index + 1]
# print(next_username)
# # ----------查找函数路径 用法-------------
# print(os.path.exists.__code__)
# print(os.__file__)
# # ----------查找函数路径 用法-------------
# # ----------list 用法-------------
# s = '123'
# print(list(s))  # ['1', '2', '3']
# print([s])

# # -------python 获取文件夹下文件个数----------
# # path_file_number=glob.glob('D:/case/test/testcase/checkdata/*.py')#或者指定文件下个数
# path_file_number=glob.glob(pathname='*.py') #获取当前文件夹下个数
# print(path_file_number)
# print(len(path_file_number))
# # ---------python 获取文件夹下文件个数  end ------------

# ----------从es 公有集获取数据----------
# publicset_url = "http://elastic:ELK@911$@58.58.111.158:20101/zhy-detect-pub/_search"

# headers = {
#     "Content-Type":"application/json",
# }

# data = {
#     "_source": {"excludes": ["blob"]},
#     "track_total_hits": True,
#     "from": 0,
#     "size": 10,
#     "query": {"query_string": {"query": "_id: COCO_train2014_000000332038_pub"}},
#     "sort": [{"@timestamp": {"order": "desc"}}]
#     }

# resp = requests.post(publicset_url,headers=headers, data=json.dumps(data))
# res_json = resp.json()

# img_detail = res_json['hits']['hits'][0]['_source']
# width = img_detail['width']
# height = img_detail['height']
# name = img_detail['name']
# annotations = img_detail['annotations']

# # 来 处理标注数据
# xml_ann = []
# json_ann = []
# for annotate in annotations:
#     # 判断数据是否超出范围
#     x = int(annotate["bbox"][0])
#     y = int(annotate["bbox"][1])
#     w = int(annotate["bbox"][2])
#     h = int(annotate["bbox"][3])

#     x = 0 if x < 0 else x
#     y = 0 if y < 0 else y

#     w = width if (x + w) > width else w
#     h = height if (y + h) > height else h

#     xml_ann_data = {
#         "tag": annotate["label"],
#         "score": 1,
#         "warning": 0,
#         "reserved": 0,
#         "frame": {
#             "x": x,
#             "y": y,
#             "width": w,
#             "height": h
#         },
#         "segmentation": []
#         }
#     xml_ann.append(xml_ann_data)

#     # 来 处理json
#     for seg in annotate["segmentation"]:
#         json_ann_data = {
#             "tag": annotate["label"],
#             "segmentation": seg
#             }
#         json_ann.append(json_ann_data)
# print(xml_ann)
# print(json_ann)

#----------------公有集end--------------

# # --------------- 缩略图 ---------------------
# img = r"C:\Users\Administrator\Desktop\tt.jpg"
# img2 = r"C:\Users\Administrator\Desktop\tt1.jpg"
# im=Image.open(img)
# print(im.format,im.size,im.mode)
# im.thumbnail((800,800))
# print(im.format,im.size,im.mode)
# im.save(img2,'JPEG')

# # ------------------ Python 连接 MongoDB -------------------
# #导入模块
# from pymongo import MongoClient
# #建立Mongodb数据库连接
# client=MongoClient('localhost',27017)
# #test为数据库
# db=client.app
# # 认证
# db.authenticate("tian", "123")
# #test为集合，相当于表名(没有的话会去创建的)
# collection=db.address
# #插入集合数据
# # collection.insert({"title":"test"})
# # 更新某个字段
# student = collection.find_one({'name': 'hu'})
# student['address'] = 'button'
# result = collection.update_one({'name': 'hu'}, {'$set': student})
# #打印集合中所有数据
# for item in collection.find():
#     print(item)
# #更新集合里的数据
# # collection.update({"title":"test"},{"title":"this is update test"})
# #关闭连接
# client.close()
# #!!!!其他操作
# #查找集合中单条数据
# #print collection.find_one()
# #删除集合collection中的所有数据
# #collection.remove()
# #删除集合collection
# #collection.drop()

# # -----------------gif 动图分解 暂时还没测试-------------
# import os
# from PIL import Image
# def analyseImage(path):
#   '''
#   Pre-process pass over the image to determine the mode (full or additive).
#   Necessary as assessing single frames isn't reliable. Need to know the mode
#   before processing all frames.
#   '''
#   im = Image.open(path)
#   results = {
#     'size': im.size,
#     'mode': 'full',
#   }
#   try:
#     while True:
#       if im.tile:
#         tile = im.tile[0]
#         update_region = tile[1]
#         update_region_dimensions = update_region[2:]
#         if update_region_dimensions != im.size:
#           results['mode'] = 'partial'
#           break
#       im.seek(im.tell() + 1)
#   except EOFError:
#     pass
#   return results


# def processImage(path):
#   '''
#   Iterate the GIF, extracting each frame.
#   '''
#   mode = analyseImage(path)['mode']
#   im = Image.open(path)
#   i = 0
#   p = im.getpalette()
#   last_frame = im.convert('RGBA')
#   try:
#     while True:
#       print("saving %s (%s) frame %d, %s %s") % (path, mode, i, im.size, im.tile)
#       '''
#       If the GIF uses local colour tables, each frame will have its own palette.
#       If not, we need to apply the global palette to the new frame.
#       '''
#       if not im.getpalette():
#         im.putpalette(p)
#       new_frame = Image.new('RGBA', im.size)
#       '''
#       Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
#       If so, we need to construct the new frame by pasting it on top of the preceding frames.
#       '''
#       if mode == 'partial':
#         new_frame.paste(last_frame)
#       new_frame.paste(im, (0,0), im.convert('RGBA'))
#       new_frame.save('%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')
#       i += 1
#       last_frame = new_frame
#       im.seek(im.tell() + 1)
#   except EOFError:
#     pass
# def main():
#   processImage(r'C:\Users\Administrator\Desktop\333.gif')
# if __name__ == "__main__":
#   main()

# ------------------图片的二进制编码---------------
# img = b"C:\Users\Administrator\Desktop\111\\1.png"
# p = base64.b64encode(img)
# print(p)

# with open(r"C:\Users\Administrator\Desktop\111\\998.jpg", "wb") as fp:
#     fp.write(imageData)
# 图片转base64

# 能用
# with open(r"C:\Users\Administrator\Desktop\dwdwd\images\99000843025114_20200715163602.jpg","rb") as f:  # 二进制方式打开图文件
#     base64_str = base64.b64encode(f.read())  # base64编码
#     # print(base64_str)
#     # print(type(base64_str))
#     # print(str(base64_str).replace("b'", "").replace("'", ""))
#     # print(type(str(base64_str).replace("b'", "")))
#     dir = {
#         "imageData": str(base64_str).replace("b'", "").replace("'", "")
#     }
#     fol = json.dumps(dir)
#     with open(r"C:\Users\Administrator\Desktop\66.json", "w") as aass:
#         aass.write(fol)

# ------------------python  压缩 -----------------------------
# 归档函数：make_archive()

# 　　语法：shutil.make_archive(base_name, format, base_dir)

# 　　　　　base_name ---> 创建的目标文件名，包括路径，减去任何特定格式的扩展

# 　　　　　format        ---> 压缩包格式后缀：zip、tar、bztar、gztar

# 　　　　　base_dir     ---> 开始打包的路径

# 　　返回值：返回打包文件的绝对路径和名称

# 复制代码
# 1 import shutil
# 2 # 将path_1处的文件归档到path_2处
# 3 path_1 = r'C:\Users\hasee\Desktop\test007'
# 4 path_2 = r'C:\Users\hasee\Desktop\new'
# 5 new_path = shutil.make_archive(path_2, 'zip', path_1)
# 6 print(new_path)
# 7 --->C:\Users\hasee\Desktop\new.zip
# path1 = r"C:\Users\Administrator\Desktop\xmls"
# path2 = r"C:\Users\Administrator\Desktop\new"

# shutil.make_archive(path2, "zip", path1)


# # -------- 先来个复杂的

# # 这个是新建一个全新的xml文件
# domT = minidom.Document()
# # impl = minidom.getDOMImplementation()
# # domT = impl.createDocument(None, None, None)
# # 在xml里面追加一些元素信息
# # domT = parse(r"C:\Users\Administrator\Desktop\look.xml")
# # 文档根元素
# # rootNode = domT.documentElement
# '''
# ①创建一个新元素结点createElement()
# ②创建一个文本节点createTextNode()
# ③将文本节点挂载元素结点上
# ④将元素结点挂载到其父元素上。'''

# # 新建一个节点 就叫annotation 根节点或者一级节点
# annotation_node = domT.createElement("annotation")
# domT.appendChild(annotation_node)
# # 创建二级节点 folder 设置text value
# folder_node = domT.createElement("folder")
# annotation_text_value = domT.createTextNode("kavin")
# folder_node.appendChild(annotation_text_value)  # 把文本节点挂到name_node节点
# annotation_node.appendChild(folder_node)
# # f = open(r'C:\Users\Administrator\Desktop\look.xml', "w")
# # domT.writexml(f, indent='', addindent='\n', encoding='utf-8')
# # f.close()
# # 创建二级节点 filename path segmented  具有三级节点的 source size object
# filename_node = domT.createElement("filename")
# filename_text_value = domT.createTextNode("kavin")
# filename_node.appendChild(filename_text_value)
# annotation_node.appendChild(filename_node)

# path_node = domT.createElement("path")
# path_text_value = domT.createTextNode("kavin")
# path_node.appendChild(path_text_value)
# annotation_node.appendChild(path_node)

# segmented_node = domT.createElement("segmented")
# segmented_text_value = domT.createTextNode("0")
# segmented_node.appendChild(segmented_text_value)
# annotation_node.appendChild(segmented_node)

# source_node = domT.createElement("source")
# annotation_node.appendChild(source_node)

# size_node = domT.createElement("size")
# annotation_node.appendChild(size_node)

# # 来三级节点 database width height depth


# database_node = domT.createElement("database")
# database_text_value = domT.createTextNode("Unkonwn")
# database_node.appendChild(database_text_value)
# source_node.appendChild(database_node)

# width_node = domT.createElement("width")
# width_text_value = domT.createTextNode("kavin")
# width_node.appendChild(width_text_value)
# size_node.appendChild(width_node)

# height_node = domT.createElement("height")
# height_text_value = domT.createTextNode("kavin")
# height_node.appendChild(height_text_value)
# size_node.appendChild(height_node)

# depth_node = domT.createElement("depth")
# depth_text_value = domT.createTextNode("kavin")
# depth_node.appendChild(depth_text_value)
# size_node.appendChild(depth_node)

# for i in range(2):
#     object_node = domT.createElement("object")
#     annotation_node.appendChild(object_node)
#     # 三级重要节点  name pose truncated difficult bndbox 
#     name_node = domT.createElement("name")
#     name_text_value = domT.createTextNode("kavin")
#     name_node.appendChild(name_text_value)
#     object_node.appendChild(name_node)

#     pose_node = domT.createElement("pose")
#     pose_text_value = domT.createTextNode("kavin")
#     pose_node.appendChild(pose_text_value)
#     object_node.appendChild(pose_node)

#     truncated_node = domT.createElement("truncated")
#     truncated_text_value = domT.createTextNode("0")
#     truncated_node.appendChild(truncated_text_value)
#     object_node.appendChild(truncated_node)

#     difficult_node = domT.createElement("difficult")
#     difficult_text_value = domT.createTextNode("0")
#     difficult_node.appendChild(difficult_text_value)
#     object_node.appendChild(difficult_node)

#     bndbox_node = domT.createElement("bndbox")
#     object_node.appendChild(bndbox_node)

#     # 四级节点 xmin ymin xmax ymax
#     xmin_node = domT.createElement("xmin")
#     xmin_text_value = domT.createTextNode("kavin")
#     xmin_node.appendChild(xmin_text_value)
#     bndbox_node.appendChild(xmin_node)

#     ymin_node = domT.createElement("ymin")
#     ymin_text_value = domT.createTextNode("kavin")
#     ymin_node.appendChild(ymin_text_value)
#     bndbox_node.appendChild(ymin_node)

#     xmax_node = domT.createElement("xmax")
#     xmax_text_value = domT.createTextNode("kavin")
#     xmax_node.appendChild(xmax_text_value)
#     bndbox_node.appendChild(xmax_node)

#     ymax_node = domT.createElement("ymax")
#     ymax_text_value = domT.createTextNode("kavin")
#     ymax_node.appendChild(ymax_text_value)
#     bndbox_node.appendChild(ymax_node)

# with open(r'C:\Users\Administrator\Desktop\lo.xml', "w") as f:
# # 缩进 - 换行 - 编码
#     domT.writexml(f, indent='', addindent='\t', newl='\n',encoding='utf-8')

# from xml.dom import minidom 
# import traceback 
# try: 
#     f = open(r'C:\Users\Administrator\Desktop\look.xml', "w") 
#     try: 
#         doc = minidom.Document() 
#         rootNode = doc.createElement("root") 

#         doc.appendChild(rootNode) 

#         bookNode = doc.createElement("book") 
#         bookNode.setAttribute("isbn", "34909023") 
#         rootNode.appendChild(bookNode) 
#         authorNode = doc.createElement("author") 
#         bookNode.appendChild(authorNode) 
#         authorTextNode = doc.createTextNode("dikatour") 
#         authorNode.appendChild(authorTextNode) 
#         doc.writexml(f, indent='', addindent='\t', encoding='utf-8') 
#     except: 
#         print(666)
#     finally: 
#         f.close() 
# except IOException:
#     print("open file failed")

# -----------------------------------
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)

# def Decrypt(key:str, text:str) -> str:
#   if len(key) < 32: key += ' ' * (32 - len(key))
#   elif len(key) > 32: key = key[0:32]
#   cipher = AES.new(bytes(key,encoding='utf-8'), AES.MODE_CBC, bytes(AES.block_size))
#   return str(gzip.decompress(bytes.strip(cipher.decrypt(base64.b64decode(text)))), encoding='utf-8')


# def Pass(id, priv_key):
#   prefix = str(id) + str(int(time.time()))
#   pub_key = prefix + md5(bytes(prefix + priv_key, 'utf8')).hexdigest()
#   print('恭喜通过第%d关,通关公钥:%s' % (id, pub_key))

# key=input('1+1=')
# exec(Decrypt(key,'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'))

# import json
# import os
# from datetime import datetime
# # enti = {
# #     "id": "look",
# #     "ping": "noting"
# # }
# # enti["point"] = [{
# #     "id": "look",
# #     "ping": "noting"
# # },
# # {
# #     "id": "look",
# #     "ping": "noting"
# # },
# # ]
# # print(enti)
# # for i in []:
# #     print(i) 20200603160735
# # print(os.path.dirname(r"D:\新建文件夹\例外\6.Flask课件\6.Flask课件\黑马头条项目课件"))
# # dt = datetime.now()  
# # # dt = dt.strftime('%Y%m%d%H%M%S')
# # dt = dt.strftime('%H')
# # print(dt)
# pp = r"D:\新建文件夹\例外\6.Flask课件\6.Flask课件\黑马头条项目课件"
# for i in os.listdir(pp):
#     print(os.path.join(pp, i))

