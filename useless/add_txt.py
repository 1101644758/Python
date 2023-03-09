import os

def add_txt(input_path, add_path):
    l = []
    k = 0
    with open(input_path, 'r') as f:
        line = f.readline()
        while line:
            img_name = line.strip()
            l.append(img_name)
            line = f.readline()
        num = len(l)

    with open(add_path, 'a') as f:
        for i in range(num):
            img_path = l[i]
            f.write('data/images/%s.jpg\n' % img_path)
            k += 1
        l.clear()
    print('%s images have been added' % k)


if __name__ == '__main__':
    sets = ['train', 'val', 'test']
    for set in sets:
        input_path = r'/home/dell/ZJC/datasets/重新整理230228/公司/小图/initial_data/ImageSets自爬/%s.txt' % set
        add_path = '%s.txt' % set
        add_txt(input_path, add_path)
    print('finish')

