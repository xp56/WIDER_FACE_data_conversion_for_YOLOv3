"""
train_list将标注文件转成yolov3所需要的train_list列表
@author: XP
"""

def readfile(filename,train_list):
    fo = open(filename, "r")  # 读入标注结果集
    while True:
        key = next(fo, -1)
        if key == -1:
            break;
        key = key.replace('\n', '').split("/")
        key = key[-1]
        train_list.write("/darknet/data/images/"+key+"\n")           #写入图片位置
        num = int(next(fo, -1))
        for i in range(num):
            next(fo, -1)
        print(key)

    fo.close()
filename = "F:/WIDER_FACE/wider_face_split/wider_face_split/wider_face_train_bbx_gt.txt"
train_list = open('My_labels/train.txt', 'w')
readfile(filename,train_list)
