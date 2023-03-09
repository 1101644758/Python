#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2022/3/17 14:34

import os
import shutil


#剪切
def move(read_path, move_path):
    total_file = os.listdir(read_path)
    num = len(total_file)
    k = 0
    for i in range(num):
        # print(total_file[i][0])
        if total_file[i][0] == '4':
            # print(total_file[i])
            com_path = os.path.join(read_path, total_file[i])
            shutil.move(com_path, move_path)
            k += 1
    print('%s images have been moved!' % k)

# 删除txt某些行
def del_line(file_path):
    l = []
    k = 0
    with open(file_path, 'r') as f:
        lines =  f.readlines()
        # print(lines)
        for line in lines:
            img_name = line.split('/')[2].strip()
            if img_name[0] != '4':
                l.append(img_name)
            else:
                k += 1
    # print(l)
    with open('test.txt', 'w') as f:
        num = len(l)
        for i in range(num):
            f.write('data/images/%s\n' % l[i])
    print('%s imgs have been deleted' % k)



if __name__ == '__main__':
    read_path = r"C:\Users\吴世龙\Desktop\images_without_fire"
    move_path = r"C:\Users\吴世龙\Desktop\total_fire"
    file_path = r"C:\Users\吴世龙\Desktop\test.txt"
    # move(read_path, move_path)
    del_line(file_path)






# 复制
# 读取图片的路径
# read_path = r"C:\Users\吴世龙\Desktop\0903test"
# # read_path = r"C:\Users\吴世龙\Desktop\测试小图标注-无空白标签"
# # 存放图片的路径
# save_path = r"C:\Users\吴世龙\Desktop\有目标文件\JPEGImages"
# # save_path = r"C:\Users\吴世龙\Desktop\151后有目标小图\Annotations"
# # save_path = r"C:\Users\吴世龙\Desktop\有目标文件\labels"
# if not os.path.exists(save_path):
#     os.mkdir(save_path)
# #fileType = '.JPG'
# num = 0
# # 读取并遍历读取txt中的每行
# with open(r'C:\Users\吴世龙\Desktop\xml_list.txt', 'r') as f:
#     for name in f:
#         fileName = name.strip()  # 去除末尾的换行
#         fileName = fileName + '.jpg'
#         # fileName = fileName + '.xml'
#         # print(fileName)
#         # print(type(fileName)) # 查看文件类型
#
#         # 读取并遍历文件夹中的图片
#         for file in os.listdir(read_path):
#             # print(file)
#             # print(type(file))
#
#             if fileName.upper() == file.upper():
#                 num += 1
#                 shutil.copy(os.path.join(read_path, fileName ), save_path)
#                 print("%s Copy successfully" % (fileName ))
#     print("Copy complete!")
#     print("Total pictures copied:", num)


#删除txt中的文件
# num = 0
# with open(r'C:\Users\吴世龙\Desktop\object.txt', 'r') as c:
#     for name in c:
#         filename = name.strip() + '.jpg'                #去除换行
#         # filename = filename + '.jpg'
#         for file in os.listdir(read_path):
#             if file == filename:
#                 num += 1
#                 delpath = os.path.join(read_path, file)
#                 # delpath = read_path+r'\\'+file
#                 os.remove(delpath)
#     print(num,'files have been deleted')

