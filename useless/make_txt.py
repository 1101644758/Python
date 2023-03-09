import os


def make_txt(name):
    path = r'/home/dell/wsl/1/yolov5-v6.0/data/s_images/images/%s' % name
    total_imgs = os.listdir(path)
    num = len(total_imgs)
    k = 0
    with open('%s.txt' % name, 'w') as f:
        for i in range(num):
            if total_imgs[i].endswith(',jpg'):
                img_name = total_imgs[i][:-4]
                f.write('data/images/%s.jpg\n' % img_name)
                k += 1
        total_imgs.clear()
    print(k)

if __name__ == '__main__':
    sets = ['train', 'val', 'test']
    for set in sets:
        make_txt(set)



#
#
# train_path = r'/home/dell/wsl/1/yolov5-v6.0/data/s_images/images/train'
# total_train = os.listdir(train_path)
# train_num = len(total_train)
# k = 0
# with open('train.txt', 'w') as f:
#     for i in range(train_num):
#         name = total_train[i][:-4]
#         f.write('data/images/%s.jpg\n' % name)
#         k += 1
# print(k)
#
# val_path = r'/home/dell/wsl/1/yolov5-v6.0/data/s_images/images/val'
# total_val = os.listdir(val_path)
# val_num = len(total_val)
# k = 0
# with open('val.txt', 'w') as f:
#     for i in range(val_num):
#         name = total_val[i][:-4]
#         f.write('data/images/%s.jpg\n' % name)
#         k += 1
# print(k)

# test_path = r'/home/dell/wsl/1/yolov5-v6.0/data/s_images/images/test'
# total_test = os.listdir(test_path)
# test_num = len(total_test)
# k = 0
# with open('test.txt', 'w') as f:
#     for i in range(test_num):
#         name = total_test[i][:-4]
#         f.write('data/images/%s.jpg\n' % (name))
#         k += 1
# print(k)





