"""
count_IOU 是进行检测结果与标注结果的IOU计算，并得到精确率召回率
@author: XP
"""
def calcIOU(x1, y1, w1, h1, x2, y2, w2, h2):  #传入连个人脸框的坐标进行 对比输出两个框的重复度

    if((abs(x1 - x2) < ((w1 + w2)/ 2.0)) and (abs(y1-y2) < ((h1 + h2)/2.0))):
        left = max((x1 - (w1 / 2.0)), (x2 - (w2 / 2.0)))
        upper = max((y1 - (h1 / 2.0)), (y2 - (h2 / 2.0)))

        right = min((x1 + (w1 / 2.0)), (x2 + (w2 / 2.0)))
        bottom = min((y1 + (h1 / 2.0)), (y2 + (h2 / 2.0)))

        inter_w = abs(left - right)
        inter_h = abs(upper - bottom)
        inter_square = inter_w * inter_h
        union_square = (w1 * h1)+(w2 * h2)-inter_square

        b = inter_square/union_square * 1.0
        #b=calcIOU
        #print("calcIOU:", b)
    else:
        b=0
        #print("calcIOU:", b)
    return b

    
#************************************************************#
fo = open("F:/WIDER_FACE/wider_face_split/wider_face_split/wider_face_val_bbx_gt.txt", "r")  #读入原标注结果集
dict = {}
while True:
    key = next(fo,-1)

    if key == -1:
        break;
    value = []
    num = next(fo,-1)
    value.append(int(num))
    for i in range(int(num)):
        value.append(next(fo,-1).replace('\n','').split(' ',))
    key = key.replace('\n', '').split("/")
    key = key[1]
    dict[key] = value

fo.close()

#************************************************************#

fo1= open("C:/Users/XP/Desktop/yolo/数据标注/label.txt", "r")   #读入模型输出结果集
# fo1= open("F:/数据/face_recognition/aDir_val.txt", "r")
dict1 = {}
while True:
	key = next(fo1,-1)
	if key == -1:
		break;

	value1 = []
	num1 = next(fo1,-1)
	value1.append(int(num1))
	for i in range(int(num1)):
		value1.append(next(fo1,-1).replace('\n','').split(' ', 9 ))
	dict1[key.replace('\n','')] = value1

fo1.close()

#************************************************************#

b=0
a=0
total=0
IOU = 0.7                  #修改IOU得到自己想要的精度
P = []
R = []
for key in dict1:
    a = 0
    for i in range(1,dict1[key][0]+1):
        for j in range(1,dict[key][0]+1):
            b=calcIOU(float(dict1[key][i][0]),float(dict1[key][i][1]),float(dict1[key][i][2]),float(dict1[key][i][3]),float(dict[key][j][0]),float(dict[key][j][1]),float(dict[key][j][2]),float(dict[key][j][3]));
            if b>IOU:
                a=a+1
    if dict1[key][0] == 0:
        dict1[key][0] = 1
    P.append(a/dict1[key][0])
    R.append(a/dict[key][0])


print("精确率：",sum(P)/len(P))
print("召回率：",sum(R)/len(R))
print("交并比：",IOU)


# for key in dict:
#         total=total+ int(dict[key][0])
# total_2 = 0
# for key in dict1:
#         total_2 = total_2+int(dict1[key][0])
# print("原数据的脸数：",total)
# print("检测出的脸数：",total_2)
# print("交并比大于{0}的总数，TP：".format(IOU),a)
# print("精确率：", a / total_2)
# print("召回率:", a/total)
