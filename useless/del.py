#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2022/4/11 16:16

import os

read_path= r"C:\Users\吴世龙\Desktop\毕设实验\test.txt"
del_path= r"E:\test\yolov5-v2.0\data\JPEGImages"
num= 0
f= open(read_path)
line= f.readline()
list= []
while line:
    a= line.split('/')#按/分隔开
    b= a[2:]
    list.append(b)
    line= f.readline()  #读取下一行
f.close

#print(list)
with open(r'C:\Users\吴世龙\Desktop\毕设实验\base test\test.txt', 'w') as e:
    for l in list:
        s=''.join(l)
        e.write(s)

with open(r'C:\Users\吴世龙\Desktop\毕设实验\base test\test.txt', 'r') as c:
    for name in c:
        filename=name.strip()
        for file in os.listdir(del_path):
            if file.upper() == filename.upper():
                num+=1
                delpath=del_path+r'\\'+file
                os.remove(delpath)
    print(num,'files have been deleted')











