import os
import shutil

from pymongo import MongoClient

folder = '/data/data_manage'
target_folder = '/home/xuwei/road/images'
target_folder_xml = '/home/xuwei/road/xmls'

if not os.path.exists(target_folder):
    os.mkdir(target_folder)
if not os.path.exists(target_folder_xml):
    os.mkdir(target_folder_xml)

client = MongoClient('127.0.0.1', 27017)
db = client['app']
db.authenticate('tian', '123')
imageCollect = db.image

for sc in ['高速公路', '公路']:
    imageResult = imageCollect.find({'sence_name': sc})

    for result in imageResult:
        # 找path 拼接路径
        imgPath = result['path']
        print(imgPath)
        image_abs_path = os.path.join(folder, imgPath)
        xmlPath = image_abs_path.replace('/images', '/xmls').replace('.jpg', '.xml')
        # 移动图片和xml
        shutil.copy(image_abs_path, target_folder)
        shutil.copy(xmlPath, target_folder_xml)
