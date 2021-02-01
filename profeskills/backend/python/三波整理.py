# 牛啤开始
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.etree.ElementTree as ET
from pprint import pprint

class XmlOperat(object):
    def read1_xml(path):
        #打开xml文档
        dom = minidom.parse(path)

        #得到文档元素对象
        root = dom.documentElement
        print(root.nodeName)

        # 所有标注数据
        obj_info = root.getElementsByTagName("object")
        for obj in obj_info:

            name = obj.getElementsByTagName(i)[0]
            print(name.childNodes[0].data)

            ann = obj.getElementsByTagName("xmin")[0]
            print(ann.childNodes[0].data)

    def read2_xml(path):
        # dom = ET.parse(path)

        # data = {}
        # data['name'] = dom.findall('filename')[0].text
        # data['annotations'] = []
        # obj_list = dom.findall('object')
        # for obj in obj_list:
        #     frame_data = [float(box.text)
        #                   for box in obj.findall('bndbox')[0].getchildren()]
        #     data['annotations'].append({
        #         'tag': obj.findall('name')[0].text,
        #         'frame': {
        #             'x': frame_data[0],
        #             'y': frame_data[1],
        #             'width': frame_data[2] - frame_data[0],
        #             'height': frame_data[3] - frame_data[1]
        #         }
        #     })
        # print(data)
        dom = ET.parse(path)
        data = []
        obj_list = dom.findall('object')
        for obj in obj_list:
            frame_data = [float(box.text) for box in obj.findall('bndbox')[0].getchildren()]
            data.append({
                'tag': obj.findall('name')[0].text,
                'frame': {
                    'x': frame_data[0],
                    'y': frame_data[1],
                    'width': frame_data[2] - frame_data[0],
                    'height': frame_data[3] - frame_data[1]
                }
            })
        pprint(data)

# path = r'C:\Users\Administrator\Desktop\承德供电公司@河宽线014号（小号侧）@09-01-41@99000843024054_20190410072702.xml'
path = r'C:\Users\Administrator\Desktop\测试创建数据集\xmls\99000843150926_20201014152802.xml'
XmlOperat.read2_xml(path)