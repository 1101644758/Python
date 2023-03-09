# python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2022/9/22 9:57

import os
import hashlib

def get_md5(file):
    file = open(file, 'rb')
    md5 = hashlib.md5(file.read())
    file.close()
    md5_values = md5.hexdigest()
    return md5_values

if __name__ == '__main__':
    i = 0
    file_path = r'E:\test\base\chap16-crawl\images1'
    os.chdir(file_path)                            #改变当前工作目录到指定路径
    file_list = os.listdir(file_path)
    md5_list = []
    for file in file_list:
        md5 = get_md5(file)
        if md5 not in md5_list:
            md5_list.append(md5)
        else:
            os.remove(file)
            i += 1

    print(i, 'images have been removed!')