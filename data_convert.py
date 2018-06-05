"""
data_conversion.py 是将 wider_faced的标注数据集转成yolov3所需要的labels
- 每个图片转成对应名称的label
- 由于yolov3需要的是归一化之后的中心坐标和w，h所以在convert方法中进行了归一化和数据转换
@author: XP
"""
import cv2

def convert(size, box):                 #size是图片尺寸 box是坐标
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def readfile(filename):
    fo = open(filename, "r")  # 读入标注结果集
    while True:
        key = next(fo, -1)
        if key == -1:
            break;
        key = key.replace('\n', '')
        key1 = key.split("/")
        key1 = key1[1].split(".")
        key1 = key1[0]         #获取图片名称
        list_file = open('My_labels/%s.txt' % (key1), 'w')                                             #新建对应图片的label，存放在My_labels文件夹下
        value = []
        key = "F:/WIDER_FACE/WIDER_train/WIDER_train/images/%s"%(key) 	#该图片位置
        # print(key)
        image = cv2.imread(key)																						#用opencv读取该图片
        image_size = []																							
        # print(image.shape[0],image.shape[1])
        image_size = [image.shape[1],image.shape[0]]											#得到图片尺寸，为了后面进行归一化
        num = next(fo, -1)
        for i in range(int(num)):																					#遍历每一张标注的脸
            value = next(fo, -1).split(' ')
            box = [int(value[0]),int(value[0])+int(value[2]),int(value[1]),int(value[1])+int(value[3])]
            x, y, w, h = convert(image_size,box)
            # print(x, y, w, h)
            list_file.write('0 %s %s %s %s\n' % (x,y,w,h))									#将转换后的坐标写入label

    fo.close()
filename = "C:/Users/XP/Desktop/yolo/数据标注/wider_face_train_bbx_gt.txt"    #标注文件位置
readfile(filename)