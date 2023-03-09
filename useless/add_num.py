# python 3.8
# -*- coding: utf-8 -*-
# author：wsl time:2023/2/20 21:32

import os
import numpy as np

xmlfilepath= r"C:\Users\吴世龙\Desktop\readata\labels"
total_xml= os.listdir(xmlfilepath)
# print(total_xml)
num= len(total_xml)
# print(num)
os.chdir(xmlfilepath)        #更改工作地址
l= []
cls= []
#批量定义动态变量名
class_all= 0
for i in range(11):
    locals()[f'class_{i}']= 0
    for n in range(11):
        if n > i:
            locals()[f'cls{i}_{n}']= 0
# print(cls2_9)



for i in range(num):
    # print(i)
    name = total_xml[i]
    # print(name)
    with open(name, 'r') as f:
        lines= f.readlines()
        for line in lines:
            a= line.strip().split()
            b= int(a[0])
            l.append(b)
        print(l)
        # len_all = l.count(0)
        # class_0+= len_all
        # len_all = l.count(1)
        # class_1+= len_all
        # len_all = l.count(2)
        # class_2+= len_all
        # len_all = l.count(3)
        # class_3+= len_all
        # len_all = l.count(4)
        # class_4+= len_all
        # len_all = l.count(5)
        # class_5+= len_all
        # len_all = l.count(6)
        # class_6+= len_all
        # len_all = l.count(7)
        # class_7+= len_all
        # len_all = l.count(8)
        # class_8+= len_all
        # len_all = l.count(9)
        # class_9+= len_all
        # len_all = l.count(10)
        # class_10+= len_all
        # print(class_7)

        #类别计数
        for n in range(11):
            len_cls= l.count(n)
            locals()[f'class_{n}']+= len_cls

        #共现计数
        for j in range(11):
            for k in range(11):
                if k > j:
                    if j in l and k in l:
                        locals()[f'cls{j}_{k}']+= 1
        l.clear()
        # print(0 in l and i in l)
        # print(cls8_9)

for i in range(11):
    class_all+= locals()[f'class_{i}']
    cls.append(locals()[f'class_{i}'])

# print(cls, class_all)
# print(cls4_7)

mat = np.identity(11, dtype= int)                  #构建单位矩阵
mat_trans= np.identity(11, dtype= int)
# mat[3][2]= 11
# print(mat)
# print(mat[0][0])

for i in range(11):
    for j in range(11):
        if j > i:
            mat[i][j]= locals()[f'cls{i}_{j}']
            mat_trans[i][j]= locals()[f'cls{i}_{j}']
            mat_trans[j][i]=  mat[i][j]
print(mat)

with open(r"C:\Users\吴世龙\Desktop\readata\re_sum.txt", 'w') as f:
    f.writelines('total_bbox='+ str(class_all)+ '\n')
    f.writelines('\n')
    f.writelines(str(cls).strip('[').strip(']')+ '\n')
    f.writelines('\n')
    f.writelines('\x20'+str(mat).replace('[','').replace(']', '')+ '\n')   #\x20：空格
    f.writelines('\n')
    f.writelines('\x20' + str(mat_trans).replace('[', '').replace(']', '') + '\n')







