# python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2023/3/6 21:08

import os

# img_path = r"C:\Users\吴世龙\Desktop\第一批小图\JPEGImages"
img_path = r"C:\Users\吴世龙\Desktop\第二批小图\JPEGImages"
n = 0
total_img = os.listdir(img_path)
num = len(total_img)
with open(r"C:\Users\吴世龙\Desktop\train.txt", 'w') as f:
    for i in range(num):
        dir_name = total_img[i][:-4] + '\n'
        f.write(dir_name)
        n += 1

print(n)


