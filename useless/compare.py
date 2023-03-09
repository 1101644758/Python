# python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2022/9/3 16:45

import os

# image_path = r"C:\Users\吴世龙\Desktop\标注_1\JPEGImages"
xml_path = r"C:\Users\吴世龙\Desktop\501"
# save_path = r"C:\Users\吴世龙\Desktop\标注_1"
# image_name = os.listdir(image_path)
xml_name = os.listdir(xml_path)
num = 0
# num1 = len(image_name)
# num2 = range(num1)
num3 = len(xml_name)
num4 = range(num3)
fxml = open(r'C:\Users\吴世龙\Desktop\xml_list.txt','w')
#
#
# for i in num2:
#     name = image_name[i][:-4] + '.txt'
#     file = open(os.path.join(save_path, name),'w')
#     file.close()
#
for i in num4:
    name = xml_name[i][:-4] + '\n'
    fxml.write(name)
fxml.close()

# with open(r'C:\Users\吴世龙\Desktop\标注_1\del.txt', 'r') as c:
#     for name in c:
#         filename=name.strip()
#         for file in os.listdir(save_path):
#             if file == filename:
#                 num += 1
#                 delpath = os.path.join(save_path, file)
#                 os.remove(delpath)
#     print(num,'files have been deleted')

# num = 0
# read_path = r"C:\Users\吴世龙\Desktop\煜邦测试原图标注1"
# with open(r'C:\Users\吴世龙\Desktop\object.txt', 'r') as c:
#     for name in c:
#         filename = name.strip()                #去除换行
#         filename = filename + '.jpg'
#         for file in os.listdir(read_path):
#             if file == filename:
#                 num += 1
#                 # delpath = os.path.join(read_path, file)
#                 delpath = read_path+r'\\'+file
#                 os.remove(delpath)
#     print(num,'files have been deleted')
