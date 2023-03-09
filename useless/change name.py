#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2022/1/26 14:46


import os
import re
"""批量修改文件夹的图片名"""
def ReFileName(dirPath,pattern):
    """
    :param dirPath: 文件夹路径
    :pattern:正则

    :return:
    """
    # 对目录下的文件进行遍历
    i = 900001
    for file in os.listdir(dirPath):
        # 判断是否是文件

        if os.path.isfile(os.path.join(dirPath, file)) == True:
           #c= os.path.basename(file)
           a = file.split('.')
           newName = str(i) +'.xml'
           # 重命名
           os.rename(os.path.join(dirPath, file), os.path.join(dirPath, newName))
           i+=1
    print("图片名已全部修改成功")

if __name__ == '__main__':

    dirPath = r"C:\Users\吴世龙\Desktop\抠图标注\Annotations"
    pattern = re.compile(r'.*')
    ReFileName(dirPath,pattern)

