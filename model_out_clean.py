"""
modle_out_clean是将yolov3输出的valid文件 进行class值的筛选 通过改变不同的阀值可以得到PR图
@author: XP
"""


def readfile(filename,train_list):
    fo = open(filename, "r")  # 读入标注结果集
    while True:
        key = next(fo, -1)
        if key == -1:
            break;
        key = key.split(" ")
        num = float(key[1])                                                   #class 值 
        if num > 0.9:																#可以通过改变不同的阀值得到PR图
            list.write(key[0]+' '+key[1]+' '+key[2]+' '+key[3]+' '+key[4]+' '+key[5])


    fo.close()
filename = "F:/comp4_det_test_face.txt"                    #yolov3输出的valid文件
list = open('modle_out_clean.txt', 'w')                          # 将晒出来的结果写入文件
readfile(filename,list)
