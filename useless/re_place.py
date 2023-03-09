# python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2023/3/4 15:24

import os

limg_path = r"C:\Users\吴世龙\Desktop\images"
simg_path = r"C:\Users\吴世龙\Desktop\JPEGImages"
total_limg = os.listdir(limg_path)
total_simg = os.listdir(simg_path)
l_num = len(total_limg)
s_num = len(total_simg)
l = []
k = 0

for i in range(l_num):
    l.append(total_limg[i][:6])
# print(l)

for i in range(s_num):
    if total_simg[i][:6] not in l:
        delpath = os.path.join(simg_path, total_simg[i])
        os.remove(delpath)
        k +=1

print(k, 'files have been deleted')


