# python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2022/9/3 16:39

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
# sets = ['train', 'test','val']
sets = ['train']
classes = ['tower crane','crane','construction machinery','foreign object','fire and smoke']
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
def convert_annotation(image_id):
    # in_file = open('data/Annotations/%s.xml' % (image_id))
    out_file = open('data/labels/%s.txt' % (image_id), 'w')
    in_file = open(r"C:\Users\吴世龙\Desktop\第二批小图\Annotations\%s.xml" % (image_id), encoding= 'UTF-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)             #index返回指定元素的序列
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('data/labels/'):
        os.makedirs('data/labels/')
    # image_ids = open('data/ImageSets/%s.txt' % (image_set)).read().strip().split()
    image_ids = open(r"C:\Users\吴世龙\Desktop\%s.txt" % (image_set)).read().strip().split()
    list_file = open('data/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('data/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
