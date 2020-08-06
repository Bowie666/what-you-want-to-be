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


# ------------------ Python 连接 MongoDB -------------------
#导入模块
from pymongo import MongoClient
#建立Mongodb数据库连接
client=MongoClient('localhost',27017)
#test为数据库
db=client.app
# 认证
db.authenticate("tian", "123")
#test为集合，相当于表名(没有的话会去创建的)
collection=db.address
#插入集合数据
# collection.insert({"title":"test"})
# 更新某个字段
student = collection.find_one({'name': 'hu'})
student['address'] = 'button'
result = collection.update_one({'name': 'hu'}, {'$set': student})
#打印集合中所有数据
for item in collection.find():
    print(item)
#更新集合里的数据
# collection.update({"title":"test"},{"title":"this is update test"})
#关闭连接
client.close()
#!!!!其他操作
#查找集合中单条数据
#print collection.find_one()
#删除集合collection中的所有数据
#collection.remove()
#删除集合collection
#collection.drop()

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

